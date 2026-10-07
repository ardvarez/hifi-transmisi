const fs = require('fs');
const path = require('path');

function cleanPembongkaranAction() {
    const file = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'pembongkaran-action.html');
    let content = fs.readFileSync(file, 'utf8');

    // 1. Evidence Pembongkaran: remove banner & dashed failed slot, make all 4 thumbnails clean & clickable
    const bongkarGridRegex = /<!-- Alert Banner status file gagal unduh -->[\s\S]*?<\/div>[\s\S]*?<\/div>(\r?\n\s*<\/div>\r?\n\s*<\/div>\r?\n\s*<!-- SECTION 2)/m;
    const replacementBongkar = `<div class="evidence-gallery-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80" alt="Evidence 1" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1544724796-5f56436f5f1c?auto=format&fit=crop&w=300&q=80" alt="Evidence 2" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80" alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=bongkar'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence (+2 Foto Lainnya)">
                                <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=300&q=80" alt="Evidence 4" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                                <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">+2</div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- SECTION 2`;

    if (bongkarGridRegex.test(content)) {
        content = content.replace(bongkarGridRegex, replacementBongkar);
        console.log('pembongkaran-action.html Bongkar grid updated!');
    } else {
        console.log('bongkarGridRegex not matched');
    }

    // 2. Evidence Pemasangan Historical grid in Pembongkaran: make all clickable
    const pasangOldGrid = `<div class="evidence-gallery-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                            <div class="evidence-thumb-box" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                                <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80" alt="Evidence 1" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                                <img src="https://images.unsplash.com/photo-1544724796-5f56436f5f1c?auto=format&fit=crop&w=300&q=80" alt="Evidence 2" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1;">
                                <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80" alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1;">
                                <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=300&q=80" alt="Evidence 4" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                                <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">+2</div>
                            </div>
                        </div>`;

    const pasangNewGrid = `<div class="evidence-gallery-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=mulai'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80" alt="Evidence 1" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=mulai'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1544724796-5f56436f5f1c?auto=format&fit=crop&w=300&q=80" alt="Evidence 2" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=mulai'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #e2e8f0; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence">
                                <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=300&q=80" alt="Evidence 3" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <div class="evidence-thumb-box" onclick="window.location.href='./gallery-evidence.html?from=pembongkaran&type=mulai'" style="position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; background: #334155; border: 1px solid #cbd5e1; cursor: pointer;" title="Lihat Galeri Foto Evidence (+2 Foto Lainnya)">
                                <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=300&q=80" alt="Evidence 4" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.45;">
                                <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.6);">+2</div>
                            </div>
                        </div>`;

    if (content.includes(pasangOldGrid)) {
        content = content.replace(pasangOldGrid, pasangNewGrid);
        console.log('pembongkaran-action.html Pasang historical grid updated!');
    }

    // Clean refresh function
    const oldBongkarFnRegex = /function refreshEvidenceBongkar\(\) \{[\s\S]*?function refreshEvidencePasang/m;
    const cleanBongkarFn = `function refreshEvidenceBongkar() {
            const btn = document.getElementById('btnRefreshEvidenceBongkar');
            const icon = document.getElementById('refreshBongkarIcon');
            const txt = document.getElementById('refreshBongkarText');
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

        function refreshEvidencePasang`;
    if (oldBongkarFnRegex.test(content)) {
        content = content.replace(oldBongkarFnRegex, cleanBongkarFn);
        console.log('refreshEvidenceBongkar cleaned.');
    }

    fs.writeFileSync(file, content, 'utf8');
}

cleanPembongkaranAction();
