import os
import re

base_file = r'c:\KERJAAN\Project\hifi-transmisi\hifi-new-pst\Master Sub-sistem\tambah-data-sub-sistem.html'
out_file = r'c:\KERJAAN\Project\hifi-transmisi\hifi-new-pst\Master Sub-sistem\mainpage-osl.html'

with open(base_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <title>
content = content.replace('<title>Master Sub-sistem – Tambah Data – PLN</title>', '<title>Master OSL – PLN</title>')

# Inject tab CSS just before </style>
css_to_add = """
        /* TABS */
        .tabs {
            display: flex;
            gap: 8px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }

        .tab-btn {
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 500;
            color: var(--text-secondary);
            background: transparent;
            border: none;
            border-bottom: 3px solid transparent;
            cursor: pointer;
            transition: all 0.2s;
        }

        .tab-btn:hover {
            color: var(--pln-blue);
            background: var(--surface);
        }

        .tab-btn.active {
            color: var(--pln-blue);
            font-weight: 600;
            border-bottom-color: var(--pln-blue);
        }

        .tab-pane {
            display: none;
        }

        .tab-pane.active {
            display: block;
        }
"""
content = content.replace('</style>', css_to_add + '\n</style>')

# Replace the topbar
topbar_start = content.find('<header class="topbar">')
topbar_end = content.find('</header>') + len('</header>')
new_topbar = """<header class="topbar">
            <div class="topbar-left">
                <div>
                    <div class="page-title">Master OSL</div>
                    <div class="breadcrumb">
                        <a href="#">Master OSL</a>
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <path d="M9 18l6-6-6-6" />
                        </svg>
                        <span>Mainpage</span>
                    </div>
                </div>
            </div>
            <div class="topbar-right">
                <span>Contact us: helpdesk_pi@iconpln.co.id | Security issue: soc@pln.co.id</span>
            </div>
        </header>"""
content = content[:topbar_start] + new_topbar + content[topbar_end:]

# Replace the content area
main_content_start = content.find('<main class="content">')
main_content_end = content.find('</main>') + len('</main>')
new_main_content = """<main class="content">
            <div class="tabs">
                <button class="tab-btn active" onclick="openTab('sistem', this)">Data Sistem</button>
                <button class="tab-btn" onclick="openTab('subsistem', this)">Data Sub-sistem</button>
            </div>

            <div id="sistem" class="tab-pane active section-card">
                <div class="toolbar" style="display:flex; justify-content:space-between; margin-bottom: 16px;">
                    <input type="text" placeholder="Cari data sistem..." style="padding: 8px 14px; border: 1px solid var(--border); border-radius: var(--radius-sm); width: 300px; font-size: 13px;">
                    <a href="tambah-data-sistem.html" class="btn-submit" style="text-decoration:none; display:inline-block; padding: 10px 20px;">+ Tambah Data</a>
                </div>
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="border-bottom: 1px solid var(--border);">
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">No</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Nama Sistem</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Unit Induk P2B</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Kapasitas (MW)</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid var(--border);">
                            <td style="padding: 12px;">1</td>
                            <td style="padding: 12px;">Sistem Jamali</td>
                            <td style="padding: 12px;">UIP2B Jamali</td>
                            <td style="padding: 12px;">400</td>
                            <td style="padding: 12px;">
                                <a href="#" style="color:var(--pln-blue); text-decoration:none; font-weight: 500;">Edit</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div id="subsistem" class="tab-pane section-card">
                <div class="toolbar" style="display:flex; justify-content:space-between; margin-bottom: 16px;">
                    <input type="text" placeholder="Cari data sub-sistem..." style="padding: 8px 14px; border: 1px solid var(--border); border-radius: var(--radius-sm); width: 300px; font-size: 13px;">
                    <a href="tambah-data-sub-sistem.html" class="btn-submit" style="text-decoration:none; display:inline-block; padding: 10px 20px;">+ Tambah Data</a>
                </div>
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="border-bottom: 1px solid var(--border);">
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">No</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Sistem</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Nama Sub-sistem</th>
                            <th style="padding: 12px; font-weight: 600; color: var(--text-secondary);">Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid var(--border);">
                            <td style="padding: 12px;">1</td>
                            <td style="padding: 12px;">Sistem Jamali</td>
                            <td style="padding: 12px;">Subsistem A</td>
                            <td style="padding: 12px;">
                                <a href="#" style="color:var(--pln-blue); text-decoration:none; font-weight: 500;">Edit</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </main>"""
content = content[:main_content_start] + new_main_content + content[main_content_end:]

# Replace the footer (since it's a list page, no form footer needed)
footer_start = content.find('<!-- FOOTER -->')
footer_end = content.find('</footer>') + len('</footer>')
if footer_start != -1:
    content = content[:footer_start] + content[footer_end:]

# Replace Javascript with just the tab function
js_start = content.find('<script>')
js_end = content.find('</script>') + len('</script>')
new_js = """<script>
        function openTab(tabId, element) {
            const panes = document.querySelectorAll('.tab-pane');
            panes.forEach(pane => pane.classList.remove('active'));
            
            const btns = document.querySelectorAll('.tab-btn');
            btns.forEach(btn => btn.classList.remove('active'));

            document.getElementById(tabId).classList.add('active');
            element.classList.add('active');
        }
    </script>"""
content = content[:js_start] + new_js + content[js_end:]

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {out_file}")
