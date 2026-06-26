import os
import glob
import re

css_content = """<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
  --pln-blue: #0A58CA;
  --pln-blue-mid: #0d6efd;
  --pln-blue-light: #E7F1FF;
  --pln-yellow: #F7A800;
  --bg: #F8FAFC;
  --card: #FFFFFF;
  --surface: #F1F5F9;
  --border: #E2E8F0;
  --text-primary: #0F172A;
  --text-secondary: #475569;
  --text-hint: #94A3B8;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --sidebar-w: 64px;
  --danger: #DC2626;
  --danger-light: #FEE2E2;
  --success: #16A34A;
  --success-light: #DCFCE7;
  --warning: #D97706;
  --warning-light: #FEF3C7;
  
  /* Additional colors for chips */
  --chip-proses-bg: #FFF7ED; --chip-proses-text: #C2410C; --chip-proses-dot: #F97316;
  --chip-kirim-bg: #EFF6FF; --chip-kirim-text: #1D4ED8; --chip-kirim-dot: #3B82F6;
  --chip-tunggu-bg: #FEFCE8; --chip-tunggu-text: #854D0E; --chip-tunggu-dot: #EAB308;
  --chip-review-bg: #FDF4FF; --chip-review-text: #7E22CE; --chip-review-dot: #A855F7;
  --chip-approval-bg: #F0FDF4; --chip-approval-text: #166534; --chip-approval-dot: #22C55E;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4, h5, h6, .page-title, .section-label, .card-title, .logo span {
  font-family: 'Outfit', sans-serif;
}

body {
  background: var(--bg);
  color: var(--text-primary);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

/* LAYOUT */
.layout {
  display: flex;
  min-height: 100vh;
}

/* SIDEBAR */
.sidebar {
  width: var(--sidebar-w);
  background: rgba(10, 30, 60, 0.95);
  backdrop-filter: blur(12px);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px 0;
  gap: 8px;
  flex-shrink: 0;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  z-index: 100;
  box-shadow: 2px 0 15px rgba(0,0,0,0.05);
}

.sidebar .logo {
  width: 40px;
  height: 40px;
  background: var(--pln-yellow);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
  box-shadow: 0 4px 10px rgba(247, 168, 0, 0.3);
  transition: transform 0.2s;
}
.sidebar .logo:hover {
  transform: scale(1.05);
}
.sidebar .logo span {
  color: #003B8E;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.5px;
}

.sidebar .nav-item, .nav-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: rgba(255, 255, 255, 0.6);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: 4px;
}
.sidebar .nav-item:hover, .nav-icon:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  transform: translateY(-2px);
}
.sidebar .nav-item.active, .nav-icon.active {
  background: var(--pln-blue);
  color: #fff;
  box-shadow: 0 4px 12px rgba(10, 88, 202, 0.4);
}
.sidebar .nav-item svg, .nav-icon svg {
  width: 20px;
  height: 20px;
}
.sidebar-bottom {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* MAIN CONTENT */
.main {
  margin-left: var(--sidebar-w);
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: calc(100% - var(--sidebar-w));
}

/* TOPBAR */
.topbar {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 12px 32px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 90;
  font-size: 13px;
  color: var(--text-secondary);
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-primary);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: var(--card);
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}
.back-btn:hover {
  background: var(--surface);
  border-color: #CBD5E1;
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.breadcrumb {
  font-size: 12px;
  color: var(--text-hint);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}
.breadcrumb a {
  color: var(--pln-blue);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}
.breadcrumb a:hover {
  color: var(--pln-blue-mid);
}

.page-title {
  font-size: 20px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.3px;
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-log {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--pln-blue);
  background: var(--card);
  color: var(--pln-blue);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 2px 4px rgba(10, 88, 202, 0.05);
}
.btn-log:hover {
  background: var(--pln-blue);
  color: #fff;
  box-shadow: 0 4px 10px rgba(10, 88, 202, 0.2);
}
.log-badge {
  background: var(--pln-yellow);
  color: #7A5200;
  font-size: 11px;
  font-weight: 700;
  border-radius: 20px;
  padding: 2px 8px;
  min-width: 22px;
  text-align: center;
}
.btn-log:hover .log-badge {
  background: #fff;
}

/* CONTENT AREA */
.content {
  padding: 32px;
  flex: 1;
  padding-bottom: 100px;
}

.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

/* CARDS & SECTIONS */
.card, .section-card {
  background: var(--card);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
  overflow: hidden;
  margin-bottom: 24px;
  transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover, .section-card:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
}

.section-card {
  padding: 24px;
}

.section-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.section-label::before {
  content: '';
  display: block;
  width: 4px;
  height: 16px;
  background: var(--pln-blue);
  border-radius: 2px;
}

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  background: rgba(248, 250, 252, 0.5);
}

.search-wrap {
  position: relative;
  display: flex;
  align-items: center;
}
.search-wrap input {
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 16px 10px 40px;
  font-size: 13px;
  width: 280px;
  outline: none;
  color: var(--text-primary);
  background: var(--card);
  transition: all 0.2s;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}
.search-wrap input:focus {
  border-color: var(--pln-blue);
  box-shadow: 0 0 0 3px rgba(10, 88, 202, 0.1);
  width: 320px;
}
.search-icon {
  position: absolute;
  left: 14px;
  color: var(--text-hint);
  transition: color 0.2s;
}
.search-wrap input:focus + .search-icon,
.search-wrap:focus-within .search-icon {
  color: var(--pln-blue);
}

.btn-add {
  background: var(--pln-blue);
  color: #fff;
  border: none;
  border-radius: var(--radius-sm);
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  letter-spacing: 0.3px;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(10, 88, 202, 0.25);
}
.btn-add:hover {
  background: var(--pln-blue-mid);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(10, 88, 202, 0.35);
}

/* FORMS */
.form-row {
  display: grid;
  gap: 20px;
  align-items: start;
  margin-bottom: 20px;
}
.cols-4 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.cols-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.field label {
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
}
.field-val, input, select, textarea {
  width: 100%;
  border: 1px solid transparent;
  border-radius: var(--radius-sm);
  padding: 8px 14px;
  font-size: 13px;
  color: var(--text-primary);
  outline: none;
  background: #F8FAFC;
  min-height: 36px;
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}
.field-val:focus-within, .field-val:focus {
  border-color: var(--pln-blue);
  box-shadow: 0 0 0 3px rgba(10, 88, 202, 0.1);
  background: var(--card);
}
.field-val.muted {
  color: var(--text-hint);
  font-style: italic;
}
.field-val.textarea {
  min-height: 100px;
  line-height: 1.6;
  white-space: pre-wrap;
  resize: vertical;
}
.section-divider {
  height: 1px;
  background: var(--border);
  margin: 24px 0;
}

/* RADIO & CHECKBOX */
.radio-dot {
  width: 18px; height: 18px;
  border-radius: 50%;
  border: 2px solid var(--pln-blue);
  display: inline-flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.radio-dot::after {
  content: ''; width: 8px; height: 8px;
  border-radius: 50%; background: var(--pln-blue);
}
.radio-off {
  width: 18px; height: 18px;
  border-radius: 50%;
  border: 2px solid var(--border);
  display: inline-flex; flex-shrink: 0; background: var(--card);
  transition: border-color 0.2s;
}
.radio-off:hover { border-color: #CBD5E1; }

.radio-group {
  display: flex;
  gap: 12px;
  align-items: center;
}
.radio-opt {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border: 1px solid var(--border);
  border-radius: 20px;
  cursor: pointer;
  background: var(--card);
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s;
}
.radio-opt:hover {
  border-color: var(--pln-blue);
}
.radio-opt input[type="radio"] {
  accent-color: var(--pln-blue);
  width: 15px;
  height: 15px;
  margin: 0;
}
/* For checked state if structured differently, or using :has if supported */
.radio-opt:has(input[type="radio"]:checked) {
  border-color: var(--pln-blue);
  background: var(--pln-blue-light);
  color: var(--pln-blue);
}

.checkbox-custom {
  display: inline-flex; align-items: center; gap: 8px;
  cursor: pointer; font-size: 14px; color: var(--text-primary);
}
.checkbox-custom input {
  width: 18px; height: 18px; cursor: pointer; accent-color: var(--pln-blue);
}

/* DOC TRIGGER & DROP */
.doc-trigger {
  width: 100%;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px dashed var(--pln-blue);
  background: var(--pln-blue-light);
  color: var(--pln-blue);
  font-size: 13px; font-weight: 600;
  cursor: pointer;
  min-height: 36px;
  transition: all 0.2s;
}
.doc-trigger:hover {
  background: #D4E8F8;
}
.doc-trigger svg {
  width: 18px;
  height: 18px;
}

.doc-display {
  width: 100%;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text-secondary);
  font-size: 13px; font-weight: 600;
  cursor: pointer;
  min-height: 36px;
  transition: all 0.2s;
}
.doc-display:hover {
  border-color: var(--pln-blue);
  color: var(--pln-blue);
  background: var(--pln-blue-light);
}
.doc-display svg {
  width: 18px;
  height: 18px;
}
.doc-count-chip {
  background: var(--pln-blue-light);
  color: var(--pln-blue);
  border-radius: 12px;
  padding: 2px 8px;
  font-size: 11px;
  font-weight: 700;
}

.doc-drop {
  border: 2px dashed var(--border);
  border-radius: var(--radius-sm);
  padding: 32px 20px; text-align: center;
  background: var(--card); cursor: pointer; transition: all 0.2s;
}
.doc-drop:hover {
  border-color: var(--pln-blue); background: var(--pln-blue-light);
}

/* DOC OVERLAY MODAL */
.doc-overlay-backdrop {
  position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(4px); z-index: 300; display: none; opacity: 0; transition: opacity 0.3s;
}
.doc-overlay-backdrop.open { display: block; opacity: 1; }

.doc-overlay-panel {
  position: fixed; top: 0; right: 0; width: 50%; height: 100vh;
  background: var(--card); z-index: 301; display: flex; flex-direction: column;
  box-shadow: -8px 0 30px rgba(0, 0, 0, 0.1);
  transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.doc-overlay-backdrop.open .doc-overlay-panel {
  transform: translateX(0);
}

.doc-cat-header {
  padding: 14px 16px; border-bottom: 1px solid var(--border);
  background: #FAFBFC; display: flex; align-items: center; justify-content: space-between;
}
.doc-cat-badge {
  background: var(--pln-blue-light); color: var(--pln-blue);
  border-radius: 12px; padding: 2px 10px; font-size: 11.5px; font-weight: 600;
}
.doc-file-item {
  display: flex; align-items: center; gap: 10px; padding: 12px;
  border: 1px solid var(--border); border-radius: var(--radius-sm);
  background: var(--card); transition: all 0.2s;
}
.doc-file-item:hover { border-color: var(--pln-blue); box-shadow: 0 2px 8px rgba(10, 88, 202, 0.05); }
.doc-file-icon {
  width: 32px; height: 32px; border-radius: 6px; background: var(--pln-blue-light); color: var(--pln-blue);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}

/* TABLES */
.table-container {
  overflow-x: auto;
}
table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13px;
}
thead tr {
  background: #F8FAFC;
}
th {
  padding: 14px 20px;
  text-align: left;
  font-weight: 600;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
  font-size: 12px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
td {
  padding: 14px 20px;
  border-bottom: 1px solid #F1F5F9;
  color: var(--text-primary);
  vertical-align: middle;
  transition: background 0.2s;
}
tr:last-child td { border-bottom: none; }
tbody tr { transition: transform 0.2s, box-shadow 0.2s; }
tbody tr:hover td {
  background: #FAFBFC;
}
tbody tr:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
  transform: translateY(-1px);
  position: relative; z-index: 2;
}

/* CHIPS & TAGS */
.unit-tag {
  display: inline-block;
  background: var(--surface);
  color: var(--text-primary);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 11px;
  font-weight: 600;
  margin: 2px 0;
}
.dest-tag {
  font-size: 11px; color: var(--text-hint); font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.5px;
}
.chip {
  display: inline-flex; align-items: center; gap: 6px;
  border-radius: 20px; padding: 4px 12px;
  font-size: 12px; font-weight: 600; white-space: nowrap;
}
.chip-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

.chip-proses { background: var(--chip-proses-bg); color: var(--chip-proses-text); }
.chip-proses .chip-dot { background: var(--chip-proses-dot); }

.chip-kirim { background: var(--chip-kirim-bg); color: var(--chip-kirim-text); }
.chip-kirim .chip-dot { background: var(--chip-kirim-dot); }

.chip-tunggu { background: var(--chip-tunggu-bg); color: var(--chip-tunggu-text); }
.chip-tunggu .chip-dot { background: var(--chip-tunggu-dot); }

.chip-review { background: var(--chip-review-bg); color: var(--chip-review-text); }
.chip-review .chip-dot { background: var(--chip-review-dot); }

.chip-approval { background: var(--chip-approval-bg); color: var(--chip-approval-text); }
.chip-approval .chip-dot { background: var(--chip-approval-dot); }

.chip-terima {
  background: var(--pln-blue-light); color: var(--pln-blue);
  border: 1px solid #BFDBFE;
}

/* STATUS PILLS & TOOLTIP */
.status-pill {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 12px; border-radius: 20px;
  font-size: 12px; font-weight: 600; white-space: nowrap;
}
.status-dot {
  width: 6px; height: 6px; border-radius: 50%;
}
.s-srm { background: #FEF3C7; color: #D97706; border: 1px solid #FDE68A; }
.s-srm .status-dot { background: #D97706; }

.s-msb { background: #F0FDF4; color: #16A34A; border: 1px solid #BBF7D0; }
.s-msb .status-dot { background: #16A34A; }

.s-rej { background: #FEF2F2; color: #DC2626; border: 1px solid #FECACA; }
.s-rej .status-dot { background: #DC2626; }

.tooltip-wrap {
  position: relative;
  display: inline-flex;
  margin-left: 6px;
}
.tooltip-icon {
  background: none; border: none; color: var(--text-hint);
  cursor: pointer; width: 18px; height: 18px; display: flex; align-items: center; justify-content: center;
  transition: color 0.2s; padding: 0;
}
.tooltip-icon:hover { color: var(--pln-blue); }
.tooltip-box {
  position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%) translateY(-8px);
  background: #1E293B; color: #F8FAFC;
  padding: 10px 14px; border-radius: 8px; font-size: 12px; font-weight: 400;
  width: max-content; max-width: 220px; line-height: 1.5; white-space: normal;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  visibility: hidden; opacity: 0; transition: all 0.2s;
  z-index: 100;
  pointer-events: none;
  text-align: left;
}
.tooltip-box::after {
  content: ''; position: absolute; top: 100%; left: 50%; margin-left: -5px;
  border-width: 5px; border-style: solid;
  border-color: #1E293B transparent transparent transparent;
}
.tooltip-wrap.show .tooltip-box, .tooltip-wrap:hover .tooltip-box {
  visibility: visible; opacity: 1; transform: translateX(-50%) translateY(-4px);
}
table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13px;
}
thead tr {
  background: #F8FAFC;
}
th {
  padding: 14px 20px;
  text-align: left;
  font-weight: 600;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
  font-size: 12px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
td {
  padding: 14px 20px;
  border-bottom: 1px solid #F1F5F9;
  color: var(--text-primary);
  vertical-align: middle;
  transition: background 0.2s;
}
tr:last-child td { border-bottom: none; }
tbody tr { transition: transform 0.2s, box-shadow 0.2s; }
tbody tr:hover td {
  background: #FAFBFC;
}
tbody tr:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
  transform: translateY(-1px);
  position: relative; z-index: 2;
}

/* CHIPS & TAGS */
.unit-tag {
  display: inline-block;
  background: var(--surface);
  color: var(--text-primary);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 11px;
  font-weight: 600;
  margin: 2px 0;
}
.dest-tag {
  font-size: 11px; color: var(--text-hint); font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.5px;
}
.chip {
  display: inline-flex; align-items: center; gap: 6px;
  border-radius: 20px; padding: 4px 12px;
  font-size: 12px; font-weight: 600; white-space: nowrap;
}
.chip-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

.chip-proses { background: var(--chip-proses-bg); color: var(--chip-proses-text); }
.chip-proses .chip-dot { background: var(--chip-proses-dot); }

.chip-kirim { background: var(--chip-kirim-bg); color: var(--chip-kirim-text); }
.chip-kirim .chip-dot { background: var(--chip-kirim-dot); }

.chip-tunggu { background: var(--chip-tunggu-bg); color: var(--chip-tunggu-text); }
.chip-tunggu .chip-dot { background: var(--chip-tunggu-dot); }

.chip-review { background: var(--chip-review-bg); color: var(--chip-review-text); }
.chip-review .chip-dot { background: var(--chip-review-dot); }

.chip-approval { background: var(--chip-approval-bg); color: var(--chip-approval-text); }
.chip-approval .chip-dot { background: var(--chip-approval-dot); }

.tipe-satuan {
  background: #E0F2FE; color: #0369A1; border-radius: 6px;
  padding: 4px 10px; font-size: 11px; font-weight: 700; border: 1px solid #BAE6FD;
}
.tipe-set {
  background: #FCE7F3; color: #BE185D; border-radius: 6px;
  padding: 4px 10px; font-size: 11px; font-weight: 700; border: 1px solid #FBCFE8;
}

/* ACTION BUTTONS */
.action-btn, .aksi-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  cursor: pointer;
  padding: 6px;
  color: var(--text-secondary);
  border-radius: 8px;
  transition: all 0.2s;
  display: inline-flex; align-items: center; justify-content: center;
  width: 32px; height: 32px;
}
.action-btn:hover, .aksi-btn:hover {
  background: var(--pln-blue);
  color: #fff;
  border-color: var(--pln-blue);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(10, 88, 202, 0.2);
}

/* PAGINATION */
.pagination {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 24px; border-top: 1px solid var(--border);
  background: #FAFBFC;
}
.pag-info {
  font-size: 13px; color: var(--text-secondary);
  display: flex; align-items: center; gap: 8px;
}
.pag-info select {
  border: 1px solid var(--border); border-radius: 6px;
  padding: 4px 8px; font-size: 13px; color: var(--text-primary);
  outline: none; cursor: pointer;
}
.pag-btns {
  display: flex; gap: 6px; align-items: center;
}
.pag-btn {
  width: 32px; height: 32px;
  border: 1px solid var(--border); background: #fff; border-radius: 8px;
  font-size: 13px; cursor: pointer; color: var(--text-secondary);
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s; font-weight: 500;
}
.pag-btn.active {
  background: var(--pln-blue); color: #fff; border-color: var(--pln-blue);
  box-shadow: 0 4px 8px rgba(10, 88, 202, 0.25); font-weight: 600;
}
.pag-btn:hover:not(.active) {
  background: var(--surface); border-color: #CBD5E1; color: var(--text-primary);
  transform: translateY(-1px);
}

/* FOOTER FORMS */
.form-footer {
  position: fixed; bottom: 0; left: var(--sidebar-w); right: 0;
  background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px);
  border-top: 1px solid var(--border); padding: 16px 32px;
  display: flex; align-items: center; justify-content: flex-end; gap: 16px;
  z-index: 80; box-shadow: 0 -4px 20px rgba(0,0,0,0.03);
}
.btn-reject-footer {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 24px; border-radius: var(--radius-sm);
  border: 1px solid var(--danger); background: var(--danger-light); color: var(--danger);
  font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.2s;
}
.btn-reject-footer:hover {
  background: var(--danger); color: #fff; transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.25);
}
.btn-approve-footer {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 24px; border-radius: var(--radius-sm); border: none;
  background: var(--pln-blue); color: #fff; font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
}
.btn-approve-footer:hover {
  background: var(--pln-blue-mid); transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(10, 88, 202, 0.3);
}

/* ACCORDION */
.acc-group {
  border: 1px solid var(--border); border-radius: var(--radius-lg);
  margin-bottom: 16px; overflow: hidden; background: var(--card);
  transition: box-shadow 0.2s;
}
.acc-group:hover { box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
.acc-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 20px; background: #FAFBFC; border-bottom: 1px solid var(--border);
  cursor: pointer; transition: background 0.2s;
}
.acc-header:hover { background: #F1F5F9; }
.acc-header-left { display: flex; align-items: center; gap: 12px; }
.acc-title { font-size: 14px; font-weight: 600; color: var(--text-primary); }
.acc-icon { width: 20px; height: 20px; color: var(--text-secondary); transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.acc-group.open .acc-icon { transform: rotate(180deg); }
.acc-body { padding: 20px; }

/* FILE LIST */
.doc-file-list { margin-top: 16px; display: flex; flex-direction: column; gap: 12px; }
.doc-file-item {
  display: flex; align-items: center; padding: 12px 16px;
  border: 1px solid var(--border); border-radius: var(--radius-sm);
  background: var(--card); transition: box-shadow 0.2s;
}
.doc-file-item:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.doc-file-item svg { width: 20px; height: 20px; color: var(--pln-blue); flex-shrink: 0; margin-right: 12px; }
.doc-file-info { flex: 1; min-width: 0; }
.doc-file-name { font-size: 13px; font-weight: 500; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.doc-file-meta { font-size: 11px; color: var(--text-hint); margin-top: 4px; }
.doc-file-remove {
  width: 32px; height: 32px; border-radius: 8px; border: none; background: var(--surface);
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  color: var(--text-secondary); transition: all 0.2s;
}
.doc-file-remove:hover { background: var(--danger-light); color: var(--danger); transform: scale(1.05); }

/* MISC */
.val-badge {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 32px; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;
}
.overlay-backdrop {
  position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(4px); z-index: 300; display: none; opacity: 0; transition: opacity 0.3s;
}
.overlay-backdrop.open { display: block; opacity: 1; }
.side-panel {
  position: fixed; top: 0; right: 0; width: 50%; height: 100vh;
  background: var(--card); z-index: 301; display: flex; flex-direction: column;
  box-shadow: -8px 0 30px rgba(0, 0, 0, 0.1);
  transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.overlay-backdrop.open .side-panel { transform: translateX(0); }

/* EXTENDED FORMS (Direct children of .field) */
.field input:not([type="radio"]):not([type="checkbox"]), .field select, .field textarea {
  width: 100%;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 13px;
  color: var(--text-primary);
  background: var(--surface);
  min-height: 36px;
  transition: all 0.2s;
  outline: none;
}

/* SELECT / COMBOBOX CUSTOM ARROW */
.field select, .unit-sel {
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 12px;
  padding-right: 36px;
}

/* DATE PICKER ICON (NATIVE) */
.field input[type="date"] {
  position: relative;
  padding-right: 36px;
}
.field input[type="date"]::-webkit-calendar-picker-indicator {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  opacity: 0.5;
  transition: opacity 0.2s;
}
.field input[type="date"]::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}

/* CUSTOM DATE PICKER (DIV) */
.date-picker {
  display: flex !important;
  align-items: center;
  justify-content: space-between;
}
.date-picker svg {
  color: var(--text-secondary);
  flex-shrink: 0;
}
.field input:not([type="radio"]):not([type="checkbox"]):focus, .field select:focus, .field textarea:focus {
  border-color: var(--pln-blue);
  box-shadow: 0 0 0 3px rgba(10, 88, 202, 0.1);
  background: var(--card);
}
.field input:not([type="radio"]):not([type="checkbox"]):disabled, .field select:disabled, .field textarea:disabled {
  background: var(--surface) !important;
  color: var(--text-hint) !important;
  cursor: not-allowed !important;
}

/* RADIO OPTIONS */
.radio-group {
  display: flex;
  gap: 16px;
  align-items: center;
}
.radio-opt {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: 1px solid var(--border);
  border-radius: 20px;
  background: var(--card);
  font-size: 13px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s;
}
.radio-opt:hover {
  border-color: var(--pln-blue-mid);
  background: var(--pln-blue-light);
}
.radio-opt.selected {
  border-color: var(--pln-blue);
  background: var(--pln-blue-light);
  color: var(--pln-blue);
  font-weight: 600;
}
.radio-opt input {
  accent-color: var(--pln-blue);
  cursor: pointer;
}

/* BUTTONS */
.view-stock-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.view-stock-btn:hover {
  background: var(--card);
  border-color: var(--pln-blue);
  color: var(--pln-blue);
  transform: translateY(-1px);
}

.btn-cancel {
  padding: 10px 24px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-cancel:hover:not(:disabled) {
  background: var(--danger-light);
  border-color: var(--danger);
  color: var(--danger);
}
.btn-submit {
  padding: 10px 24px;
  border-radius: var(--radius-sm);
  border: none;
  background: var(--pln-blue);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-submit:hover:not(:disabled) {
  background: var(--pln-blue-mid);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(10, 88, 202, 0.3);
}

.btn-log {
  white-space: nowrap;
}

.preview-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #FEF3C7;
  color: #D97706;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  border: 1px solid #FDE68A;
}
.preview-badge svg {
  width: 16px;
  height: 16px;
}

.edit-input {
  width: 100%;
  min-height: 36px;
  padding: 8px 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--card);
  color: var(--text-primary);
  font-size: 13px;
  outline: none;
  transition: all 0.2s;
}
.edit-input:focus {
  border-color: var(--pln-blue);
}

.btn-tambah-unit {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border: 1px dashed var(--pln-blue);
  background: var(--pln-blue-light);
  color: var(--pln-blue);
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-tambah-unit:hover {
  background: #d4e8f8;
}

.btn-footer-simpan {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 24px;
  border-radius: var(--radius-sm);
  border: none;
  background: var(--pln-blue);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-footer-simpan:hover {
  background: var(--pln-blue-mid);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(10, 88, 202, 0.3);
}

.karantina-table {
  width: 100%;
  border-collapse: collapse;
}
.karantina-table th {
  background: #F8FAFC;
  padding: 12px 16px;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border);
  text-align: left;
}
.karantina-table td {
  padding: 14px 16px;
  border-bottom: 1px solid #F1F5F9;
  vertical-align: middle;
  font-size: 13px;
}
.qty-input {
  width: 60px;
  padding: 6px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  text-align: center;
  font-size: 13px;
  outline: none;
}
.qty-input:focus {
  border-color: var(--pln-blue);
}
.btn-evidence {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s;
}
.btn-evidence:hover {
  background: var(--card);
  border-color: var(--pln-blue);
  color: var(--pln-blue);
}

/* UNIT SELECT */
.unit-sel-wrap {
  position: relative;
  width: 100%;
}
.unit-sel {
  width: 100%;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 13px;
  color: var(--text-primary);
  background: var(--card);
  outline: none;
  transition: border-color 0.2s;
}
.unit-sel:focus {
  border-color: var(--pln-blue);
}

.doc-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px 12px;
  border: 1px dashed var(--pln-blue);
  border-radius: var(--radius-sm);
  background: var(--pln-blue-light);
  color: var(--pln-blue);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  min-height: 36px;
  transition: all 0.2s;
}
.doc-trigger:hover {
  background: #D4E8F8;
}
.doc-trigger svg, .doc-drop svg {
  width: 18px;
  height: 18px;
}

/* STOCK STANDBY MODAL / PANELS */
.ss-backdrop {
  position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(4px); z-index: 300; display: none; opacity: 0; transition: opacity 0.3s;
}
.ss-backdrop.open { display: block; opacity: 1; }

.ss-panel {
  position: fixed; top: 0; right: 0; width: 60%; height: 100vh;
  background: var(--card); z-index: 301; display: flex; flex-direction: column;
  box-shadow: -8px 0 30px rgba(0, 0, 0, 0.1);
  transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.ss-backdrop.open + .ss-panel, .ss-panel.open, body.ss-open .ss-panel {
  transform: translateX(0);
}

.ss-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 24px; border-bottom: 1px solid var(--border);
}
.ss-title { font-size: 16px; font-weight: 600; display: flex; align-items: center; gap: 8px; }
.ss-title-badge { background: var(--pln-blue-light); color: var(--pln-blue); padding: 2px 8px; border-radius: 12px; font-size: 12px; }
.ss-close { background: none; border: none; cursor: pointer; color: var(--text-secondary); transition: color 0.2s; }
.ss-close:hover { color: var(--danger); }

.ss-toolbar { padding: 16px 24px; display: flex; gap: 12px; align-items: center; border-bottom: 1px solid var(--border); background: #FAFBFC; }
.ss-search { position: relative; flex: 1; display: flex; align-items: center; }
.ss-search-ico { position: absolute; left: 12px; color: var(--text-hint); }
.ss-search input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 8px 12px 8px 36px; outline: none; transition: border-color 0.2s; font-size: 13px; }
.ss-search input:focus { border-color: var(--pln-blue); }
.btn-log {
  display: flex; align-items: center; gap: 8px;
  background: var(--pln-blue-light); color: var(--pln-blue);
  border: 1px solid #BFDBFE; border-radius: var(--radius-sm);
  padding: 8px 16px; font-size: 13px; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
}
.btn-log:hover { background: #D4E8F8; border-color: var(--pln-blue); transform: translateY(-1px); box-shadow: 0 4px 8px rgba(10,88,202,0.05); }
.btn-log svg { width: 16px; height: 16px; }

.btn-ubah-data {
  display: flex; align-items: center; gap: 8px;
  background: var(--pln-blue); color: #fff;
  border: none; border-radius: var(--radius-sm);
  padding: 8px 16px; font-size: 13px; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
}
.btn-ubah-data:hover { background: #0B65E6; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(10, 88, 202, 0.3); }
.btn-ubah-data svg { width: 16px; height: 16px; }

.ss-filter-bar { display: none; padding: 16px 24px; background: var(--surface); border-bottom: 1px solid var(--border); gap: 16px; flex-wrap: wrap; }
.ss-filter-bar.open { display: flex; }

</style>"""

root_dir = r"c:\KERJAAN\Project\hifi-ers\hifi-ers\Mutasi"

files = glob.glob(os.path.join(root_dir, "*.html"))
changed = 0

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        continue
    
    # Check if there is an existing <style> tag
    if "<style" in content and "</style>" in content:
        # replace the first style tag block (we assume only one main style tag)
        new_content = re.sub(r'(?is)<style.*?>.*?</style>', css_content, content, count=1)
        
        if new_content != content:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected premium CSS to {filepath}")
                changed += 1
            except Exception as e:
                print(f"Could not write {filepath}: {e}")
    else:
        # No style tag found? We inject it inside <head>
        new_content = content.replace('</head>', css_content + '\n</head>')
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added premium CSS to {filepath}")
            changed += 1
        except Exception as e:
            print(f"Could not write {filepath}: {e}")

print(f"Total files updated: {changed}")
