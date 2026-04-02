const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const BASE_URL = 'https://eplan.help/ru-ru/Infoportal/Content/Plattform/2.9';

// Parse define({...}) wrapper
function parseDefine(filePath) {
    let content = fs.readFileSync(filePath, 'utf-8');
    content = content.replace(/^define\(/, '').replace(/\);\s*$/, '').replace(/\);$/, '');
    return new Function('return (' + content + ')')();
}

// 1. Build index -> { title, url } from all Toc_Chunk*.js files
const indexMap = {};

const chunkFiles = fs.readdirSync(DIR)
    .filter(f => /^Toc_Chunk\d+\.js$/.test(f))
    .sort();

for (const file of chunkFiles) {
    const data = parseDefine(path.join(DIR, file));
    for (const [urlPath, entry] of Object.entries(data)) {
        const indices = entry.i;
        const titles = entry.t;
        for (let j = 0; j < indices.length; j++) {
            const idx = indices[j];
            const title = (titles[j] !== undefined ? titles[j] : titles[0]) || '';
            indexMap[idx] = { title, urlPath };
        }
    }
}

console.log(`Loaded ${Object.keys(indexMap).length} index entries`);

// 2. Build URL from urlPath
function buildUrl(urlPath) {
    if (!urlPath || urlPath === '___') {
        return '___';
    }
    // /Content/htm/filename.htm  ->  BASE_URL/Content/htm/filename.htm
    return BASE_URL + urlPath;
}

// 3. Load Toc.js and get the tree
const tocData = parseDefine(path.join(DIR, 'Toc.js'));
const tree = tocData.tree;

// 4. Recursively build output nodes
function buildNode(node) {
    const info = indexMap[node.i];
    const result = {};

    if (info) {
        result.title = info.title;
        const url = buildUrl(info.urlPath);
        result.link = url === '___'
            ? BASE_URL + '___'
            : url;
    } else {
        result.title = `[${node.i}]`;
        result.link = BASE_URL + '___';
    }

    if (node.n && node.n.length > 0) {
        result.children = node.n.map(child => buildNode(child));
    }

    return result;
}

// Root tree.n is the top-level array
const output = tree.n.map(node => buildNode(node));

const outPath = path.join(DIR, 'tree29.json');
fs.writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf-8');
console.log(`Done! Wrote tree29.json (${output.length} root nodes)`);