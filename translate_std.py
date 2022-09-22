import sys
import os
import main

macos = "MacOs"
other = "Other"
if sys.platform.startswith("win32"):
    include_path = os.path.expandvars("%programfiles%/imhex/includes/std/")
elif sys.platform.startswith("darwin"):
    include_path = macos
else:
    include_path = other

if include_path == macos:
        raise Exception("""
Hexpyt doesn't know where MacOs's imhex std include path is.
To fix it, change line 10 of translate_std.py
    from
        "include_path = macos"
    to
        "include_path = '<The include path goes here>'"
""")
elif include_path == other:
        raise Exception("""
Hexpyt doesn't know where your OS's imhex std include path is.
To fix it, change line 12 of translate_std.py
    from
        "include_path = other"
    to
        "include_path = '<The include path goes here>'"
""")

def translate_std_files(target_dir: str):
    if not (target_dir.endswith("/") or target_dir.endswith("\\")):
        target_dir = target_dir + "/"
    try:
        os.listdir(target_dir)
    except FileNotFoundError:
        os.mkdir(target_dir)

    std = os.listdir(include_path)
    for file in std:
        main.translate_file(include_path+file, target_dir+file.replace(".pat", ".py"))

if __name__ == "__main__":
    translate_std_files("hexpat_std____/")