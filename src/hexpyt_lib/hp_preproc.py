from hexpyt_lib.hp_consts import TranslateState
from hexpyt_lib.hp_include import get_symbols

def try_preproc(ts: TranslateState, extra_paths):
    has_entered = True
    if ts.cur_line.startswith("using"):
        words = ts.cur_line.split(" ")
        if len(words) == 2:
            new_symbol = words[1].split(";")[0]
            ts.type_names.append(new_symbol)
            ts.cur_line = f"#{ts.cur_line[:-1]} This using was taken into account\n"
    if ts.cur_line.startswith("#include"):
        orig_line = f"{ts.cur_line[:-1]} This include was taken into account\n"
        if '"' in ts.cur_line:
            path = ts.cur_line.split('"')[1]
        elif "<" in ts.cur_line:
            path = ts.cur_line.split("<")[1].split(">")[0]
        else:
            raise Exception("Error while parsing #include")
        get_symbols(path, extra_paths, ts)
        path = path.replace(".pat", "")
        path = path.replace(".hexpat", "")
        ts.final_string += orig_line
        ts.final_string += f"from {path.replace('/', '.')} import *\n\n"
    elif ts.cur_line.startswith("#define"):
        orig_line = f"{ts.cur_line[:-1]} This include was (probably) taken into account\n"
        words = ts.cur_line.split(" ")
        const = words[1]
        replacement = " ".join(words[2:])
        ts.defines.append((const, replacement))
        ts.final_string += orig_line
    else:
        has_entered = False
    
    return has_entered