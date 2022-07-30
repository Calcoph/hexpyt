from src.hexpyt_lib.hp_consts import TranslateState
from src.hexpyt_lib.hp_include import get_symbols

def try_preproc(ts: TranslateState, extra_paths):
    has_entered = True
    if line.startswith("using"):
        words = line.split(" ")
        if len(words) == 2:
            new_symbol = words[1].split(";")[0]
            ts.type_names.append(new_symbol)
            line = f"#{line[:-1]} This using was taken into account\n"
    if line.startswith("#include"):
        orig_line = f"{line[:-1]} This include was taken into account\n"
        if '"' in line:
            path = line.split('"')[1]
        elif "<" in line:
            path = line.split("<")[1].split(">")[0]
        else:
            raise Exception("Error while parsing #include")
        ts.type_names.extend(get_symbols(path, extra_paths))
        path = path.replace(".pat", "")
        path = path.replace(".hexpat", "")
        final_string += orig_line
        final_string += f"from {path.replace('/', '.')} import *\n\n"
    elif line.startswith("#define"):
        orig_line = f"{line[:-1]} This include was (probably) taken into account\n"
        words = line.split(" ")
        const = words[1]
        replacement = " ".join(words[2:])
        ts.defines.append((const, replacement))
        final_string += orig_line
    else:
        has_entered = False
    
    return has_entered