from pathlib import Path

md_path = "ddd/docs/README.md"
md_path_obj = Path(md_path)

print(md_path_obj.name)    # README.md
print(md_path_obj.stem)    # README
print(md_path_obj)  # .md