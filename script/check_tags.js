const fs = require('fs');
const path = require('path');
const vm = require('vm');

function getAllFiles(dir, ext = '.html') {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      if (file !== 'node_modules' && file !== '.git') {
        results = results.concat(getAllFiles(fullPath, ext));
      }
    } else if (file.endsWith(ext)) {
      results.push(fullPath);
    }
  });
  return results;
}

const dirsToCheck = ['./hifi-mobile', './hifi-power-inspect', './hifi-ers', './hifi-new-pst', './hifi-home'];
let allHtmlFiles = [];
dirsToCheck.forEach(d => {
  if (fs.existsSync(d)) {
    allHtmlFiles = allHtmlFiles.concat(getAllFiles(d));
  }
});

console.log(`Scanning ${allHtmlFiles.length} HTML files...`);

const tagsToCheck = ['div', 'span', 'svg', 'button', 'script', 'style', 'head', 'body', 'html', 'table', 'tbody', 'tr', 'td', 'th', 'ul', 'ol', 'li', 'header', 'footer', 'main', 'section', 'a'];

let totalIssues = 0;

allHtmlFiles.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  let issues = [];

  // Check unclosed or unbalanced tags
  tagsToCheck.forEach(tag => {
    const openRegex = new RegExp('<' + tag + '(\\s+[^>]*)?>', 'gi');
    const closeRegex = new RegExp('</' + tag + '>', 'gi');
    const openMatches = content.match(openRegex) || [];
    const closeMatches = content.match(closeRegex) || [];
    if (openMatches.length !== closeMatches.length) {
      issues.push(`${tag} tag mismatch: <${tag}> = ${openMatches.length}, </${tag}> = ${closeMatches.length}`);
    }
  });

  // Check for multiple html or body
  const htmlOpens = (content.match(/<html/gi) || []).length;
  if (htmlOpens > 1) issues.push(`Multiple <html> tags: ${htmlOpens}`);
  const bodyOpens = (content.match(/<body/gi) || []).length;
  if (bodyOpens > 1) issues.push(`Multiple <body> tags: ${bodyOpens}`);

  // Check for leaked tags before <body>
  const bodyPos = content.indexOf('<body');
  if (bodyPos > -1) {
    const headContent = content.substring(0, bodyPos);
    // Leaked div or svg in head (outside script/style)
    const headStripped = headContent
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<style[\s\S]*?<\/style>/gi, '');
    
    if (headStripped.includes('</div>') || headStripped.includes('</svg>') || headStripped.includes('<div') || headStripped.includes('<svg')) {
      issues.push(`Leaked HTML tags inside <head> before <body>!`);
    }
  }

  // Check for content after </html>
  const htmlClosePos = content.indexOf('</html>');
  if (htmlClosePos > -1) {
    const afterHtml = content.substring(htmlClosePos + 7).trim();
    if (afterHtml.length > 0 && !afterHtml.startsWith('<!--')) {
      issues.push(`Trailing content after </html>: ${afterHtml.substring(0, 50)}...`);
    }
  }

  // Check script syntax
  const scriptRegex = /<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIdx = 0;
  while ((match = scriptRegex.exec(content)) !== null) {
    scriptIdx++;
    const scriptTag = match[0].split('>')[0];
    if (scriptTag.includes('type="module"') || scriptTag.includes('type="application/json"') || scriptTag.includes('type="text/template"')) {
      continue;
    }
    const scriptCode = match[1];
    if (!scriptCode.trim()) continue;
    try {
      new vm.Script(scriptCode);
    } catch (e) {
      issues.push(`Script #${scriptIdx} JS syntax error: ${e.message}`);
    }
  }

  if (issues.length > 0) {
    totalIssues += issues.length;
    console.log(`\n[ISSUE] ${f}`);
    issues.forEach(iss => console.log(`  - ${iss}`));
  }
});

console.log(`\nScan complete! Found ${totalIssues} issue(s).`);
