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

    // 1. Add id to sync-status-strip if not present
    content = content.replace(/<div class="sync-status-strip"(?! id=)/g, '<div class="sync-status-strip" id="syncStatusStrip"');

    // 2. Update setEvidenceState implementation
    const oldFnRegex = /function setEvidenceState\(state\) \{[\s\S]*?filterGallery\(currentFilter\);\s*\}/;

    const newFn = `function setEvidenceState(state) {
            currentEvidenceState = state;

            const pillInc = document.getElementById('btnPillIncomplete');
            const pillClr = document.getElementById('btnPillClear');
            const syncStrip = document.getElementById('syncStatusStrip');
            const banner = document.getElementById('evidenceCaseBanner');
            const bannerIcon = document.getElementById('bannerIcon');
            const bannerTitle = document.getElementById('bannerTitle');
            const bannerDesc = document.getElementById('bannerDesc');
            const btnBanner = document.getElementById('btnBannerAction');
            const syncIcon = document.getElementById('syncIcon');
            const syncText = document.getElementById('syncText');
            const chipAll = document.getElementById('chipTabAll');
            const chipMulai = document.getElementById('chipTabMulai');
            const chipSelesai = document.getElementById('chipTabSelesai');

            if (state === 'incomplete') {
                if (pillInc) pillInc.classList.add('active');
                if (pillClr) pillClr.classList.remove('active');

                // Tampilkan info refresh & banner ketika status belum lengkap
                if (syncStrip) syncStrip.style.display = 'flex';
                if (banner) {
                    banner.style.display = 'flex';
                    banner.className = 'evidence-case-banner banner-incomplete';
                    if (bannerIcon) {
                        bannerIcon.className = 'fa-solid fa-triangle-exclamation';
                        bannerIcon.style.color = '#d97706';
                    }
                    if (bannerTitle) bannerTitle.textContent = 'Foto Evidence Belum Lengkap (4/6)';
                    if (bannerDesc) bannerDesc.innerHTML = 'Masih kurang 2 foto wajib tahap penyelesaian. Tekan <strong>Refresh</strong> untuk sinkronisasi otomatis.';
                    if (btnBanner) {
                        btnBanner.className = 'banner-btn-action btn-banner-refresh';
                        btnBanner.innerHTML = '<i class="fa-solid fa-arrows-rotate"></i> Refresh';
                        btnBanner.onclick = refreshToClearState;
                    }
                }

                if (syncIcon) {
                    syncIcon.className = 'fa-solid fa-circle-exclamation';
                    syncIcon.style.color = '#d97706';
                }
                if (syncText) syncText.textContent = 'Dokumentasi belum lengkap (4/6 foto) • Perlu Refresh';

                if (chipAll) chipAll.textContent = 'Semua (4)';
                if (chipMulai) chipMulai.textContent = 'Evidence Mulai (4)';
                if (chipSelesai) chipSelesai.textContent = 'Evidence Selesai (0)';
            } else {
                if (pillClr) pillClr.classList.add('active');
                if (pillInc) pillInc.classList.remove('active');

                // HIDE semua bar & banner informasi refresh saat sudah berhasil (Clear) agar galeri lebih luas
                if (syncStrip) syncStrip.style.display = 'none';
                if (banner) banner.style.display = 'none';

                if (chipAll) chipAll.textContent = 'Semua (6)';
                if (chipMulai) chipMulai.textContent = 'Evidence Mulai (4)';
                if (chipSelesai) chipSelesai.textContent = 'Evidence Selesai (2)';
            }

            filterGallery(currentFilter);
        }`;

    if (oldFnRegex.test(content)) {
        content = content.replace(oldFnRegex, newFn);
        fs.writeFileSync(file, content.replace(/\n/g, '\r\n'), 'utf8');
        console.log('Updated setEvidenceState in:', file);
    } else {
        console.log('Regex did not match in:', file);
    }
});
