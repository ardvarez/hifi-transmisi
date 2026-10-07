const fs = require('fs');
const path = require('path');

const galleryFiles = [
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pemasangan', 'gallery-evidence.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'Pembongkaran', 'gallery-evidence.html'),
    path.join(__dirname, '..', 'hifi-mobile', 'ers', 'gallery-evidence.html')
];

const newToastCss = `        /* Toast notification */
        .toast-bubble {
            position: absolute;
            top: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(-50px);
            background: #0f172a;
            color: #ffffff;
            padding: 10px 16px;
            border-radius: 16px;
            font-size: 11.5px;
            font-weight: 600;
            line-height: 1.45;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 3000;
            width: max-content;
            max-width: calc(100% - 36px);
            box-sizing: border-box;
            white-space: normal;
            word-break: break-word;
            text-align: left;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }

        .toast-bubble i {
            flex-shrink: 0;
            font-size: 14px;
        }

        .toast-bubble span {
            flex: 1;
        }

        .toast-bubble.show {
            opacity: 1;
            visibility: visible;
            transform: translateX(-50%) translateY(0);
        }`;

galleryFiles.forEach(file => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace(/\r\n/g, '\n');

    const toastRegex = /\/\* Toast notification \*\/[\s\S]*?\.toast-bubble\.show \{[\s\S]*?\}/;
    if (toastRegex.test(content)) {
        content = content.replace(toastRegex, newToastCss);
        fs.writeFileSync(file, content.replace(/\n/g, '\r\n'), 'utf8');
        console.log('Updated toast in:', file);
    } else {
        console.log('Toast regex not found in:', file);
    }
});

// Update login.html as well
const loginFile = path.join(__dirname, '..', 'hifi-mobile', 'login.html');
if (fs.existsSync(loginFile)) {
    let content = fs.readFileSync(loginFile, 'utf8');
    content = content.replace(/\r\n/g, '\n');

    const oldLoginToastRegex = /\/\* Toast Notification \*\/[\s\S]*?\.toast-bubble\.show \{[\s\S]*?\}/;
    const newLoginToastCss = `/* Toast Notification */
        .toast-bubble {
            position: absolute;
            top: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(-50px);
            background: #0f172a;
            color: #ffffff;
            padding: 10px 18px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            line-height: 1.4;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 2000;
            width: max-content;
            max-width: calc(100% - 36px);
            box-sizing: border-box;
            white-space: normal;
            word-break: break-word;
            text-align: left;
            pointer-events: none;
            border: 1px solid rgba(255, 255, 255, 0.12);
        }

        .toast-bubble i {
            flex-shrink: 0;
            font-size: 14px;
        }

        .toast-bubble span {
            flex: 1;
        }

        .toast-bubble.show {
            opacity: 1;
            visibility: visible;
            transform: translateX(-50%) translateY(0);
        }`;

    if (oldLoginToastRegex.test(content)) {
        content = content.replace(oldLoginToastRegex, newLoginToastCss);
        fs.writeFileSync(loginFile, content.replace(/\n/g, '\r\n'), 'utf8');
        console.log('Updated toast in login.html');
    }
}
