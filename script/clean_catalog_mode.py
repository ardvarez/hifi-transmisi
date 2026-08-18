import os
import re

ers_dir = r"c:\KERJAAN\Project\hifi-transmisi\hifi-mobile\ers"

subfolders = [
    {
        "dir": "Pemasangan",
        "active_tab": 2
    },
    {
        "dir": "Pembongkaran",
        "active_tab": 3
    },
    {
        "dir": "Karantina & Pengembalian",
        "active_tab": 4
    },
    {
        "dir": "Stock Opname",
        "active_tab": 5
    }
]

navbar_css_template = """
        /* 5-TAB BOTTOM NAVBAR */
        .bottom-nav-5tabs {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 66px;
            background: #ffffff;
            border-top: 1px solid #e2e8f0;
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 0 4px 8px;
            z-index: 100;
            box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.04);
        }

        .tab-5-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 700;
            color: #94a3b8;
            cursor: pointer;
            gap: 4px;
            text-decoration: none;
            width: 20%;
            transition: color 0.2s;
            position: relative;
            padding: 4px 0;
        }

        .tab-5-item.active {
            color: #0A58CA;
        }

        .tab-5-item i {
            font-size: 17px;
        }

        .ios-bar {
            position: absolute;
            bottom: 4px;
            left: 50%;
            transform: translateX(-50%);
            width: 110px;
            height: 4px;
            background: #0f172a;
            border-radius: 2px;
            z-index: 101;
        }
"""

def make_navbar_html(active_index):
    t1 = 'active' if active_index == 1 else ''
    t2 = 'active' if active_index == 2 else ''
    t3 = 'active' if active_index == 3 else ''
    t4 = 'active' if active_index == 4 else ''
    t5 = 'active' if active_index == 5 else ''

    return f"""
        <!-- 5-TAB BOTTOM NAVBAR -->
        <nav class="bottom-nav-5tabs">
            <a href="../home-mobile-nav.html" class="tab-5-item {t1}" title="Dashboard Root">
                <i class="fa-solid fa-chart-pie"></i>
                <span>Dashboard</span>
            </a>
            <a href="../Pemasangan/home-mobile-nav.html" class="tab-5-item {t2}" title="Pemasangan ERS">
                <i class="fa-solid fa-wrench"></i>
                <span>Pemasangan</span>
            </a>
            <a href="../Pembongkaran/home-mobile-nav.html" class="tab-5-item {t3}" title="Pembongkaran ERS">
                <i class="fa-solid fa-truck-ramp-box"></i>
                <span>Pembongkaran</span>
            </a>
            <a href="../Karantina & Pengembalian/home-mobile-nav.html" class="tab-5-item {t4}" title="Karantina & Pengembalian">
                <i class="fa-solid fa-box-archive"></i>
                <span>Karantina</span>
            </a>
            <a href="../Stock Opname/home-mobile-nav.html" class="tab-5-item {t5}" title="Stok Opname ERS">
                <i class="fa-solid fa-boxes-stacked"></i>
                <span>Stok Opnam</span>
            </a>
        </nav>
        <div class="ios-bar"></div>
"""

def clean_navbars_from_html(html_str):
    # Remove any nav tags
    html_str = re.sub(r'<nav class="bottom-nav[^"]*">.*?</nav>', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'<nav class="bottom-nav-5tabs">.*?</nav>', '', html_str, flags=re.DOTALL)
    # Remove nav CSS
    html_str = re.sub(r'/\* 5-TAB BOTTOM NAVBAR \*/.*?\.ios-bar\s*\{[^}]*\}', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'\.bottom-nav\s*\{[^}]*\}', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'\.bottom-nav-5tabs\s*\{[^}]*\}', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'\.tab-5-item[^{]*\{[^}]*\}', '', html_str, flags=re.DOTALL)
    # Adjust padding-bottom for catalog mode
    html_str = re.sub(r'padding-bottom:\s*8[0-9]px;', 'padding-bottom: 24px;', html_str)
    return html_str

for item in subfolders:
    folder_path = os.path.join(ers_dir, item["dir"])
    catalog_file = os.path.join(folder_path, "home-mobile.html")
    nav_file = os.path.join(folder_path, "home-mobile-nav.html")

    if os.path.exists(catalog_file):
        with open(catalog_file, "r", encoding="utf-8") as f:
            c_content = f.read()

        # 1. Strip ALL navbars from Catalog Mode
        c_clean = clean_navbars_from_html(c_content)
        # Ensure back button points to ../home-mobile.html
        c_clean = re.sub(r'href="[^"]*home-mobile[^"]*"', 'href="../home-mobile.html"', c_clean)
        
        with open(catalog_file, "w", encoding="utf-8") as f:
            f.write(c_clean)
        print(f"Cleaned Catalog Mode (No Navbar): {catalog_file}")

        # 2. Build Clean 5-Navbar Mode
        n_clean = clean_navbars_from_html(c_content)
        # Ensure back button points to ../home-mobile-nav.html
        n_clean = re.sub(r'href="[^"]*home-mobile[^"]*"', 'href="../home-mobile-nav.html"', n_clean)
        # Inject Navbar CSS before </style>
        n_clean = n_clean.replace("</style>", f"{navbar_css_template}\n    </style>")
        # Adjust app-body padding
        n_clean = re.sub(r'padding-bottom:\s*2[0-9]px;', 'padding-bottom: 80px;', n_clean)
        
        # Inject Navbar HTML before the end of .mobile-container
        nav_html = make_navbar_html(item["active_tab"])
        if "<script" in n_clean:
            parts = n_clean.split("<script", 1)
            last_div = parts[0].rfind("</div>")
            if last_div != -1:
                n_clean = parts[0][:last_div] + nav_html + "\n    </div>\n<script" + parts[1]
            else:
                n_clean = parts[0] + nav_html + "<script" + parts[1]
        else:
            n_clean = n_clean.replace("</body>", f"{nav_html}\n</body>")

        with open(nav_file, "w", encoding="utf-8") as f:
            f.write(n_clean)
        print(f"Generated 5-Navbar Mode (With Navbar): {nav_file}")

print("Successfully cleaned catalog mode and configured 5-navbar mode!")
