const fs = require('fs');
const csv = fs.readFileSync('c:/KERJAAN/Project/hifi-transmisi/data/_select_mui_nama_as_uit_mup_nama_as_upt_mu_nama_as_ultg_mgi_nama_202606291304_unit.csv', 'utf8');
const lines = csv.split('\n').filter(l => l.trim() !== '');
const header = lines.shift();
const result = {};

lines.forEach(line => {
    // CSV lines might contain commas inside quotes.
    // Let's use a simple regex split for this if there are no complex quotes.
    const parts = line.split(',');
    if (parts.length >= 4) {
        const uit = parts[0].replace(/"/g, '').trim();
        const upt = parts[1].replace(/"/g, '').trim();
        const ultg = parts[2].replace(/"/g, '').trim();
        const gi = parts.slice(3).join(',').replace(/"/g, '').trim(); // Join remaining parts in case gi contains comma
        
        if (!result[uit]) result[uit] = {};
        if (!result[uit][upt]) result[uit][upt] = {};
        if (!result[uit][upt][ultg]) result[uit][upt][ultg] = [];
        
        if (gi && !result[uit][upt][ultg].includes(gi)) {
            result[uit][upt][ultg].push(gi);
        }
    }
});

const jsContent = 'const unitData = ' + JSON.stringify(result, null, 2) + ';\n\nif (typeof window !== "undefined") {\n  window.unitData = unitData;\n} else if (typeof module !== "undefined") {\n  module.exports = unitData;\n}';

fs.writeFileSync('c:/KERJAAN/Project/hifi-transmisi/data_unit_hierarchy.js', jsContent);
