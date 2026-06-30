import sys
import re

file_path = r'c:\KERJAAN\Project\hifi-transmisi\hifi-new-pst\Master Sub-sistem\tambah-data-sub-sistem.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sistem file
sistem_content = content
# Change title
sistem_content = sistem_content.replace('<title>Master Sub-sistem – Tambah Data – PLN</title>', '<title>Master Sistem – Tambah Data – PLN</title>')
sistem_content = sistem_content.replace('<div class="page-title">Master Sub-sistem</div>', '<div class="page-title">Master Sistem</div>')
sistem_content = sistem_content.replace('<a href="#">Master Sub-sistem</a>', '<a href="#">Master Sistem</a>')
sistem_content = sistem_content.replace('<div class="section-label">Informasi Sub-sistem</div>', '<div class="section-label">Informasi Sistem</div>')

# Replace the form part
form_start = sistem_content.find('<div class="form-row cols-2">')
form_end = sistem_content.find('</main>')

new_form = """<div class="form-row cols-2">
                    <div class="field">
                        <label>Nama Sistem <span style="color:var(--danger)">*</span></label>
                        <input type="text" id="nama-sistem" placeholder="Masukkan Nama Sistem" />
                        <div class="help-text">Ketikkan nama sistem</div>
                    </div>

                    <div class="field">
                        <label>UNIT INDUK P2B <span style="color:var(--danger)">*</span></label>
                        <select id="unit-induk">
                            <option value="" disabled selected>Pilih Unit Induk</option>
                            <option value="UIP2B Jamali">UIP2B Jamali</option>
                            <option value="UIP2B Sumatera">UIP2B Sumatera</option>
                            <option value="UIP2B Kalimantan">UIP2B Kalimantan</option>
                            <option value="UIP2B Sulawesi">UIP2B Sulawesi</option>
                        </select>
                        <div class="help-text">Pilih unit induk P2B</div>
                    </div>

                    <div class="field">
                        <label>Pembangkit Terbesar <span style="color:var(--danger)">*</span></label>
                        <input type="text" id="pembangkit-terbesar" placeholder="Masukkan Nama Pembangkit" />
                        <div class="help-text">Pembangkit terbesar (Parent 1, Pembangkit)</div>
                    </div>
                    
                    <div class="field">
                        <label>Kapasitas <span style="color:var(--danger)">*</span></label>
                        <input type="number" id="kapasitas" placeholder="Masukkan Kapasitas" />
                        <div class="help-text">Kapasitas sistem (dalam MW)</div>
                    </div>
                </div>
            </div>
"""
sistem_content = sistem_content[:form_start] + new_form + sistem_content[form_end:]

# Replace JS script block with simpler one
js_start = sistem_content.find('<script>')
js_end = sistem_content.find('</script>') + len('</script>')
new_js = """<script>
        function submitData() {
            const nama = document.getElementById('nama-sistem').value;
            const unit = document.getElementById('unit-induk').value;
            if(!nama || !unit) {
                alert('Harap isi Nama Sistem dan Unit Induk');
                return;
            }
            alert('Data Sistem ' + nama + ' berhasil ditambahkan!');
        }
    </script>"""
sistem_content = sistem_content[:js_start] + new_js + sistem_content[js_end:]

# Write to file
sistem_path = r'c:\KERJAAN\Project\hifi-transmisi\hifi-new-pst\Master Sub-sistem\tambah-data-sistem.html'
with open(sistem_path, 'w', encoding='utf-8') as f:
    f.write(sistem_content)

print('Regenerated', sistem_path)
