const fs = require('fs');
const path = require('path');

const galleryFile = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'gallery-evidence.html');
let content = fs.readFileSync(galleryFile, 'utf8');

// Update init script in gallery-evidence.html
const oldInitPattern = /\/\/ Initialize[\s\S]*?<\/script>/;
const newInitCode = `// Initialize
        const urlParams = new URLSearchParams(window.location.search);
        const stateParam = urlParams.get('state');
        const fromParam = urlParams.get('from');
        const typeParam = urlParams.get('type');
        const indexParam = urlParams.get('index');

        // Dynamic Back Button
        const backBtn = document.querySelector('.back-btn');
        if (backBtn) {
            if (fromParam === 'pembongkaran') {
                backBtn.href = '../Pembongkaran/pembongkaran-action.html';
                document.getElementById('pageSubTitle').textContent = 'Pembongkaran • DKL20250000001-01';
            } else if (fromParam === 'karantina') {
                backBtn.href = '../Karantina & Pengembalian/karantina-action.html';
                document.getElementById('pageSubTitle').textContent = 'Karantina • KRT20250000001-01';
            } else {
                backBtn.href = './pemasangan-action.html';
            }
        }

        if (stateParam === 'clear') {
            setEvidenceState('clear');
        } else {
            setEvidenceState('incomplete');
        }

        const idParam = urlParams.get('id');
        if (idParam) {
            const prefix = fromParam === 'pembongkaran' ? 'Pembongkaran' : 'Pemasangan';
            document.getElementById('pageSubTitle').textContent = \`\${prefix} • \${idParam}\`;
        }

        // Auto filter by type if requested
        if (typeParam === 'mulai') {
            const chipMulai = document.getElementById('chipTabMulai');
            filterGallery('mulai', chipMulai);
        } else if (typeParam === 'selesai') {
            const chipSelesai = document.getElementById('chipTabSelesai');
            filterGallery('selesai', chipSelesai);
        }

        // Open specific photo if index param passed
        if (indexParam !== null && !isNaN(parseInt(indexParam))) {
            const targetIdx = parseInt(indexParam);
            setTimeout(() => {
                if (currentFilteredList[targetIdx] && currentFilteredList[targetIdx].available) {
                    openLightbox(targetIdx);
                }
            }, 300);
        }
    </script>`;

content = content.replace(oldInitPattern, newInitCode);

// Write to Pemasangan, Pembongkaran, and root ers
fs.writeFileSync(galleryFile, content, 'utf8');

const pembongkaranGallery = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'gallery-evidence.html');
const rootErsGallery = path.join(__dirname, '..', 'hifi-mobile', 'ers', 'gallery-evidence.html');
fs.writeFileSync(pembongkaranGallery, content, 'utf8');
fs.writeFileSync(rootErsGallery, content, 'utf8');

console.log('Synchronized gallery-evidence.html across all locations!');
