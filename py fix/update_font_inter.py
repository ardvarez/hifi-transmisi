import os
import glob
import re

target_dir = r"c:\KERJAAN\Project\hifi-transmisi"

html_files = glob.glob(os.path.join(target_dir, "**", "*.html"), recursive=True)

print(f"Found {len(html_files)} HTML files in workspace.")

for filepath in html_files:
    if ".system_generated" in filepath or ".git" in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace font-family declarations containing Plus Jakarta Sans
    content = re.sub(r"font-family:\s*'Plus Jakarta Sans'[^;]+;", "font-family: 'Inter', sans-serif;", content)
    content = re.sub(r"font-family:\s*['\"]Plus Jakarta Sans['\"][^;]+;", "font-family: 'Inter', sans-serif;", content)
    
    # Replace Google Fonts link if it has Plus Jakarta Sans
    content = re.sub(
        r'https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans:[^"\'&]+(&family=Inter:[^"\'&]+)?&display=swap',
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap',
        content
    )
    content = re.sub(
        r'https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans:[^"\'&]+',
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated font to Inter in: {os.path.relpath(filepath, target_dir)}")

print("Done updating fonts.")
