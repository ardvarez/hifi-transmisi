import os
import glob

root_dir = r"c:\KERJAAN\Project\hifi-ers"

files = glob.glob(os.path.join(root_dir, "**/*.html"), recursive=True)
changed = 0

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        continue
        
    if "core-theme.css" in content:
        lines = content.split('\n')
        new_lines = []
        for l in lines:
            if "<!-- Core Theme injected by frontend-design refactor -->" in l:
                continue
            if "core-theme.css" in l and "<link" in l:
                continue
            new_lines.append(l)
            
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"Fixed {filepath}")
            changed += 1
        except Exception as e:
            print(f"Could not write {filepath}: {e}")

print(f"Total fixed: {changed}")
