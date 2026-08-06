import urllib.request
import json
import html
import os
import sys

# Ensure UTF-8 output in Windows terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# File paths relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(SCRIPT_DIR, "probis-new-pi.html")

file_id = '1k6WaYj9Tijt6J2G2TqxNyAQWrokyXAqo'
gdrive_url = f'https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t'

print("[SYNC] Syncing latest diagram XML from Google Drive (Draw.io)...")
print(f"[PATH] Target file: {html_file}")

req = urllib.request.Request(gdrive_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"[SUCCESS] Downloaded {len(content):,} bytes from Google Drive.")

    if "<mxfile" not in content:
        print("[ERROR] Response does not contain valid <mxfile> XML!")
        exit(1)

    # Read current HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Update data-mxgraph attribute using direct string replacement
    mx_data_struct = {"highlight": "#0000ff", "nav": True, "resize": True, "toolbar": "zoom layers tags page", "xml": content}
    json_str = json.dumps(mx_data_struct)
    escaped_attr = html.escape(json_str)

    start_token = 'data-mxgraph="'
    end_token = '"'
    idx_start = html_content.find(start_token)
    if idx_start != -1:
        idx_end = html_content.find(end_token, idx_start + len(start_token))
        if idx_end != -1:
            html_content = html_content[:idx_start + len(start_token)] + escaped_attr + html_content[idx_end:]

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("[DONE] probis-new-pi.html has been updated with the latest Draw.io diagram!")
    print("Silakan refresh browser Anda untuk melihat diagram terbaru.")

except Exception as e:
    print(f"[ERROR] Sync failed: {e}")
