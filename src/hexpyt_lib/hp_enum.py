from typing import Tuple
from hexpyt_lib.hp_consts import *

def parseint(inp: str) -> int:
    if inp[:2].lower() == "0x":
        result = int(inp[2:], 16)
    elif inp[:2].lower() == "0o":
        result = int(inp[2:], 8)
    elif inp[:2].lower() == "0b":
        result = int(inp[2:], 2)
    else:
        result = int(inp, 10)
    
    return result

def make_enum(desc: Tuple[str, str], attributes: list[Tuple[str, str, int, int]], docstring: str, indentation):
    class_ = "Enum"
    if desc[0] in [
        "u8", "u16", "u24", "u32", "u48", "u64", "u96", "u128",
        "s8", "s16", "s24", "s32", "s48", "s64", "s96", "s128",
    ]:
        class_ = "IntEnum"
    elif desc[0] in ["float", "double"]:
        class_ = "RealEnum"
    elif desc[0] in ["char", "char16"]:
        class_ = "CharEnum"
    elif desc[0] == "bool":
        class_ = "BoolEnum"
    string = f"""\
class {desc[0]}({class_}):
{indentation}\"\"\"
hexpat definition:
```hexpat
{docstring}
```\"\"\"
{indentation}_enum__dict___ = {{
"""
    cur_value = 0
    for (this_value, val_name, indentation_count) in attributes:
        current_indentation = ""
        for i in range(0, indentation_count):
            current_indentation += f"{indentation}"
        string += f"{indentation}{indentation}{current_indentation}"

        if this_value == plain_text:
            if len(val_name) > 0:
                if val_name[-1] != "\n":
                    val_name = val_name + "\n"
                string += val_name
            else:
                indent_len = len(f"{indentation}{indentation}{current_indentation}")
                string = string[:-indent_len]
        else:
            if this_value is not None:
                cur_value = parseint(this_value)
            string += f"{cur_value}: '{val_name}',\n"
        cur_value += 1

    string += f"\n{indentation}{indentation}"
    string += f"}}\n"

    cur_value = 0
    for (this_value, val_name, indentation_count) in attributes:
        current_indentation = ""
        for i in range(0, indentation_count):
            current_indentation += f"{indentation}"
        string += f"{indentation}{current_indentation}"

        if this_value == plain_text:
            if len(val_name) > 0:
                if val_name[-1] != "\n":
                    val_name = val_name + "\n"
                string += val_name
            else:
                indent_len = len(f"{indentation}{current_indentation}")
                string = string[:-indent_len]
        else:
            if this_value is not None:
                cur_value = parseint(this_value)
            print(f"{val_name} = {cur_value}\n")
            string += f"{val_name} = {cur_value}\n"
        cur_value += 1
    return string

def translate_enum(ts: TranslateState):
    ts.docstring += ts.old_line
    if ts.cur_line[0] == "}":
        ts.final_string += make_enum(ts.enum_desc, ts.attribs, ts.docstring, ts.indentation)
        ts.attribs = []
        ts.current_attribs = []
        ts.enum_desc = ("", "")
        ts.docstring = ""
    else:
        ts.cur_line: str = ts.cur_line.lstrip()
        ts.cur_line = ts.cur_line.rstrip()
        if ts.cur_line.startswith("//") or len(ts.cur_line) == 0:
            ts.attribs.append((plain_text,
                                ts.cur_line,
                                ts.indentation_count
                            ))
        else:
            ts.cur_line = ts.cur_line.split(",")[0]
            words = ts.cur_line.split(" ")
            if len(words) > 1 and words[1] == "=":
                ts.cur_line = ts.cur_line.lstrip()
                ts.attribs.append((words[2],
                                    words[0],
                                    ts.indentation_count
                                ))
            else:
                ts.cur_line = ts.cur_line.lstrip()
                ts.attribs.append((None,
                                    words[0],
                                    ts.indentation_count
                                ))