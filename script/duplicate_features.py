import os
import re

ers_dir = r"c:\KERJAAN\Project\hifi-transmisi\hifi-mobile\ers"

subfolders = [
    {
        "dir": "Pemasangan",
        "title_keyword": "Pemasangan",
        "active_tab": 2
    },
    {
        "dir": "Pembongkaran",
        "title_keyword": "Pembongkaran",
        "active_tab": 3
    },
    {
        "dir": "Karantina & Pengembalian",
        "title_keyword": "Karantina",
        "active_tab": 4
    },
    {
        "dir": "Stock Opname",
        "title_keyword": "Stock Opname",
        "active_tab": 5
    }
]

navbar_css = """
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

for item in subfolders:
    src_file = os.path.join(ers_dir, item["dir"], "home-mobile.html")
    nav_file = os.path.join(ers_dir, item["dir"], "home-mobile-nav.html")

    if not os.path.exists(src_file):
        print(f"Warning: {src_file} does not exist")
        continue

    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update src_file (Catalog Version):
    # Ensure back button links to ../home-mobile.html
    # Remove any stray bottom-nav-5tabs if exists
    catalog_content = content
    # Replace back button target with ../home-mobile.html
    catalog_content = re.sub(r'href="[^"]*home-mobile[^"]*"', 'href="../home-mobile.html"', catalog_content)
    with open(src_file, "w", encoding="utf-8") as f:
        f.write(catalog_content)
    print(f"Updated Catalog Version: {src_file}")

    # 2. Create nav_file (Navbar Version):
    nav_content = content
    # Replace back button target with ../home-mobile-nav.html
    nav_content = re.sub(r'href="[^"]*home-mobile[^"]*"', 'href="../home-mobile-nav.html"', nav_content)

    # Inject navbar CSS before </style>
    if "</style>" in nav_content:
        nav_content = nav_content.replace("</style>", f"{navbar_css}\n    </style>")

    # Adjust app-body padding if needed
    if ".app-body" in nav_content:
        nav_content = nav_content.replace("padding-bottom: 28px;", "padding-bottom: 80px;")
        nav_content = nav_content.replace("padding-bottom: 24px;", "padding-bottom: 80px;")

    # Inject navbar HTML before </div>\n\n    <!-- Detail
    # or before </div>\n</body>
    nav_bar_snippet = make_navbar_html(item["active_tab"])
    
    # Place inside .mobile-container before closing </div>
    # Find the last closing </div> of .mobile-container
    if "<script" in nav_content:
        # Insert before <script
        parts = nav_content.split("<script", 1)
        # Find last </div> in parts[0]
        last_div_idx = parts[0].rfind("</div>")
        if last_div_idx != -1:
            updated_part0 = parts[0][:last_div_idx] + nav_bar_snippet + "\n    </div>\n"
            nav_content = updated_part0 + "<script" + parts[1]
        else:
            nav_content = parts[0] + nav_bar_snippet + "<script" + parts[1]
    else:
        nav_content = nav_content.replace("</body>", f"{nav_bar_snippet}\n</body>")

    with open(nav_file, "w", encoding="utf-8") as f:
        f.write(nav_content)
    print(f"Created 5-Navbar Version: {nav_file}")

print("All dual feature versions created successfully!")
