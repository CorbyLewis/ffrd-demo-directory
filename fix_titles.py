import os
import re

SKIP_DIRS = {"stylesheets"}

for dirpath, dirnames, filenames in os.walk("docs"):
    # Skip unwanted directories
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    
    folder_name = os.path.basename(dirpath)
    index_path = os.path.join(dirpath, "index.md")

    # Create blank index.md if missing
    if "index.md" not in filenames:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"# {folder_name}\n")
        print(f"Created: {index_path}")
        continue

    # Fix title in existing index.md
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    if re.match(r'^# ', content, re.MULTILINE):
        new_content = re.sub(r'^# .+', f'# {folder_name}', content, count=1, flags=re.MULTILINE)
    else:
        new_content = f"# {folder_name}\n\n" + content

    if new_content != content:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {index_path}")
    else:
        print(f"OK: {index_path}")