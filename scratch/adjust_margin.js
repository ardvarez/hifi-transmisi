const fs = require('fs');
const path = require('path');

const galleryFiles = [
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'gallery-evidence.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'gallery-evidence.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'gallery-evidence.html')
];

galleryFiles.forEach(file => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace(/\r\n/g, '\n');

    content = content.replace(/margin-top:\s*10px;/g, 'margin-top: 0;');
    fs.writeFileSync(file, content.replace(/\n/g, '\r\n'), 'utf8');
});
console.log('Done updating filter-tabs-strip margin');
