const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'pemasangan-action.html');
let content = fs.readFileSync(file, 'utf8');

const oldSelesaiGrid = `<div class="evidence-gallery-grid"
                        style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="evidence-thumb-box"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                            <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 1" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                            <img src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 2" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                            <img src="https://images.unsplash.com/photo-1581092162384-8987c1d64718?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 3" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?type=selesai'"
                            style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Buka Galeri Evidence">
                            <img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=300&q=80"
                                alt="Evidence Selesai 4"
                                style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                            <div
                                style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">
                                +1</div>
                        </div>
                    </div>`;

const newSelesaiGrid = `<div class="evidence-gallery-grid"
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

// Normalize \r\n
const normContent = content.replace(/\r\n/g, '\n');
const normOld = oldSelesaiGrid.replace(/\r\n/g, '\n');
const normNew = newSelesaiGrid.replace(/\r\n/g, '\n');

if (normContent.includes(normOld)) {
    const updated = normContent.replace(normOld, normNew);
    // Write back with CRLF
    fs.writeFileSync(file, updated.replace(/\n/g, '\r\n'), 'utf8');
    console.log('Successfully updated pemasangan-action.html Selesai grid thumbnails!');
} else {
    console.log('Old grid not matched');
}
