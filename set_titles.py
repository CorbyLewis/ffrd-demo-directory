import os

for dirpath, dirnames, filenames in os.walk("docs"):
    pages_file = os.path.join(dirpath, ".pages")
    folder_name = os.path.basename(dirpath)
    if os.path.exists(pages_file):
        with open(pages_file, "r") as f:
            lines = f.readlines()
        with open(pages_file, "w") as f:
            found = False
            for line in lines:
                if line.startswith("title:"):
                    f.write(f"title: {folder_name}\n")
                    found = True
                else:
                    f.write(line)
            if not found:
                f.write(f"title: {folder_name}\n")
    else:
        with open(pages_file, "w") as f:
            f.write(f"title: {folder_name}\n")