import sys
import re

file_path = r'c:\KERJAAN\Project\hifi-transmisi\hifi-new-pst\Master Sub-sistem\tambah-data-sub-sistem.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the HTML block from <div class="section-label" style="margin-top: 32px;">Kriteria Sub-sistem</div> to </div> </main>
start_html = content.find('<div class="section-label" style="margin-top: 32px;">Kriteria Sub-sistem</div>')
end_html = content.find('</main>')

html_replacement = """
                <div class="section-label" style="margin-top: 32px;">Kriteria N-1 (Mandatory)</div>
                <div id="n-1">
                    <div class="form-row cols-2">
                        <div class="field">
                            <label>Jenis Kriteria N-1 <span style="color:var(--danger)">*</span></label>
                            <select id="jenis-kriteria-n1" onchange="onJenisKriteriaChange('n1')">
                                <option value="" disabled selected>Pilih Jenis Kriteria</option>
                                <option value="TRAFO">TRAFO</option>
                                <option value="PEMBANGKIT">PEMBANGKIT</option>
                                <option value="PENGHANTAR">PENGHANTAR</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-parent-n1">Data Parent N-1 <span style="color:var(--danger)">*</span></label>
                            <select id="parent-n1" onchange="onParentChange('n1')" disabled>
                                <option value="" disabled selected>Pilih Data Parent</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-child-n1">Kriteria N-1 <span style="color:var(--danger)">*</span></label>
                            <select id="kriteria-n1" onchange="onChildChange('n1')" disabled>
                                <option value="" disabled selected>Pilih Kriteria</option>
                            </select>
                        </div>
                        <div class="field">
                            <label>Kapasitas N-1 <span style="color:var(--danger)">*</span></label>
                            <input type="number" id="kapasitas-n1" placeholder="Masukkan Kapasitas" />
                        </div>
                    </div>
                </div>

                <div class="section-label" style="margin-top: 32px;">Kriteria N-1-1 (Opsional)</div>
                <div id="n-1-1">
                    <div class="form-row cols-2">
                        <div class="field">
                            <label>Jenis Kriteria N-1-1</label>
                            <select id="jenis-kriteria-n11" onchange="onJenisKriteriaChange('n11')">
                                <option value="" disabled selected>Pilih Jenis Kriteria</option>
                                <option value="TRAFO">TRAFO</option>
                                <option value="PEMBANGKIT">PEMBANGKIT</option>
                                <option value="PENGHANTAR">PENGHANTAR</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-parent-n11">Data Parent N-1-1</label>
                            <select id="parent-n11" onchange="onParentChange('n11')" disabled>
                                <option value="" disabled selected>Pilih Data Parent</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-child-n11">Kriteria N-1-1</label>
                            <select id="kriteria-n11" onchange="onChildChange('n11')" disabled>
                                <option value="" disabled selected>Pilih Kriteria</option>
                            </select>
                        </div>
                        <div class="field">
                            <label>Kapasitas N-1-1</label>
                            <input type="number" id="kapasitas-n11" placeholder="Masukkan Kapasitas" />
                        </div>
                    </div>
                </div>

                <div class="section-label" style="margin-top: 32px;">Kriteria N-2 (Opsional)</div>
                <div id="n-2">
                    <div class="form-row cols-2">
                        <div class="field">
                            <label>Jenis Kriteria N-2</label>
                            <select id="jenis-kriteria-n2" onchange="onJenisKriteriaChange('n2')">
                                <option value="" disabled selected>Pilih Jenis Kriteria</option>
                                <option value="TRAFO">TRAFO</option>
                                <option value="PEMBANGKIT">PEMBANGKIT</option>
                                <option value="PENGHANTAR">PENGHANTAR</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-parent-n2">Data Parent N-2</label>
                            <select id="parent-n2" onchange="onParentChange('n2')" disabled>
                                <option value="" disabled selected>Pilih Data Parent</option>
                            </select>
                        </div>
                        <div class="field">
                            <label id="label-child-n2">Kriteria N-2</label>
                            <select id="kriteria-n2" onchange="onChildChange('n2')" disabled>
                                <option value="" disabled selected>Pilih Kriteria</option>
                            </select>
                        </div>
                        <div class="field">
                            <label>Kapasitas N-2</label>
                            <input type="number" id="kapasitas-n2" placeholder="Masukkan Kapasitas" />
                        </div>
                    </div>
                </div>
            </div>
"""

content = content[:start_html] + html_replacement + content[end_html:]

# Now replace the JS part for kriteria
start_js = content.find('function openTab(tabId, element) {')
end_js = content.find('function submitData() {')

