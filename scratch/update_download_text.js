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

    // Replace button text and title in header
    content = content.replace(
        /<button type="button" class="header-action-btn" onclick="downloadAllPhotos\(\)" title="Unduh Semua Foto">\s*<i class="fa-solid fa-cloud-arrow-down"><\/i>\s*<span>Unduh Semua<\/span>\s*<\/button>/g,
        `<button type="button" class="header-action-btn" onclick="downloadAllPhotos()" title="Unduh Foto Evidence">
                <i class="fa-solid fa-cloud-arrow-down"></i>
                <span>Unduh Foto</span>
            </button>`
    );

    // Also update toast text in downloadAllPhotos
    content = content.replace(
        /showToast\(`Mengunduh \$\{count\} berkas foto evidence \(ZIP\)\.\.\.`,\s*'fa-cloud-arrow-down'\);/g,
        `showToast(\`Mengunduh \${count} berkas foto evidence...\`, 'fa-cloud-arrow-down');`
    );

    fs.writeFileSync(file, content.replace(/\n/g, '\r\n'), 'utf8');
    console.log('Updated download button in:', file);
});
