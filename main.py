import os

LINE = "Monday installed an update overnight. Changelog: your energy has been removed for your convenience."
MAX_CHARS = 200

if len(LINE) > MAX_CHARS:
    raise ValueError("entry line must be 200 characters or fewer")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