js_replacement = """
        const hierarchyData = {
            "TRAFO": {
                labelParent: "Data GI",
                labelChild: "Data Bay Trafo",
                parents: ["GI Cawang", "GI Gandul", "GI Kembangan"],
                children: {
                    "GI Cawang": [{name: "Bay Trafo 1 Cawang", cap: 150}, {name: "Bay Trafo 2 Cawang", cap: 150}],
                    "GI Gandul": [{name: "Bay Trafo 1 Gandul", cap: 500}],
                    "GI Kembangan": [{name: "Bay Trafo 1 Kembangan", cap: 500}]
                }
            },
            "PEMBANGKIT": {
                labelParent: "Unit Pembangkitan",
                labelChild: "Pembangkit",
                parents: ["Unit Pembangkitan Suralaya", "Unit Pembangkitan Paiton"],
                children: {
                    "Unit Pembangkitan Suralaya": [{name: "PLTU Suralaya 1", cap: 400}, {name: "PLTU Suralaya 2", cap: 400}],
                    "Unit Pembangkitan Paiton": [{name: "PLTU Paiton 1", cap: 815}]
                }
            },
            "PENGHANTAR": {
                labelParent: "Data GI",
                labelChild: "Data Bay Line/Penghantar",
                parents: ["GI Cawang", "GI Gandul", "GI Kembangan"],
                children: {
                    "GI Cawang": [{name: "Bay Line Cawang-Priok", cap: 300}, {name: "Bay Line Cawang-Muara Karang", cap: 300}],
                    "GI Gandul": [{name: "Bay Line Gandul-Muara Karang", cap: 300}],
                    "GI Kembangan": [{name: "Bay Line Kembangan-Duri Kosambi", cap: 300}]
                }
            }
        };

        function onJenisKriteriaChange(suffix) {
            const jenis = document.getElementById('jenis-kriteria-' + suffix).value;
            const parentSelect = document.getElementById('parent-' + suffix);
            const kriteriaSelect = document.getElementById('kriteria-' + suffix);
            const kapasitasInput = document.getElementById('kapasitas-' + suffix);
            
            const labelParent = document.getElementById('label-parent-' + suffix);
            const labelChild = document.getElementById('label-child-' + suffix);

            parentSelect.innerHTML = '<option value="" disabled selected>Pilih Data Parent</option>';
            kriteriaSelect.innerHTML = '<option value="" disabled selected>Pilih Kriteria</option>';
            kapasitasInput.value = '';
            
            if (jenis && hierarchyData[jenis]) {
                labelParent.innerHTML = hierarchyData[jenis].labelParent + (suffix === 'n1' ? ' <span style="color:var(--danger)">*</span>' : '');
                labelChild.innerHTML = hierarchyData[jenis].labelChild + (suffix === 'n1' ? ' <span style="color:var(--danger)">*</span>' : '');
                
                hierarchyData[jenis].parents.forEach(item => {
                    const opt = document.createElement("option");
                    opt.value = item;
                    opt.textContent = item;
                    parentSelect.appendChild(opt);
                });
                parentSelect.disabled = false;
                kriteriaSelect.disabled = true;
            } else {
                parentSelect.disabled = true;
                kriteriaSelect.disabled = true;
            }
        }

        function onParentChange(suffix) {
            const jenis = document.getElementById('jenis-kriteria-' + suffix).value;
            const parentVal = document.getElementById('parent-' + suffix).value;
            const kriteriaSelect = document.getElementById('kriteria-' + suffix);
            const kapasitasInput = document.getElementById('kapasitas-' + suffix);
            
            kriteriaSelect.innerHTML = '<option value="" disabled selected>Pilih Kriteria</option>';
            kapasitasInput.value = '';
            
            if (jenis && parentVal && hierarchyData[jenis].children[parentVal]) {
                hierarchyData[jenis].children[parentVal].forEach(item => {
                    const opt = document.createElement("option");
                    opt.value = item.name;
                    opt.textContent = item.name;
                    opt.dataset.kapasitas = item.cap;
                    kriteriaSelect.appendChild(opt);
                });
                kriteriaSelect.disabled = false;
            } else {
                kriteriaSelect.disabled = true;
            }
        }
        
        function onChildChange(suffix) {
            const kriteriaSelect = document.getElementById('kriteria-' + suffix);
            const kapasitasInput = document.getElementById('kapasitas-' + suffix);
            const selectedOption = kriteriaSelect.options[kriteriaSelect.selectedIndex];
            
            if(selectedOption && selectedOption.dataset.kapasitas) {
                kapasitasInput.value = selectedOption.dataset.kapasitas;
            }
        }

"""
content = content[:start_js] + js_replacement + content[end_js:]

# Remove old unused CSS
tabs_css_start = content.find('/* TABS */')
tabs_css_end = content.find('</style>')
if tabs_css_start != -1:
    content = content[:tabs_css_start] + content[tabs_css_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
