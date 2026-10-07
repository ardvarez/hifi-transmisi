const fs = require('fs');
const path = require('path');

const targetFiles = [
    path.join(__dirname, '..', 'hifi-mobile', 'ers-v2', 'Pemasangan', 'pemasangan-action.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers-v2', 'Pembongkaran', 'pembongkaran-action.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers-v2', 'Karantina & Pengembalian', 'karantina-action.html')
];

targetFiles.forEach(filePath => {
    if (!fs.existsSync(filePath)) return;
    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Remove any failed banner
    content = content.replace(/<div id="[^"]*FailedBanner"[\s\S]*?<\/div>\r?\n\s*<\/div>/g, '');

    // 2. Replace any failed slot with normal clean photo slot
    const failedSlotRegex = /<!-- Slot 3: File yang gagal terunduh[^>]*-->[\s\S]*?<\/div>/g;
    const cleanSlot = `<div class="evidence-thumb-box" onclick="window.location.href='../../ers/Pemasangan/gallery-evidence.html'"
                            style="position: relative; aspect-ratio: 1; border-radius: 10px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>`;
    content = content.replace(failedSlotRegex, cleanSlot);

    // 3. Ensure all evidence-thumb-box have cursor pointer and gallery trigger
    content = content.replace(/<div class="evidence-thumb-box"(?![^>]*onclick)/g, `<div class="evidence-thumb-box" onclick="window.location.href='../../ers/Pemasangan/gallery-evidence.html'" cursor: pointer;`);

    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Cleaned V2:', filePath);
});
