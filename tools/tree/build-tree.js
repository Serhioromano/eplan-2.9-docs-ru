const fs = require('fs');
const path = require('path');

// Parse define({...}) files by extracting the object
function parseDefineFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf-8');
    // Remove the define( wrapper and trailing );
    content = content.replace(/^define\(/, '').replace(/\);\s*$/, '');
    // Use Function constructor to evaluate the JS object literal
    return new Function('return (' + content + ')')();
}

// 1. Load all db files and build index->{ title, url } map
const indexMap = {}; // i -> { title, url }

for (let i = 1; i <= 9; i++) {
    const dbPath = path.join(__dirname, `db${i}.js`);
    const db = parseDefineFile(dbPath);
    for (const [url, entry] of Object.entries(db)) {
        if (entry.i && entry.t) {
            for (let j = 0; j < entry.i.length; j++) {
                indexMap[entry.i[j]] = {
                    title: entry.t[j] || entry.t[0],
                    url: url
                };
            }
        }
    }
}

// 2. Load root.js and extract tree + prefix info
const rootData = parseDefineFile(path.join(__dirname, 'root.js'));
const tree = rootData.tree;

const BASE_URL = 'https://www.eplan.help/ru-ru/Infoportal/Content/Plattform/2026';

// 3. Recursively build the output tree
function buildNode(node) {
    const info = indexMap[node.i];
    const result = {};

    if (info) {
        result.title = info.title;
        // Build the link from the URL path
        // URLs in db look like '/Content/htm/xxx.htm'
        result.link = BASE_URL + info.url;
    } else {
        result.title = `[Unknown index ${node.i}]`;
        result.link = '';
    }

    if (node.n && node.n.length > 0) {
        result.children = node.n.map(child => buildNode(child));
    }

    return result;
}

// The root tree has a top-level 'n' array
const output = tree.n.map(node => buildNode(node));

fs.writeFileSync(
    path.join(__dirname, 'tree.json'),
    JSON.stringify(output, null, 2),
    'utf-8'
);

console.log(`Done! Generated tree.json with ${Object.keys(indexMap).length} indexed entries.`);
