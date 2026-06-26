import os
import re

root_dir = r'C:\KERJAAN\Project\hifi-transmisi'
home_html_path = os.path.join(root_dir, 'hifi-home', 'home.html')
exclude_dirs = {'.git', '.github', 'py fix', 'hifi-home'}

# 1. Gather all files
tree = {}
for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
    rel_path = os.path.relpath(dirpath, root_dir)
    
    if rel_path == '.': continue # skip root
    
    parts = rel_path.split(os.sep)
    top_level = parts[0]
    
    if top_level not in tree:
        tree[top_level] = {'__files__': [], 'subfolders': {}}
    
    current_level = tree[top_level]
    for p in parts[1:]:
        if p not in current_level['subfolders']:
            current_level['subfolders'][p] = {'__files__': [], 'subfolders': {}}
        current_level = current_level['subfolders'][p]
        
    for f in filenames:
        if f.endswith('.html'):
            current_level['__files__'].append(f)

# 2. Build HTML
html_parts = []

def format_name(name):
    n = name.replace('.html', '').replace('-', ' ').replace('_', ' ')
    if n.lower().startswith('hifi '):
        n = 'HiFi ' + n[5:].upper()
    else:
        n = n.title()
    return n

# max_depth limits how deep the menu can nest.
def build_tree(data, path_parts, depth=1, max_depth=2):
    html = []
    pad = 12 * depth
    
    # Files directly in this folder
    for file in data['__files__']:
        href = '../' + '/'.join(path_parts + [file])
        name = format_name(file)
        if depth == 1:
            html.append(f'                <a href="{href}" class="menu-item" target="contentFrame">')
            html.append(f'                    <div class="menu-item-content">')
            html.append(f'                        <i class="ri-file-list-3-line"></i>')
            html.append(f'                        <span>{name}</span>')
            html.append(f'                    </div>')
            html.append(f'                </a>')
        else:
            html.append(f'                    <a href="{href}" class="submenu-item" target="contentFrame" style="padding-left: {16 + pad}px;">')
            html.append(f'                        <i class="ri-checkbox-blank-circle-line" style="font-size: 8px;"></i> {name}')
            html.append(f'                    </a>')
    
    if depth > max_depth:
        return html
        
    # Subfolders
    for subfolder, subdata in data['subfolders'].items():
        if not subdata['__files__'] and not subdata['subfolders']:
            continue
            
        cls = "menu-item has-submenu" if depth == 1 else "submenu-item has-submenu"
        pl = "" if depth == 1 else f' style="padding-left: {16 + pad}px; display:flex; justify-content:space-between; align-items:center; cursor:pointer; color:var(--text-muted);"'
        
        icon = "ri-folder-2-line" if depth == 1 else "ri-folder-3-line"
        
        html.append(f'                <div class="{cls}" onclick="toggleSubmenu(this)"{pl}>')
        html.append(f'                    <div class="menu-item-content" style="display:flex; align-items:center; gap:12px;">')
        html.append(f'                        <i class="{icon}"></i>')
        html.append(f'                        <span>{format_name(subfolder)}</span>')
        html.append(f'                    </div>')
        html.append(f'                    <i class="ri-arrow-down-s-line chevron-icon"></i>')
        html.append(f'                </div>')
        html.append(f'                <div class="submenu">')
        
        # Recurse
        html.extend(build_tree(subdata, path_parts + [subfolder], depth + 1, max_depth))
        
        html.append(f'                </div>')
        
    return html


for top_level, data in tree.items():
    if not data['__files__'] and not data['subfolders']:
        continue
        
    html_parts.append(f'            <!-- Module: {top_level} -->')
    html_parts.append(f'            <div class="menu-section">')
    html_parts.append(f'                <div class="menu-section-title">{format_name(top_level)}</div>')
    
    html_parts.extend(build_tree(data, [top_level], depth=1, max_depth=2))
    
    html_parts.append(f'            </div>')

new_sidebar_content = '\n'.join(html_parts)

with open(home_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(<div class="sidebar-menu">).*?(</aside>)'
replacement = f'\\g<1>\n{new_sidebar_content}\n        </div>\n    \\g<2>'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(home_html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated recursive sidebar with max depth!")
