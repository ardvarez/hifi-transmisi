import os
import re

source = r'c:\KERJAAN\Project\hifi-ers\inject_premium_css.py'
target = r'c:\KERJAAN\Project\hifi-ers\hifi-new-pst\master-unit-level-5.html'

with open(source, 'r', encoding='utf-8') as f:
    source_content = f.read()

# Extract css_content from inject_premium_css.py
css_content = ''
if 'css_content = """<style>' in source_content:
    parts = source_content.split('css_content = """')
    css_content = parts[1].split('"""')[0]
else:
    print('Failed to extract css')
    exit(1)

with open(target, 'r', encoding='utf-8') as f:
    target_content = f.read()

new_content = re.sub(r'(?is)<style.*?>.*?</style>', css_content, target_content, count=1)

with open(target, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated successfully')
