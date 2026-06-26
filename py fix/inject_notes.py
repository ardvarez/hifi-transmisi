import os
import re

root_dir = r'C:\KERJAAN\Project\hifi-transmisi'
exclude_dirs = {'.git', '.github', 'py fix', 'hifi-home'}
exclude_files = {'index.html', 'home.html'}

notes_snippet = """
    <!-- NOTES FEATURE (INJECTED) -->
    <style>
      .notes-fab {
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 56px;
        height: 56px;
        background: var(--pln-blue, #0A58CA);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(10, 88, 202, 0.4);
        z-index: 9999;
        transition: all 0.3s;
      }
      .notes-fab:hover {
        transform: scale(1.05);
        background: var(--pln-blue-mid, #0d6efd);
      }
      .notes-panel {
        position: fixed;
        bottom: 90px;
        right: 24px;
        width: 320px;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        z-index: 9998;
        transform: translateY(20px);
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
      }
      .notes-panel.active {
        transform: translateY(0);
        opacity: 1;
        visibility: visible;
      }
      .notes-panel h3 {
        margin: 0 0 12px 0;
        font-family: 'Outfit', sans-serif;
        color: var(--pln-blue, #0A58CA);
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 16px;
      }
      .notes-panel ul {
        margin: 0;
        padding-left: 20px;
        font-size: 13px;
        color: var(--text-secondary, #475569);
        line-height: 1.6;
      }
      .notes-panel li {
        margin-bottom: 8px;
      }
    </style>
    
    <div class="notes-fab" onclick="document.getElementById('notesPanel').classList.toggle('active')">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="12" y1="16" x2="12" y2="12"></line>
        <line x1="12" y1="8" x2="12.01" y2="8"></line>
      </svg>
    </div>
    
    <div class="notes-panel" id="notesPanel">
      <h3>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Notes & Validasi
      </h3>
      <ul>
        <!-- TODO: UPDATE NOTES HERE -->
        <li><strong>Validasi:</strong> Semua field bertanda bintang (*) wajib diisi.</li>
        <li><strong>Rules:</strong> Tulis aturan bisnis halaman ini di sini.</li>
        <li><strong>Info:</strong> Informasi tambahan untuk user.</li>
      </ul>
    </div>
    <!-- END NOTES FEATURE -->
</body>"""

for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
    for f in filenames:
        if f.endswith('.html') and f not in exclude_files:
            file_path = os.path.join(dirpath, f)
            with open(file_path, 'r', encoding='utf-8') as html_file:
                content = html_file.read()
                
            if '<!-- NOTES FEATURE (INJECTED) -->' in content:
                continue # Already injected
                
            # Replace </body> with the snippet
            new_content = re.sub(r'</body>', notes_snippet, content, count=1, flags=re.IGNORECASE)
            
            with open(file_path, 'w', encoding='utf-8') as html_file:
                html_file.write(new_content)
            print(f'Injected notes into: {os.path.relpath(file_path, root_dir)}')
