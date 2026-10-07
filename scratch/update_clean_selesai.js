const fs = require('fs');
const path = require('path');

const files = [
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'pemasangan-action.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'pembongkaran-action.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Karantina & Pengembalian', 'karantina-action.html')
];

files.forEach(file => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    // Make sure in cardEvidenceSelesai, all thumb-boxes have onclick to gallery-evidence
    const selesaiMatch = content.indexOf('id="cardEvidenceSelesai"');
    if (selesaiMatch !== -1) {
        let before = content.substring(0, selesaiMatch);
        let after = content.substring(selesaiMatch);
        
        // Find closing of this spec-card
        let cardEnd = after.indexOf('</div>\r\n\r\n');
        if (cardEnd === -1) cardEnd = after.indexOf('</div>\n\n');
        if (cardEnd !== -1) {
            let cardContent = after.substring(0, cardEnd);
            let rest = after.substring(cardEnd);
            
            // Add onclick and cursor pointer to any evidence-thumb-box without onclick in cardContent
            cardContent = cardContent.replace(/<div class="evidence-thumb-box"(?![^>]*onclick)/g, '<div class="evidence-thumb-box" onclick="window.location.href=\'./gallery-evidence.html?type=selesai\'"');
            cardContent = cardContent.replace(/style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;"/g, 'style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence"');
            
            content = before + cardContent + rest;
        }
    }

    fs.writeFileSync(file, content, 'utf8');
    console.log('Processed:', file);
});
