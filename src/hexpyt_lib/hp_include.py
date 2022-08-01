import os
import sys

from hexpyt_lib.hp_consts import TranslateState

macos = "MacOs"
other = "Other"
if sys.platform.startswith("win32"):
    include_path = os.path.expandvars("%localappdata%/imhex/includes/")
    include_path2 = os.path.expandvars("%programfiles%/imhex/includes/")
elif sys.platform.startswith("darwin"):
    include_path = macos
    include_path2 = macos
else:
    include_path = os.path.expanduser("~/.local/share/imhex/includes/")
    include_path2 = "/usr/share/imhex/includes/"

def get_path(rel_path: str, extra_paths: list[str]):
    if include_path == macos and include_path2 == macos and len(extra_paths) == 0:
        raise Exception("""
That script contains an "#include<...>".
Hexpyt doesn't know where MacOs's imhex include path is.
You can fix it in 2 ways.
1. Add the path to the "extra_paths" argument of translate_file
2. Change lines 12-13 of main.py
    from
        "include_path = macos"
    to
        "include_path = '<The include path goes here>'"
""")
    elif include_path == other and include_path2 == other and len(extra_paths) == 0:
        raise Exception("""
That script contains an "#include<...>".
Hexpyt doesn't know where your OS's imhex include path is.
You can fix it in 2 ways.
1. Add the path to the "extra_paths" argument of translate_file
2. Change lines 15-16 of main.py
    from
        "include_path = other"
    to
        "include_path = '<The include path goes here>'"
""")
    searched_paths = ""
    extra_paths.append(include_path)
    extra_paths.append(include_path2)
    found = False
    for e_path in extra_paths:
        if e_path[-1] not in ["/", "\\"]:
            e_path += "/"
        path = e_path+rel_path
        file = path.split("/")[-1]
        folder = "/".join(path.split("/")[:-1])
        searched_paths += f"\n    * {e_path}"
        try:
            if file not in os.listdir(folder):
                continue
            else:
                found = True
                break
        except FileNotFoundError:
            continue
    if not found:
        raise Exception(f"""
{rel_path} not found.
Paths searched:{searched_paths}
""")

    return path

def get_symbols(rel_path, extra_paths: list[str], ts: TranslateState):
    path = get_path(rel_path, extra_paths)
    with open(path, "r") as f:
        lines = f.readlines()

    new_symbols = []
    struct_name = ""
    bitfield_name = ""
    for line in lines:
        if struct_name == "" and bitfield_name == "":
            words = line.split(" ")
            if len(words) == 2 and words[0] == "using":
                new_symbol = words[1].split(";")[0]
                new_symbols.append(new_symbol)
            if words[0] == "#include":
                if '"' in ts.cur_line:
                    path = ts.cur_line.split('"')[1]
                elif "<" in ts.cur_line:
                    path = ts.cur_line.split("<")[1].split(">")[0]
                else:
                    raise Exception("Error while parsing #include")
                get_symbols(path, extra_paths, ts)
            elif words[0] == "#define":
                const = words[1]
                replacement = " ".join(words[2:])
                ts.defines.append((const, replacement))
            elif words[0] == "struct":
                struct_name = list(words[1])
                if struct_name[-1] == "\n":
                    struct_name = struct_name[:-1]
                if struct_name[-1] == "{":
                    struct_name = struct_name[:-1]
                struct_name = "".join(struct_name)
                new_symbols.append(struct_name)
            elif words[0] == "bitfield":
                bitfield_name = list(words[1])
                if bitfield_name[-1] == "\n":
                    bitfield_name = bitfield_name[:-1]
                if bitfield_name[-1] == "{":
                    bitfield_name = bitfield_name[:-1]
                bitfield_name = "".join(bitfield_name)
                new_symbols.append(bitfield_name)
            elif words[0] == "enum":
                enum_name = "".join(words[1:])
                split = enum_name.split(":")
                new_symbols.append(split[0])

    ts.type_names.extend(new_symbols)
