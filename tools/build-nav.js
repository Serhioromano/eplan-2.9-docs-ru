const fs = require('fs');
const path = require('path');

const tree = JSON.parse(fs.readFileSync(path.join(__dirname, 'tree.json'), 'utf-8'));
const docsDir = path.join(__dirname, 'docs', 'eplan');

// Get set of existing md files
const existingFiles = new Set(
  fs.readdirSync(docsDir).filter(f => f.endsWith('.md'))
);

// Extract filename from URL: last segment, .htm -> .md
function urlToFile(link) {
  if (!link || link.endsWith('___')) return null;
  const match = link.match(/\/([^/]+)\.htm$/);
  if (!match) return null;
  const mdFile = match[1] + '.md';
  return existingFiles.has(mdFile) ? 'eplan/' + mdFile : null;
}

// Convert tree node to YAML nav entry
function nodeToYaml(node, indent) {
  const prefix = '  '.repeat(indent) + '- ';
  const file = urlToFile(node.link);
  const lines = [];

  if (node.children && node.children.length > 0) {
    // Collect child lines first to check if any have content
    const childLines = [];
    if (file) {
      childLines.push('  '.repeat(indent + 1) + '- ' + JSON.stringify(node.title) + ': ' + file);
    }
    for (const child of node.children) {
      childLines.push(...nodeToYaml(child, indent + 1));
    }
    // Only emit section if it has at least one child entry
    if (childLines.length > 0) {
      lines.push(prefix + JSON.stringify(node.title) + ':');
      lines.push(...childLines);
    }
  } else if (file) {
    lines.push(prefix + JSON.stringify(node.title) + ': ' + file);
  }

  return lines;
}

const navLines = ['nav:', '  - Главная: index.md'];
for (const topNode of tree) {
  navLines.push(...nodeToYaml(topNode, 1));
}

const navYaml = navLines.join('\n');
fs.writeFileSync(path.join(__dirname, 'nav.yml'), navYaml, 'utf-8');
console.log('Generated nav.yml');
