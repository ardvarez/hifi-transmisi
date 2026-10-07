const fs = require('fs');
const path = require('path');

function processPemasanganAction() {
    const file = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'pemasangan-action.html');
    let content = fs.readFileSync(file, 'utf8');

    // 1. Remove evidenceFailedBanner and restore clean 4 thumbnails in evidence-gallery-grid
    const oldMulaiSectionRegex = /<!-- Alert Banner status file gagal unduh -->[\s\S]*?<\/div>[\s\S]*?<!-- Evidence Selesai Card/m;
    
    const replacementMulai = `<div class="evidence-gallery-grid"
                        style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=mulai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence 1" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=mulai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1544724796-5f56436f5f1c?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence 2" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=mulai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=mulai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence (+2 Foto Lainnya)">
                            <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence 4" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                            <div
                                style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">
                                +2</div>
                        </div>
                    </div>
                </div>

                <!-- Evidence Selesai Card`;

    if (oldMulaiSectionRegex.test(content)) {
        content = content.replace(oldMulaiSectionRegex, replacementMulai);
        console.log('pemasangan-action.html Mulai grid updated successfully!');
    } else {
        console.log('Regex match failed for oldMulaiSectionRegex');
    }

    // 2. Also ensure Evidence Selesai thumbnails all have click triggers to gallery-evidence
    const oldSelesaiRegex = /<div class="spec-card" style="margin-bottom: 0; display: none;" id="cardEvidenceSelesai">[\s\S]*?<\/div>(\r?\n\s*<\/div>\r?\n\s*<\/div>)/;
    
    // Find cardEvidenceSelesai
    const idxCardSelesai = content.indexOf('id="cardEvidenceSelesai"');
    if (idxCardSelesai !== -1) {
        const nextSpecCard = content.indexOf('</div>\r\n\r\n                <!-- Catatan', idxCardSelesai);
        const nextSpecCardAlt = nextSpecCard !== -1 ? nextSpecCard : content.indexOf('</div>\n\n                <!-- Catatan', idxCardSelesai);
        
        if (nextSpecCardAlt !== -1) {
            let selesaiBlock = content.substring(idxCardSelesai, nextSpecCardAlt);
            
            // Replace thumbnails inside this block
            const replacementSelesaiGrid = `<div class="evidence-gallery-grid"
                        style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=selesai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 1" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=selesai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 2" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=selesai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                            <img src="https://images.unsplash.com/photo-1581092162384-8987c1d64718?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 3" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=selesai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence (+1 Foto Lainnya)">
                            <img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 4"
                                style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                            <div
                                style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">
                                +1</div>
                        </div>
                    </div>`;
            
            selesaiBlock = selesaiBlock.replace(/<div class="evidence-gallery-grid"[\s\S]*?<\/div>(\r?\n\s*<\/div>)?/, replacementSelesaiGrid + '\n                </div>');
            content = content.substring(0, idxCardSelesai) + selesaiBlock + content.substring(nextSpecCardAlt);
            console.log('pemasangan-action.html Selesai grid updated successfully!');
        }
    }

    // 3. Clean up refreshEvidenceMulai function
    const oldFnRegex = /function refreshEvidenceMulai\(\) \{[\s\S]*?function refreshEvidenceSelesai/m;
    const cleanFn = `function refreshEvidenceMulai() {
            const btn = document.getElementById('btnRefreshEvidenceMulai');
            const icon = document.getElementById('refreshEvidenceIcon');
            const txt = document.getElementById('refreshEvidenceText');
            if (!icon) return;

            icon.classList.add('fa-spin');
            if (txt) txt.textContent = 'Memuat...';
            if (btn) btn.style.pointerEvents = 'none';

            setTimeout(() => {
                icon.classList.remove('fa-spin');
                if (txt) txt.textContent = 'Refresh';
                if (btn) btn.style.pointerEvents = 'auto';
            }, 800);
        }

        function refreshEvidenceSelesai`;
    
    if (oldFnRegex.test(content)) {
        content = content.replace(oldFnRegex, cleanFn);
        console.log('refreshEvidenceMulai function simplified.');
    }

    fs.writeFileSync(file, content, 'utf8');
}

processPemasanganAction();
