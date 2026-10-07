const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'pembongkaran-action.html');
let content = fs.readFileSync(file, 'utf8');

// Replace evidenceBongkarFailedBanner and grid
const startMarker = '<div id="evidenceBongkarFailedBanner"';
const endMarker = '<!-- SECTION 2: PEMASANGAN';

const startIdx = content.indexOf(startMarker);
const endIdx = content.indexOf(endMarker);

if (startIdx !== -1 && endIdx !== -1) {
    const replacement = `<div class="evidence-gallery-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'"
                                style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80" alt="Evidence 1" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'"
                                style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1544724796-5f56436f5f1c?auto=format&fit=crop&w=300&q=80" alt="Evidence 2" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'"
                                style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80" alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'"
                                style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence (+2 Foto Lainnya)">
                                <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=300&q=80" alt="Evidence 4" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                                <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">+2</div>
                            </div>
                        </div>
                    </div>
                </div>

                `;

    content = content.substring(0, startIdx) + replacement + content.substring(endIdx);
    fs.writeFileSync(file, content, 'utf8');
    console.log('Successfully updated pembongkaran-action.html grid!');
} else {
    console.log('Markers not found:', startIdx, endIdx);
}
