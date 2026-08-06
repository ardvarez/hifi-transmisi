import time
import os
import re
import html
import json
import xml.etree.ElementTree as ET

drawio_path = r"C:\KERJAAN\Project\hifi-transmisi\flow_req\power-inspect\probis-new-pi.drawio"
html_path = r"C:\KERJAAN\Project\hifi-transmisi\flow_req\power-inspect\probis-new-pi.html"

print("👀 Draw.io Auto-Watcher Started...")
print(f"Watching: {drawio_path}")
print(f"Target:   {html_path}")
print("Setiap kali Anda mengedit dan menyimpan file .drawio, probis-new-pi.html akan ter-update otomatis!\n")

last_mtime = 0

def update_html():
    if not os.path.exists(drawio_path):
        return
    with open(drawio_path, 'r', encoding='utf-8') as f:
        raw_xml = f.read()
        
    if not raw_xml.strip():
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    match = re.search(r'data-mxgraph="([^"]+)"', html_content)
    if match:
        old_raw_attr = match.group(0)
        mx_data = html.unescape(match.group(1))
        data_json = json.loads(mx_data)
        data_json['xml'] = raw_xml
        
        new_mx_data = html.escape(json.dumps(data_json))
        new_raw_attr = f'data-mxgraph="{new_mx_data}"'
        
        new_html = html_content.replace(old_raw_attr, new_raw_attr)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        print(f"[{time.strftime('%H:%M:%S')}] ⚡ Auto-updated probis-new-pi.html from probis-new-pi.drawio!")

while True:
    try:
        if os.path.exists(drawio_path):
            mtime = os.path.getmtime(drawio_path)
            if mtime != last_mtime:
                last_mtime = mtime
                update_html()
        time.sleep(2)
    except KeyboardInterrupt:
        print("Watcher stopped.")
        break
    except Exception as e:
        print("Watcher error:", e)
        time.sleep(2)
