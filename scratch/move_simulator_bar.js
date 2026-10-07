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

    // 1. Update CSS for .simulator-bar to be outside phone layer
    const oldSimCss = `        /* Demo Simulator Switcher */
        .simulator-bar {
            background: #f8fafc;
            border-bottom: 1px solid #e2e8f0;
            padding: 8px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 11px;
        }`;

    const newSimCss = `        /* Demo Simulator Switcher - Outside Phone Mockup */
        .simulator-bar {
            position: fixed;
            top: 14px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid #cbd5e1;
            border-radius: 30px;
            padding: 6px 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 11.5px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.16);
            z-index: 10000;
        }`;

    // Normalize for CRLF
    content = content.replace(/\r\n/g, '\n');
    const normOldSimCss = oldSimCss.replace(/\r\n/g, '\n');
    const normNewSimCss = newSimCss.replace(/\r\n/g, '\n');
    if (content.includes(normOldSimCss)) {
        content = content.replace(normOldSimCss, normNewSimCss);
    } else {
        // Fallback replace regex
        content = content.replace(/\/\* Demo Simulator Switcher \*\/[\s\S]*?font-size: 11px;\s*\}/, normNewSimCss);
    }

    // Adjust body padding so phone container doesn't get covered by top floating bar
    content = content.replace(/body\s*\{[\s\S]*?min-height: 100vh;[\s\S]*?padding: 10px 0;\s*\}/, `body {
            background-color: #cbd5e1;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 50px 0 20px;
        }`);

    // 2. Cut simulator-bar from inside .mobile-container and place outside
    const simBarHtml = `<!-- Simulator State Bar (Demo Test Switcher - Outside Phone Layer) -->
    <div class="simulator-bar">
        <div class="simulator-label">
            <i class="fa-solid fa-sliders" style="color: #2563eb;"></i>
            <span>Simulasi Kondisi:</span>
        </div>
        <div class="simulator-pills">
            <button type="button" class="sim-pill incomplete active" id="btnPillIncomplete" onclick="setEvidenceState('incomplete')">
                <i class="fa-solid fa-triangle-exclamation"></i> Tidak Lengkap (4/6)
            </button>
            <button type="button" class="sim-pill clear" id="btnPillClear" onclick="setEvidenceState('clear')">
                <i class="fa-solid fa-circle-check"></i> Lengkap Clear (6/6)
            </button>
        </div>
    </div>`;

    // Remove simulator-bar from inside mobile-container
    content = content.replace(/\s*<!-- Simulator State Bar \(Demo Test Switcher\) -->[\s\S]*?<\/div>\s*<\/div>/, '');

    // Place simulator-bar right before <div class="mobile-container">
    content = content.replace(/(<body>\s*)(<div class="mobile-container">)/, `$1    ${simBarHtml}\n\n    $2`);

    // Write back with CRLF
    fs.writeFileSync(file, content.replace(/\n/g, '\r\n'), 'utf8');
    console.log('Updated simulator bar in:', file);
});
