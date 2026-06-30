import re

def update_file(filepath, is_subsistem):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove BATAL button
    content = re.sub(r'<button class="btn-cancel"[^>]*>BATAL</button>\s*', '', content)
    
    # 2. Add Modal CSS before </style>
    modal_css = """
        /* SUCCESS MODAL */
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.4); backdrop-filter: blur(4px); z-index: 999; display: none; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s; }
        .modal-overlay.open { display: flex; opacity: 1; }
        .modal-card { background: var(--card); padding: 32px; border-radius: var(--radius-lg); width: 90%; max-width: 400px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.1); transform: scale(0.95); transition: transform 0.3s; }
        .modal-overlay.open .modal-card { transform: scale(1); }
        .modal-icon-success { width: 64px; height: 64px; background: #DCFCE7; color: #15803D; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px; }
        .modal-title { font-size: 20px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
        .modal-desc { font-size: 14px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.5; }
    """
    content = content.replace("</style>", modal_css + "\n</style>")
    
    # 3. Add Modal HTML before <script>
    modal_html = """
    <!-- SUCCESS MODAL -->
    <div class="modal-overlay" id="successModal">
        <div class="modal-card">
            <div class="modal-icon-success">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h3 class="modal-title">Berhasil Disimpan!</h3>
            <p class="modal-desc" id="successDesc">Data berhasil ditambahkan.</p>
            <div style="display: flex; gap: 12px; justify-content: center;">
                <button class="btn-submit" onclick="closeSuccessModal()">OK, Kembali</button>
            </div>
        </div>
    </div>
    """
    content = content.replace("<script>", modal_html + "\n    <script>")
    
    # 4. Replace submitData logic
    if is_subsistem:
        old_submit = """function submitData() {
            const sistem = document.getElementById('sistem').value;
            const nama = document.getElementById('nama-subsistem').value;

            if (!sistem || !nama) {
                alert("Mohon lengkapi Sistem dan Nama Sub-sistem.");
                return;
            }

            alert("Data Sub-sistem " + nama + " berhasil ditambahkan!");
            window.parent.location.hash = 'page=' + encodeURIComponent('../hifi-new-pst/Master Sub-sistem/mainpage-osl.html');
        }"""
        new_submit = """function closeSuccessModal() {
            document.getElementById('successModal').classList.remove('open');
            window.parent.location.hash = 'page=' + encodeURIComponent('../hifi-new-pst/Master Sub-sistem/mainpage-osl.html');
        }

        function submitData() {
            const sistem = document.getElementById('sistem').value;
            const nama = document.getElementById('nama-subsistem').value;

            if (!sistem || !nama) {
                alert("Mohon lengkapi Sistem dan Nama Sub-sistem.");
                return;
            }

            document.getElementById('successDesc').innerText = "Data Sub-sistem " + nama + " berhasil ditambahkan!";
            document.getElementById('successModal').classList.add('open');
        }"""
    else:
        old_submit = """function submitData() {
            const nama = document.getElementById('nama-sistem').value;
            const unit = document.getElementById('unit-induk').value;
            if(!nama || !unit) {
                alert('Harap isi Nama Sistem dan Unit Induk');
                return;
            }
            alert('Data Sistem ' + nama + ' berhasil ditambahkan!');
            window.parent.location.hash = 'page=' + encodeURIComponent('../hifi-new-pst/Master Sub-sistem/mainpage-osl.html');
        }"""
        new_submit = """function closeSuccessModal() {
            document.getElementById('successModal').classList.remove('open');
            window.parent.location.hash = 'page=' + encodeURIComponent('../hifi-new-pst/Master Sub-sistem/mainpage-osl.html');
        }

        function submitData() {
            const nama = document.getElementById('nama-sistem').value;
            const unit = document.getElementById('unit-induk').value;
            if(!nama || !unit) {
                alert('Harap isi Nama Sistem dan Unit Induk');
                return;
            }
            document.getElementById('successDesc').innerText = 'Data Sistem ' + nama + ' berhasil ditambahkan!';
            document.getElementById('successModal').classList.add('open');
        }"""
    
    if old_submit in content:
        content = content.replace(old_submit, new_submit)
    else:
        # Fallback regex if spacing is different
        content = re.sub(r'function submitData\(\)\s*\{[^}]*\}', new_submit, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('c:/KERJAAN/Project/hifi-transmisi/hifi-new-pst/Master Sub-sistem/tambah-data-sistem.html', False)
update_file('c:/KERJAAN/Project/hifi-transmisi/hifi-new-pst/Master Sub-sistem/tambah-data-sub-sistem.html', True)
print("Forms updated!")
