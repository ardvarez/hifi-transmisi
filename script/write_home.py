import os

html_code = """<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Dashboard ERS (Tower Emergency) - Mobile</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <!-- Leaflet Map CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --bg-canvas: #f8fafc;
            --card-bg: #ffffff;
            --primary-blue: #0A58CA;
            --primary-blue-light: #eff6ff;
            --primary-blue-hover: #084298;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --input-bg: #f1f5f9;
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 18px;
            --radius-xl: 22px;
            --shadow-subtle: 0 2px 10px rgba(0, 0, 0, 0.03);
            --shadow-card: 0 4px 16px rgba(0, 0, 0, 0.04);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: #cbd5e1;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 10px 0;
        }

        .mobile-container {
            width: 100%;
            max-width: 420px;
            height: 100vh;
            background-color: var(--bg-canvas);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 25px 60px rgba(15, 23, 42, 0.25);
            animation: pageFadeIn 0.25s ease-out;
        }

        @keyframes pageFadeIn {
            from { opacity: 0.95; transform: scale(0.99); }
            to { opacity: 1; transform: scale(1); }
        }

        @media (min-width: 440px) {
            .mobile-container {
                height: 890px;
                max-height: 95vh;
                border-radius: 38px;
                border: 8px solid #1e293b;
            }
        }

        /* 1. iOS Status Bar (Clean White) */
        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 20px 6px;
            color: var(--text-dark);
            font-size: 13px;
            font-weight: 700;
            background-color: #ffffff;
            z-index: 20;
        }

        .status-icons {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
        }

        /* 2. Top Header (Clean White Theme) */
        .header-section {
            background: #ffffff;
            padding: 10px 16px 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            z-index: 20;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .back-nav-btn {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: #f1f5f9;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-dark);
            text-decoration: none;
            font-size: 13px;
            transition: all 0.2s;
            flex-shrink: 0;
            border: 1px solid var(--border-color);
        }

        .back-nav-btn:hover {
            background: #e2e8f0;
            color: var(--primary-blue);
        }

        .header-titles {
            display: flex;
            flex-direction: column;
        }

        .header-badge-tag {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 10px;
            font-weight: 700;
            color: #0284c7;
            text-transform: uppercase;
            letter-spacing: 0.3px;
            margin-bottom: 1px;
        }

        .main-title {
            font-size: 16.5px;
            font-weight: 800;
            color: var(--text-dark);
            letter-spacing: -0.3px;
            line-height: 1.2;
        }

        .sub-title {
            font-size: 11.5px;
            font-weight: 600;
            color: var(--text-muted);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header-icon-btn {
            width: 36px;
            height: 36px;
            border-radius: 11px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-dark);
            font-size: 13px;
            position: relative;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
            text-decoration: none;
            transition: all 0.2s;
        }

        .header-icon-btn:hover {
            border-color: var(--primary-blue);
            color: var(--primary-blue);
        }

        .header-icon-btn.filter-active {
            background: var(--primary-blue);
            color: #ffffff;
            border-color: var(--primary-blue);
        }

        /* App Body Scroll Container */
        .app-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 14px;
            overflow-y: auto;
            position: relative;
            background-color: var(--bg-canvas);
            padding-bottom: 85px;
            scrollbar-width: none;
            gap: 16px;
        }

        .app-body::-webkit-scrollbar {
            display: none;
        }

        /* ==================== 3. KATALOG FITUR ERS (CLEAN WHITE 2X2 CARDS) ==================== */
        .catalog-container-card {
            background: #ffffff;
            border-radius: var(--radius-xl);
            padding: 15px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .catalog-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .catalog-title {
            font-size: 14px;
            font-weight: 800;
            color: var(--text-dark);
            display: flex;
            align-items: center;
            gap: 7px;
        }

        .catalog-title i {
            color: var(--primary-blue);
            font-size: 15px;
        }

        .catalog-view-all {
            background: var(--primary-blue-light);
            color: var(--primary-blue);
            font-size: 11px;
            font-weight: 800;
            padding: 3px 9px;
            border-radius: 20px;
            cursor: pointer;
            border: 1px solid rgba(10, 88, 202, 0.18);
        }

        .catalog-grid-box {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .catalog-item-card {
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 12px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-decoration: none;
            color: var(--text-dark);
            min-height: 102px;
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .catalog-item-card:active {
            transform: translateY(-2px);
            background: #ffffff;
            border-color: var(--primary-blue);
            box-shadow: 0 4px 14px rgba(10, 88, 202, 0.1);
        }

        .item-card-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 6px;
        }

        .item-icon-bubble {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
        }

        .item-icon-bubble.pemasangan { background: #eff6ff; color: #2563eb; }
        .item-icon-bubble.bongkar { background: #fef2f2; color: #dc2626; }
        .item-icon-bubble.karantina { background: #f0fdf4; color: #16a34a; }
        .item-icon-bubble.stock { background: #fefce8; color: #ca8a04; }

        .item-arrow-icon {
            font-size: 11px;
            color: #94a3b8;
            margin-top: 2px;
        }

        .item-title {
            font-size: 12px;
            font-weight: 800;
            color: var(--text-dark);
            line-height: 1.25;
        }

        .item-sub {
            font-size: 10.5px;
            color: var(--text-muted);
            font-weight: 500;
            margin-top: 2px;
            line-height: 1.3;
        }

        /* Section Headings */
        .section-header-block {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .section-title {
            font-size: 14px;
            font-weight: 800;
            color: var(--text-dark);
            letter-spacing: -0.2px;
        }

        .section-subtitle {
            font-size: 11.5px;
            color: var(--text-muted);
        }

        /* ==================== 4. KPI CARDS GRID (3 CLEAN WHITE CARDS) ==================== */
        .kpi-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .kpi-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            padding: 14px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-subtle);
            border: 1px solid var(--border-color);
            position: relative;
            cursor: pointer;
            transition: transform 0.15s, box-shadow 0.15s;
        }

        .kpi-card:active {
            transform: scale(0.985);
            border-color: var(--primary-blue);
        }

        .kpi-card-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .kpi-icon-bubble {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 17px;
            flex-shrink: 0;
        }

        .kpi-icon-bubble.blue {
            background: rgba(10, 88, 202, 0.08);
            color: #0A58CA;
            border: 1px solid rgba(10, 88, 202, 0.15);
        }

        .kpi-icon-bubble.green {
            background: rgba(16, 185, 129, 0.08);
            color: #059669;
            border: 1px solid rgba(16, 185, 129, 0.15);
        }

        .kpi-icon-bubble.red {
            background: rgba(239, 68, 68, 0.08);
            color: #dc2626;
            border: 1px solid rgba(239, 68, 68, 0.15);
        }

        .kpi-info {
            display: flex;
            flex-direction: column;
        }

        .kpi-label {
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
            line-height: 1.2;
        }

        .kpi-subtext {
            font-size: 12.5px;
            font-weight: 800;
            color: var(--text-dark);
            margin-top: 1px;
        }

        .kpi-card-right {
            text-align: right;
        }

        .kpi-value {
            font-family: 'Outfit', sans-serif;
            font-size: 26px;
            font-weight: 800;
            color: var(--text-dark);
            line-height: 1;
            letter-spacing: -0.5px;
        }

        .kpi-arrow-icon {
            font-size: 11px;
            color: #94a3b8;
            margin-bottom: 3px;
        }

        /* ==================== 5. MAP CONTAINER ==================== */
        .map-card-wrapper {
            background: #ffffff;
            border-radius: var(--radius-xl);
            padding: 15px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .map-controls-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .map-tab-group {
            display: flex;
            background: #f1f5f9;
            padding: 3px;
            border-radius: 11px;
            gap: 3px;
        }

        .map-tab-btn {
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 11.5px;
            font-weight: 700;
            border: none;
            cursor: pointer;
            background: transparent;
            color: var(--text-muted);
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .map-tab-btn.active {
            background: #ffffff;
            color: var(--primary-blue);
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        }

        .map-action-btn {
            padding: 5px 10px;
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 9px;
            font-size: 11px;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .map-view-box {
            width: 100%;
            height: 230px;
            border-radius: var(--radius-md);
            overflow: hidden;
            border: 1px solid #cbd5e1;
            position: relative;
            background-color: #d0e4f2;
        }

        #indonesiaMap {
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        .map-legend-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 6px 10px;
            background: #f8fafc;
            border-radius: 10px;
            font-size: 11px;
            color: var(--text-muted);
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
        }

        .legend-badge {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #0A58CA;
            box-shadow: 0 0 0 2px rgba(10, 88, 202, 0.2);
        }

        /* ==================== 6. CHARTS CONTAINERS ==================== */
        .chart-card-wrapper {
            background: #ffffff;
            border-radius: var(--radius-xl);
            padding: 16px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .chart-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chart-title {
            font-size: 13.5px;
            font-weight: 800;
            color: var(--text-dark);
            letter-spacing: -0.2px;
        }

        .chart-canvas-container {
            position: relative;
            width: 100%;
            height: 220px;
        }

        .donut-chart-container {
            position: relative;
            width: 100%;
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .donut-center-label {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            pointer-events: none;
        }

        .donut-center-val {
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 800;
            color: var(--text-dark);
            line-height: 1;
        }

        .donut-center-sub {
            font-size: 10px;
            color: var(--text-muted);
            font-weight: 600;
            margin-top: 2px;
        }

        /* ==================== 7. DETAIL ERS LIST ==================== */
        .detail-section-card {
            background: #ffffff;
            border-radius: var(--radius-xl);
            padding: 16px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .search-and-filter-box {
            display: flex;
            gap: 8px;
            align-items: center;
        }

        .search-input-field {
            flex: 1;
            background: var(--input-bg);
            border-radius: 12px;
            padding: 9px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid transparent;
            transition: all 0.2s;
        }

        .search-input-field:focus-within {
            border-color: var(--primary-blue);
            background: #ffffff;
            box-shadow: 0 0 0 3px rgba(10, 88, 202, 0.1);
        }

        .search-input-field input {
            border: none;
            outline: none;
            background: transparent;
            width: 100%;
            font-size: 12.5px;
            color: var(--text-dark);
            font-weight: 600;
        }

        .search-input-field input::placeholder {
            color: #94a3b8;
            font-weight: 500;
        }

        .search-input-field i {
            color: #94a3b8;
            font-size: 13px;
        }

        .btn-filter-icon {
            height: 40px;
            padding: 0 12px;
            border-radius: 12px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            gap: 6px;
            color: var(--primary-blue);
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            flex-shrink: 0;
        }

        .detail-item-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .detail-data-card {
            background: #f8fafc;
            border-radius: 14px;
            padding: 12px 14px;
            border: 1px solid var(--border-color);
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
            transition: border-color 0.2s, transform 0.1s;
        }

        .detail-data-card:active {
            transform: scale(0.99);
            background: #ffffff;
            border-color: var(--primary-blue);
        }

        .detail-card-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
            padding-bottom: 8px;
            border-bottom: 1px dashed var(--border-color);
        }

        .detail-unit-badge {
            font-size: 11.5px;
            font-weight: 800;
            color: var(--primary-blue);
            background: #ffffff;
            padding: 3px 8px;
            border-radius: 8px;
            border: 1px solid rgba(10, 88, 202, 0.15);
        }

        .detail-pelaksana-tag {
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
        }

        .detail-grid-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 6px;
        }

        .detail-grid-cell {
            display: flex;
            flex-direction: column;
        }

        .cell-label {
            font-size: 10px;
            font-weight: 600;
            color: #94a3b8;
            text-transform: uppercase;
        }

        .cell-value {
            font-size: 12px;
            font-weight: 700;
            color: var(--text-dark);
            margin-top: 1px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .tag-merk {
            display: inline-block;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #334155;
            font-size: 10.5px;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 6px;
            width: fit-content;
        }

        .detail-bottom-info {
            background: #ffffff;
            padding: 8px 10px;
            border-radius: 8px;
            font-size: 11px;
            color: #475569;
            margin-top: 4px;
            border-left: 3px solid var(--primary-blue);
            border: 1px solid var(--border-color);
            border-left-width: 3px;
        }

        .pagination-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 10px;
            border-top: 1px solid var(--border-color);
            font-size: 11.5px;
            color: var(--text-muted);
        }

        .pagination-pages {
            display: flex;
            gap: 4px;
            align-items: center;
        }

        .page-num-btn {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: #ffffff;
            color: var(--text-dark);
            font-size: 11px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .page-num-btn.active {
            background: var(--primary-blue);
            color: #ffffff;
            border-color: var(--primary-blue);
        }

        /* ==================== 8. CLEAN BOTTOM NAVBAR ==================== */
        .bottom-nav {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 68px;
            background: #ffffff;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 0 4px 10px;
            z-index: 100;
            box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.04);
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: 700;
            color: #94a3b8;
            cursor: pointer;
            gap: 4px;
            text-decoration: none;
            width: 24%;
            transition: color 0.2s;
            position: relative;
        }

        .nav-item.active {
            color: var(--primary-blue);
        }

        .nav-item i {
            font-size: 19px;
        }

        .nav-catalog-bubble {
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #0A58CA, #0284c7);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 18px;
            box-shadow: 0 4px 14px rgba(10, 88, 202, 0.35);
            margin-top: -18px;
            border: 3px solid #ffffff;
            transition: transform 0.2s;
        }

        .nav-catalog-bubble:active {
            transform: scale(0.92);
        }

        .ios-bar {
            position: absolute;
            bottom: 5px;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 4px;
            background: #0f172a;
            border-radius: 2px;
            z-index: 101;
        }

        /* Full Drawer Modals */
        .modal-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.55);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            z-index: 999;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .modal-drawer {
            width: 100%;
            max-width: 420px;
            background: #ffffff;
            border-top-left-radius: 26px;
            border-top-right-radius: 26px;
            padding: 18px 20px 24px;
            box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.2);
            transform: translateY(100%);
            transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
            max-height: 86vh;
            overflow-y: auto;
            scrollbar-width: none;
        }

        .modal-overlay.active .modal-drawer {
            transform: translateY(0);
        }

        .drawer-handle {
            width: 40px;
            height: 4px;
            background: #cbd5e1;
            border-radius: 2px;
            margin: 0 auto 14px;
            cursor: pointer;
        }

        .catalog-sheet-card {
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 14px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
            text-decoration: none;
            color: var(--text-dark);
            transition: all 0.2s;
        }

        .catalog-sheet-card:active {
            background: var(--primary-blue-light);
            border-color: var(--primary-blue);
        }

        .catalog-sheet-icon {
            width: 44px;
            height: 44px;
            border-radius: 13px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 19px;
            flex-shrink: 0;
        }

        .filter-drawer-title {
            font-size: 17px;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .filter-reset-link {
            font-size: 12px;
            color: var(--primary-blue);
            font-weight: 600;
            cursor: pointer;
        }

        .filter-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 12px;
        }

        .filter-label {
            font-size: 12px;
            font-weight: 700;
            color: #334155;
        }

        .filter-select {
            width: 100%;
            height: 44px;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 0 14px;
            font-size: 13px;
            color: var(--text-dark);
            background: #ffffff;
            outline: none;
        }

        .btn-apply-filter {
            width: 100%;
            height: 46px;
            background: var(--primary-blue);
            color: #ffffff;
            border: none;
            border-radius: 14px;
            font-size: 14.5px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 10px;
            box-shadow: 0 4px 12px rgba(10, 88, 202, 0.3);
        }

        /* Marker Pin */
        .ers-marker-pin {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #0A58CA;
            border: 2.5px solid #ffffff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 12px;
        }

        .ers-marker-pin.tower { background: #059669; }
    </style>
</head>

<body>

    <div class="mobile-container">
        <!-- iOS Status Bar (Clean White) -->
        <div class="status-bar">
            <span>9:41 AM</span>
            <div class="status-icons">
                <i class="fa-solid fa-signal"></i>
                <i class="fa-solid fa-wifi"></i>
                <i class="fa-solid fa-battery-full"></i>
            </div>
        </div>

        <!-- Top Header (Clean White Concept) -->
        <div class="header-section">
            <div class="header-left">
                <a href="../../catalog-mobile.html" class="back-nav-btn" title="Kembali ke Catalog Master">
                    <i class="fa-solid fa-chevron-left"></i>
                </a>
                <div class="header-titles">
                    <span class="header-badge-tag"><i class="fa-solid fa-bolt"></i> Server Development</span>
                    <h1 class="main-title">Dashboard ERS</h1>
                    <span class="sub-title">Ketersediaan & Pemasangan ERS</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="header-icon-btn" onclick="openFilterModal()" id="btnFilterTrigger" title="Filter Wilayah & Data">
                    <i class="fa-solid fa-sliders"></i>
                </button>
                <a href="../../power-inspect/notifikasi-mobile.html" class="header-icon-btn" title="Notifikasi">
                    <i class="fa-regular fa-bell"></i>
                </a>
            </div>
        </div>

        <!-- App Body / Content Area -->
        <div class="app-body">
            
            <!-- 1. KATALOG FITUR ERS (CLEAN 2X2 GRID CARDS) -->
            <div class="catalog-container-card" id="catalogSection">
                <div class="catalog-header-row">
                    <div class="catalog-title">
                        <i class="fa-solid fa-boxes-packing"></i>
                        <span>Katalog Fitur ERS</span>
                    </div>
                    <span class="catalog-view-all" onclick="openCatalogModal()">
                        4 Modul <i class="fa-solid fa-chevron-right" style="font-size: 9px; margin-left: 2px;"></i>
                    </span>
                </div>

                <div class="catalog-grid-box">
                    <!-- Fitur 1: Pemasangan ERS -->
                    <a href="Pemasangan/home-mobile.html" class="catalog-item-card">
                        <div class="item-card-top">
                            <div class="item-icon-bubble pemasangan">
                                <i class="fa-solid fa-wrench"></i>
                            </div>
                            <i class="fa-solid fa-arrow-up-right-from-square item-arrow-icon"></i>
                        </div>
                        <div>
                            <div class="item-title">Pemasangan ERS</div>
                            <div class="item-sub">Instalasi & Ereksi Tower</div>
                        </div>
                    </a>

                    <!-- Fitur 2: Pembongkaran ERS -->
                    <a href="Pembongkaran/home-mobile.html" class="catalog-item-card">
                        <div class="item-card-top">
                            <div class="item-icon-bubble bongkar">
                                <i class="fa-solid fa-truck-ramp-box"></i>
                            </div>
                            <i class="fa-solid fa-arrow-up-right-from-square item-arrow-icon"></i>
                        </div>
                        <div>
                            <div class="item-title">Pembongkaran ERS</div>
                            <div class="item-sub">Dismantling & Rekondisi</div>
                        </div>
                    </a>

                    <!-- Fitur 3: Karantina & Pengembalian -->
                    <a href="Karantina & Pengembalian/home-mobile.html" class="catalog-item-card">
                        <div class="item-card-top">
                            <div class="item-icon-bubble karantina">
                                <i class="fa-solid fa-box-archive"></i>
                            </div>
                            <i class="fa-solid fa-arrow-up-right-from-square item-arrow-icon"></i>
                        </div>
                        <div>
                            <div class="item-title">Karantina & Return</div>
                            <div class="item-sub">Isolasi & Balik Gudang</div>
                        </div>
                    </a>

                    <!-- Fitur 4: Stock Opname -->
                    <a href="Stock Opname/home-mobile.html" class="catalog-item-card">
                        <div class="item-card-top">
                            <div class="item-icon-bubble stock">
                                <i class="fa-solid fa-boxes-stacked"></i>
                            </div>
                            <i class="fa-solid fa-arrow-up-right-from-square item-arrow-icon"></i>
                        </div>
                        <div>
                            <div class="item-title">Stock Opname</div>
                            <div class="item-sub">Audit Fisik & Berita Acara</div>
                        </div>
                    </a>
                </div>
            </div>

            <!-- 2. SECTION HEADER: DATA KETERSEDIAAN -->
            <div class="section-header-block">
                <h2 class="section-title">Data Ketersediaan & Pemasangan</h2>
                <p class="section-subtitle">Menampilkan jumlah ERS berdasarkan ketersediaan dan pemasangan</p>
            </div>

            <!-- 3. KPI CARDS GRID (3 FULL-WIDTH CARDS MATCHING REFERENCE) -->
            <div class="kpi-container">
                <!-- Card 1: Total ERS Terpasang -->
                <div class="kpi-card" onclick="scrollToDetail()">
                    <div class="kpi-card-left">
                        <div class="kpi-icon-bubble blue">
                            <i class="fa-solid fa-tower-broadcast"></i>
                        </div>
                        <div class="kpi-info">
                            <span class="kpi-label">Total ERS</span>
                            <span class="kpi-subtext">Terpasang (Set)</span>
                        </div>
                    </div>
                    <div class="kpi-card-right">
                        <i class="fa-solid fa-arrow-right kpi-arrow-icon"></i>
                        <div class="kpi-value" id="kpiTerpasangVal">35</div>
                    </div>
                </div>

                <!-- Card 2: Total ERS Set ERS Lengkap -->
                <div class="kpi-card" onclick="filterByStatus('Lengkap')">
                    <div class="kpi-card-left">
                        <div class="kpi-icon-bubble green">
                            <i class="fa-solid fa-circle-check"></i>
                        </div>
                        <div class="kpi-info">
                            <span class="kpi-label">Total ERS</span>
                            <span class="kpi-subtext">Set ERS Lengkap</span>
                        </div>
                    </div>
                    <div class="kpi-card-right">
                        <i class="fa-solid fa-arrow-right kpi-arrow-icon"></i>
                        <div class="kpi-value" id="kpiLengkapVal" style="color: #059669;">39</div>
                    </div>
                </div>

                <!-- Card 3: Total ERS Set ERS Tidak Lengkap -->
                <div class="kpi-card" onclick="filterByStatus('Tidak Lengkap')">
                    <div class="kpi-card-left">
                        <div class="kpi-icon-bubble red">
                            <i class="fa-solid fa-triangle-exclamation"></i>
                        </div>
                        <div class="kpi-info">
                            <span class="kpi-label">Total ERS</span>
                            <span class="kpi-subtext">Set ERS Tidak Lengkap</span>
                        </div>
                    </div>
                    <div class="kpi-card-right">
                        <i class="fa-solid fa-arrow-right kpi-arrow-icon"></i>
                        <div class="kpi-value" id="kpiTidakLengkapVal" style="color: #dc2626;">2945</div>
                    </div>
                </div>
            </div>

            <!-- 4. MAP CARD WRAPPER -->
            <div class="map-card-wrapper" id="mapSection">
                <div class="map-controls-row">
                    <div class="map-tab-group">
                        <button class="map-tab-btn active" id="tabSetERS" onclick="switchMapMode('set')">
                            <i class="fa-solid fa-layer-group"></i> Set ERS
                        </button>
                        <button class="map-tab-btn" id="tabTowerOperasi" onclick="switchMapMode('tower')">
                            <i class="fa-solid fa-tower-observation"></i> Tower Operasi
                        </button>
                    </div>
                    <button class="map-action-btn" onclick="resetMapZoom()" title="Reset Tampilan Peta">
                        <i class="fa-solid fa-up-right-and-down-left-from-center"></i> Detail
                    </button>
                </div>

                <!-- Leaflet Map Container -->
                <div class="map-view-box">
                    <div id="indonesiaMap"></div>
                </div>

                <!-- Map Legend -->
                <div class="map-legend-box">
                    <div class="legend-item">
                        <div class="legend-badge"></div>
                        <span>Titik Sebaran Unit Induk</span>
                    </div>
                    <span style="font-weight: 700; color: #0A58CA;" id="mapMarkerCountText">14 Titik Aktif</span>
                </div>
            </div>

            <!-- 5. CHART 1: ERS OPERASI PER UNIT -->
            <div class="chart-card-wrapper">
                <div class="chart-card-header">
                    <h3 class="chart-title">ERS Operasi Per Unit</h3>
                    <i class="fa-solid fa-chart-simple" style="color: #94a3b8; font-size: 13px;"></i>
                </div>
                <div class="chart-canvas-container">
                    <canvas id="chartOperasiUnit"></canvas>
                </div>
            </div>

            <!-- 6. CHART 2: SET ERS LENGKAP & TIDAK LENGKAP -->
            <div class="chart-card-wrapper">
                <div class="chart-card-header">
                    <h3 class="chart-title">Set ERS Lengkap & Tidak Lengkap</h3>
                    <i class="fa-solid fa-chart-column" style="color: #94a3b8; font-size: 13px;"></i>
                </div>
                <div class="chart-canvas-container">
                    <canvas id="chartLengkapStatus"></canvas>
                </div>
            </div>

            <!-- 7. CHART 3: DURASI ERS OPERASI (DONUT) -->
            <div class="chart-card-wrapper">
                <div class="chart-card-header">
                    <h3 class="chart-title">Durasi ERS Operasi</h3>
                    <i class="fa-solid fa-chart-pie" style="color: #94a3b8; font-size: 13px;"></i>
                </div>
                <div class="donut-chart-container">
                    <canvas id="chartDurasiOperasi"></canvas>
                    <div class="donut-center-label">
                        <div class="donut-center-val">27</div>
                        <div class="donut-center-sub">Total Data</div>
                    </div>
                </div>
            </div>

            <!-- 8. DETAIL ERS TABLE/CARDS -->
            <div class="detail-section-card" id="detailSection">
                <div class="section-header-block">
                    <h2 class="section-title">Detail ERS</h2>
                    <p class="section-subtitle">Daftar lokasi & status operasional ERS terpasang</p>
                </div>

                <!-- Search & Filter Bar -->
                <div class="search-and-filter-box">
                    <div class="search-input-field">
                        <input type="text" id="searchInput" placeholder="Cari unit, penghantar, merk..." oninput="handleSearch(this.value)">
                        <i class="fa-solid fa-magnifying-glass"></i>
                    </div>
                    <button class="btn-filter-icon" onclick="openFilterModal()">
                        <i class="fa-solid fa-filter"></i> Filter
                    </button>
                </div>

                <!-- Dynamic Data List -->
                <div class="detail-item-list" id="detailDataList">
                    <!-- Populated dynamically by JS -->
                </div>

                <!-- Pagination Component -->
                <div class="pagination-container">
                    <span id="paginationInfo">Menampilkan 5 dari 44 Data</span>
                    <div class="pagination-pages" id="paginationControls"></div>
                </div>
            </div>

        </div>

        <!-- 9. BOTTOM NAVBAR WITH BUBBLE CATALOG -->
        <nav class="bottom-nav">
            <!-- Tab 1: Dashboard Home -->
            <a href="home-mobile.html" class="nav-item active" title="Dashboard Root">
                <i class="fa-solid fa-chart-pie"></i>
                <span>Dashboard</span>
            </a>

            <!-- Tab 2: Peta Sebaran -->
            <a href="#mapSection" class="nav-item" onclick="scrollToMap(event)" title="Peta Sebaran">
                <i class="fa-solid fa-map-location-dot"></i>
                <span>Peta Sebaran</span>
            </a>

            <!-- Tab 3: Center Highlighted Catalog Action -->
            <div class="nav-item" onclick="openCatalogModal()" title="Katalog Fitur ERS">
                <div class="nav-catalog-bubble">
                    <i class="fa-solid fa-boxes-packing"></i>
                </div>
                <span style="color: var(--primary-blue); font-weight: 800; margin-top: 2px;">Katalog ERS</span>
            </div>

            <!-- Tab 4: Notifikasi -->
            <a href="../../power-inspect/notifikasi-mobile.html" class="nav-item" title="Notifikasi">
                <i class="fa-regular fa-bell"></i>
                <span>Notifikasi</span>
            </a>
        </nav>

        <!-- iOS Bottom Indicator Line -->
        <div class="ios-bar"></div>

        <!-- KATALOG DRAWER MODAL -->
        <div class="modal-overlay" id="catalogModal" onclick="closeCatalogModal(event)">
            <div class="modal-drawer" onclick="event.stopPropagation()">
                <div class="drawer-handle" onclick="closeCatalogModalDirect()"></div>
                
                <div class="filter-drawer-title">
                    <span><i class="fa-solid fa-boxes-packing" style="color: var(--primary-blue); margin-right: 6px;"></i>Katalog Fitur ERS</span>
                    <span class="filter-reset-link" onclick="closeCatalogModalDirect()">Tutup</span>
                </div>

                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px; line-height: 1.4;">
                    Pilih modul operasional ERS (Emergency Restoration System) di bawah ini:
                </p>

                <!-- Fitur 1: Pemasangan ERS -->
                <a href="Pemasangan/home-mobile.html" class="catalog-sheet-card">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div class="catalog-sheet-icon" style="background: #eff6ff; color: #2563eb;">
                            <i class="fa-solid fa-wrench"></i>
                        </div>
                        <div>
                            <div style="font-size: 13.5px; font-weight: 800; color: var(--text-dark);">Pemasangan ERS</div>
                            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Instalasi tower darurat, permit & erection.</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #94a3b8; font-size: 12px;"></i>
                </a>

                <!-- Fitur 2: Pembongkaran ERS -->
                <a href="Pembongkaran/home-mobile.html" class="catalog-sheet-card">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div class="catalog-sheet-icon" style="background: #fef2f2; color: #dc2626;">
                            <i class="fa-solid fa-truck-ramp-box"></i>
                        </div>
                        <div>
                            <div style="font-size: 13.5px; font-weight: 800; color: var(--text-dark);">Pembongkaran ERS</div>
                            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Dismantling & rekondisi tapak tower.</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #94a3b8; font-size: 12px;"></i>
                </a>

                <!-- Fitur 3: Karantina & Pengembalian -->
                <a href="Karantina & Pengembalian/home-mobile.html" class="catalog-sheet-card">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div class="catalog-sheet-icon" style="background: #f0fdf4; color: #16a34a;">
                            <i class="fa-solid fa-box-archive"></i>
                        </div>
                        <div>
                            <div style="font-size: 13.5px; font-weight: 800; color: var(--text-dark);">Karantina & Return</div>
                            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Isolasi item rusak & serah terima gudang.</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #94a3b8; font-size: 12px;"></i>
                </a>

                <!-- Fitur 4: Stock Opname -->
                <a href="Stock Opname/home-mobile.html" class="catalog-sheet-card">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div class="catalog-sheet-icon" style="background: #fefce8; color: #ca8a04;">
                            <i class="fa-solid fa-boxes-stacked"></i>
                        </div>
                        <div>
                            <div style="font-size: 13.5px; font-weight: 800; color: var(--text-dark);">Stock Opname ERS</div>
                            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Audit fisik berkala & berita acara stok.</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #94a3b8; font-size: 12px;"></i>
                </a>
            </div>
        </div>

        <!-- FILTER DRAWER MODAL -->
        <div class="modal-overlay" id="filterModal" onclick="closeFilterModal(event)">
            <div class="modal-drawer" onclick="event.stopPropagation()">
                <div class="drawer-handle" onclick="closeFilterModalDirect()"></div>
                
                <div class="filter-drawer-title">
                    <span>Filter Data ERS</span>
                    <span class="filter-reset-link" onclick="resetFilters()">Reset</span>
                </div>

                <div class="filter-group">
                    <label class="filter-label">Kantor Pusat</label>
                    <select class="filter-select" id="filterKantorPusat">
                        <option value="ALL">Semua Kantor Pusat</option>
                        <option value="PLN_PUSAT" selected>PT PLN (Persero) Kantor Pusat</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label class="filter-label">Unit Induk (UIT / UIW)</label>
                    <select class="filter-select" id="filterUnitInduk">
                        <option value="ALL">Semua Unit Induk</option>
                        <option value="NTB">NTB (UIW NTB)</option>
                        <option value="P3BS">P3BS (UIP3B Sumatera)</option>
                        <option value="UITJBM">UITJBM (UIT Jawa Bagian Madura)</option>
                        <option value="UITJBT">UITJBT (UIT Jawa Bagian Tengah)</option>
                        <option value="UITJBB">UITJBB (UIT Jawa Bagian Barat)</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label class="filter-label">Status Kelengkapan</label>
                    <select class="filter-select" id="filterStatusSet">
                        <option value="ALL">Semua Status</option>
                        <option value="Lengkap">Set ERS Lengkap</option>
                        <option value="Tidak Lengkap">Set ERS Tidak Lengkap</option>
                    </select>
                </div>

                <button class="btn-apply-filter" onclick="applyFilterDrawer()">Terapkan Filter</button>
            </div>
        </div>
    </div>

    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

    <script>
        const ersMasterData = [
            {
                no: 1,
                unitInduk: 'NTB',
                unitPelaksana: 'UPT MATARAM',
                penghantar: 'SUTT 70 KV WOHA-DOMPU',
                tower: 'T.42',
                lat: -8.580437,
                lng: 118.627106,
                jumlahSet: 2,
                merk: 'SBB',
                penyebab: 'Longsor akibat pergerakan tanah',
                tanggal: '24 Oktober 2023',
                statusSet: 'Lengkap'
            },
            {
                no: 2,
                unitInduk: 'NTB',
                unitPelaksana: 'UPT TANJUNG KARANG',
                penghantar: 'SUTT 150 kV Pagelaran - ULUBELU',
                tower: 'T.118',
                lat: -5.3139244,
                lng: 104.76185,
                jumlahSet: 1,
                merk: 'LINDSEY',
                penyebab: 'Tanah Longsor lereng bukit',
                tanggal: '07 Juni 2024',
                statusSet: 'Lengkap'
            },
            {
                no: 3,
                unitInduk: 'P3BS',
                unitPelaksana: 'UPT BANDA ACEH',
                penghantar: 'SUTT 150 kV Nagan - Sigli',
                tower: 'T.85',
                lat: 4.422167,
                lng: 96.189583,
                jumlahSet: 1,
                merk: 'SBB',
                penyebab: 'Pondasi tower amblas tergerus banjir',
                tanggal: '03 Desember 2023',
                statusSet: 'Tidak Lengkap'
            },
            {
                no: 4,
                unitInduk: 'UITJBM',
                unitPelaksana: 'UPT SURABAYA',
                penghantar: 'SUTT 150 kV Waru - Rungkut # 1-2',
                tower: 'T.12',
                lat: -7.34585831,
                lng: 112.7383091,
                jumlahSet: 2,
                merk: 'TOWER SOLUTION',
                penyebab: 'Tower Kritis dampak proyek jalan tol',
                tanggal: '01 Desember 2023',
                statusSet: 'Lengkap'
            },
            {
                no: 5,
                unitInduk: 'P3BS',
                unitPelaksana: 'UPT PEMATANG SIANTAR',
                penghantar: 'SUTET 275 kV Simangkuk - Sarulla',
                tower: 'T.204',
                lat: 1.93541493,
                lng: 99.02995866,
                jumlahSet: 2,
                merk: 'SBB',
                penyebab: 'Pending item UIP SBU proses drawing pondasi',
                tanggal: '19 Juni 2025',
                statusSet: 'Tidak Lengkap'
            }
        ];

        let filteredData = [...ersMasterData];
        let currentPage = 1;
        const itemsPerPage = 3;

        let map, markersLayer;

        function initMap() {
            map = L.map('indonesiaMap', {
                zoomControl: true,
                attributionControl: false
            }).setView([-2.548926, 118.0148634], 4.2);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18 }).addTo(map);
            markersLayer = L.layerGroup().addTo(map);
            renderMapMarkers('set');
        }

        function renderMapMarkers(mode = 'set') {
            markersLayer.clearLayers();
            ersMasterData.forEach(item => {
                const iconHtml = `<div class="ers-marker-pin ${mode === 'tower' ? 'tower' : ''}"><i class="fa-solid ${mode === 'tower' ? 'fa-tower-observation' : 'fa-truck'}"></i></div>`;
                const customIcon = L.divIcon({
                    html: iconHtml,
                    className: 'custom-leaflet-pin',
                    iconSize: [28, 28],
                    iconAnchor: [14, 28],
                    popupAnchor: [0, -28]
                });

                const marker = L.marker([item.lat, item.lng], { icon: customIcon });
                marker.bindPopup(`
                    <div style="font-family:'Plus Jakarta Sans',sans-serif;">
                        <strong style="color:#0A58CA;">${item.unitInduk} - ${item.unitPelaksana}</strong><br>
                        <span style="font-size:11px; color:#475569;">${item.penghantar} (${item.jumlahSet} Set)</span>
                    </div>
                `);
                markersLayer.addLayer(marker);
            });
            document.getElementById('mapMarkerCountText').innerText = `${ersMasterData.length} Titik ${mode === 'tower' ? 'Tower' : 'Set ERS'}`;
        }

        function switchMapMode(mode) {
            document.getElementById('tabSetERS').classList.toggle('active', mode === 'set');
            document.getElementById('tabTowerOperasi').classList.toggle('active', mode === 'tower');
            renderMapMarkers(mode);
        }

        function resetMapZoom() {
            if (map) {
                map.setView([-2.548926, 118.0148634], 4.2);
            }
        }

        function scrollToMap(e) {
            if (e) e.preventDefault();
            document.getElementById('mapSection').scrollIntoView({ behavior: 'smooth' });
        }

        function scrollToDetail() {
            document.getElementById('detailSection').scrollIntoView({ behavior: 'smooth' });
        }

        function initCharts() {
            const ctxOperasi = document.getElementById('chartOperasiUnit').getContext('2d');
            new Chart(ctxOperasi, {
                type: 'bar',
                data: {
                    labels: ['BABEL', 'MMU', 'NTB', 'P2B', 'P3BS', 'PLN BATAM', 'UIT JBB', 'UIT JBM', 'UIT JBT'],
                    datasets: [
                        { label: 'Terpasang', data: [0, 0, 4, 0, 18, 0, 1, 1, 3], backgroundColor: '#0A58CA', borderRadius: 4, barThickness: 6 },
                        { label: 'Selesai', data: [2, 0, 2, 3, 6, 0, 1, 1, 2], backgroundColor: '#00A2B9', borderRadius: 4, barThickness: 6 }
                    ]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } },
                    scales: { x: { grid: { color: '#f1f5f9' } }, y: { grid: { display: false } } }
                }
            });

            const ctxLengkap = document.getElementById('chartLengkapStatus').getContext('2d');
            new Chart(ctxLengkap, {
                type: 'bar',
                data: {
                    labels: ['P3B', 'PLN BATAM', 'NTB', 'P3BSUL', 'UIP KALBAGTIM', 'UIT JBB'],
                    datasets: [
                        { label: 'Lengkap', data: [0, 0, 2, 12, 5, 0], backgroundColor: '#0A58CA', borderRadius: 4, barThickness: 6 },
                        { label: 'Tidak Lengkap', data: [0, 0, 0, 15, 0, 0], backgroundColor: '#f59e0b', borderRadius: 4, barThickness: 6 }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } },
                    scales: { x: { grid: { display: false } }, y: { grid: { color: '#f1f5f9' } } }
                }
            });

            const ctxDurasi = document.getElementById('chartDurasiOperasi').getContext('2d');
            new Chart(ctxDurasi, {
                type: 'doughnut',
                data: {
                    labels: ['< 1 Tahun', '1 - 3 Tahun', '> 3 Tahun'],
                    datasets: [{ data: [4, 21, 2], backgroundColor: ['#0A58CA', '#f59e0b', '#ef4444'], borderWidth: 0 }]
                },
                options: { responsive: true, maintainAspectRatio: false, cutout: '72%', plugins: { legend: { position: 'bottom' } } }
            });
        }

        function renderDetailList() {
            const container = document.getElementById('detailDataList');
            const totalItems = filteredData.length;
            const startIdx = (currentPage - 1) * itemsPerPage;
            const pageItems = filteredData.slice(startIdx, startIdx + itemsPerPage);

            document.getElementById('paginationInfo').innerText = `Menampilkan ${Math.min(pageItems.length, itemsPerPage)} dari ${totalItems} Data`;

            if (pageItems.length === 0) {
                container.innerHTML = `<div style="text-align: center; padding: 20px; color: #94a3b8; font-size: 12px;">Tidak ada data yang cocok.</div>`;
                renderPaginationControls(0);
                return;
            }

            container.innerHTML = pageItems.map(item => `
                <div class="detail-data-card">
                    <div class="detail-card-top">
                        <span class="detail-unit-badge">${item.unitInduk}</span>
                        <span class="detail-pelaksana-tag">${item.unitPelaksana}</span>
                    </div>

                    <div class="detail-grid-row">
                        <div class="detail-grid-cell">
                            <span class="cell-label">Penghantar</span>
                            <span class="cell-value" title="${item.penghantar}">${item.penghantar}</span>
                        </div>
                        <div class="detail-grid-cell">
                            <span class="cell-label">Tower / Set</span>
                            <span class="cell-value">${item.tower} • <strong>${item.jumlahSet} Set</strong></span>
                        </div>
                    </div>

                    <div class="detail-grid-row">
                        <div class="detail-grid-cell">
                            <span class="cell-label">Merk Terpasang</span>
                            <span class="tag-merk">${item.merk}</span>
                        </div>
                        <div class="detail-grid-cell">
                            <span class="cell-label">Tgl Pemasangan</span>
                            <span class="cell-value" style="font-size: 11px;">${item.tanggal}</span>
                        </div>
                    </div>

                    <div class="detail-bottom-info">
                        <strong>Penyebab:</strong> ${item.penyebab}
                    </div>
                </div>
            `).join('');

            renderPaginationControls(Math.ceil(totalItems / itemsPerPage));
        }

        function renderPaginationControls(totalPages) {
            const container = document.getElementById('paginationControls');
            if (totalPages <= 1) { container.innerHTML = ''; return; }
            let html = '';
            for (let i = 1; i <= totalPages; i++) {
                html += `<button class="page-num-btn ${i === currentPage ? 'active' : ''}" onclick="goToPage(${i})">${i}</button>`;
            }
            container.innerHTML = html;
        }

        function goToPage(page) {
            currentPage = page;
            renderDetailList();
        }

        function handleSearch(query) {
            const q = query.toLowerCase().trim();
            filteredData = ersMasterData.filter(item => {
                return item.unitInduk.toLowerCase().includes(q) ||
                       item.unitPelaksana.toLowerCase().includes(q) ||
                       item.penghantar.toLowerCase().includes(q) ||
                       item.merk.toLowerCase().includes(q) ||
                       item.penyebab.toLowerCase().includes(q);
            });
            currentPage = 1;
            renderDetailList();
        }

        function filterByStatus(status) {
            filteredData = ersMasterData.filter(item => item.statusSet === status);
            currentPage = 1;
            renderDetailList();
            scrollToDetail();
        }

        function openFilterModal() { document.getElementById('filterModal').classList.add('active'); }
        function closeFilterModal(e) { if (e.target.id === 'filterModal') document.getElementById('filterModal').classList.remove('active'); }
        function closeFilterModalDirect() { document.getElementById('filterModal').classList.remove('active'); }

        function applyFilterDrawer() {
            const ui = document.getElementById('filterUnitInduk').value;
            const status = document.getElementById('filterStatusSet').value;
            filteredData = ersMasterData.filter(item => {
                let matchUI = (ui === 'ALL' || item.unitInduk === ui);
                let matchStatus = (status === 'ALL' || item.statusSet === status);
                return matchUI && matchStatus;
            });
            currentPage = 1;
            renderDetailList();
            closeFilterModalDirect();
        }

        function resetFilters() {
            document.getElementById('filterKantorPusat').value = 'PLN_PUSAT';
            document.getElementById('filterUnitInduk').value = 'ALL';
            document.getElementById('filterStatusSet').value = 'ALL';
            document.getElementById('searchInput').value = '';
            filteredData = [...ersMasterData];
            currentPage = 1;
            renderDetailList();
            closeFilterModalDirect();
        }

        function openCatalogModal() { document.getElementById('catalogModal').classList.add('active'); }
        function closeCatalogModal(e) { if (e.target.id === 'catalogModal') document.getElementById('catalogModal').classList.remove('active'); }
        function closeCatalogModalDirect() { document.getElementById('catalogModal').classList.remove('active'); }

        window.addEventListener('DOMContentLoaded', () => {
            initMap();
            initCharts();
            renderDetailList();
        });
    </script>
</body>
</html>
"""

target_path = r"c:\KERJAAN\Project\hifi-transmisi\hifi-mobile\ers\home-mobile.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Restored clean white initial dashboard concept successfully!")
