from typing import List, Tuple

from hexpyt_lib.hp_namespace import remove_namespaces
from hexpyt_lib.hp_struct import translate_struct
from hexpyt_lib.hp_bitfield import translate_bitfield
from src.hexpyt_lib.hp_consts import *
from src.hexpyt_lib.hp_preproc import try_preproc

def get_header() -> str:
    final_string = "from primitives import Dollar, Struct, BitField, IntStruct, "
    final_string += "u8, u16, u24, u32, u48, u64, u96, u128, "
    final_string += "s8, s16, s24, s32, s48, s64, s96, s128, "
    final_string += "Float, double, char, char16, Bool, "
    final_string += "Padding, Array, sizeof, addressof\n"
    final_string += """
# Template to read from a file. follow the instructions.
# _dollar___offset has this name so it doesn't clash with others. Feel free to rename it. 
if True: # Change this from "if True" to "if False", then put the file path below.
    byts = b''
else:
    file_path = "" # Put the file path here and change the above "if True" to "if False".
    with open(file_path, "rb") as f:
        byts = f.read()
_dollar___offset = Dollar(0x00, byts)
# End of template
"""
    return final_string

def translate_lines(lines: List[str], indentation: str="    ", extra_paths: List[str]=[]) -> str:
    lines = remove_namespaces(lines)
    padding_count = 0
    header = get_header()
    ts = TranslateState(header, indentation)
    for line in lines:
        ts.old_line = line
        for (const, replacement) in ts.defines:
            line = line.replace(const, replacement)
        if ts.struct_name == "" and ts.bitfield_name == "" and ts.function_name == "":
            if not try_preproc(ts, extra_paths):
                words = line.lstrip().split(" ")
                if words[0] == "struct":
                    ts.docstring = ts.old_line
                    ts.final_string += "\n"
                    ts.struct_name = list(words[1])
                    if ts.struct_name[-1] == "\n":
                        ts.struct_name = ts.struct_name[:-1]
                    if ts.struct_name[-1] == "{":
                        ts.struct_name = ts.struct_name[:-1]
                    ts.struct_name = "".join(ts.struct_name)
                    ts.type_names.append(ts.struct_name)
                elif words[0] == "bitfield":
                    ts.docstring = ts.old_line
                    ts.final_string += "\n"
                    ts.bitfield_name = list(words[1])
                    if ts.bitfield_name[-1] == "\n":
                        ts.bitfield_name = ts.bitfield_name[:-1]
                    if ts.bitfield_name[-1] == "{":
                        ts.bitfield_name = ts.bitfield_name[:-1]
                    ts.bitfield_name = "".join(ts.bitfield_name)
                    ts.type_names.append(ts.bitfield_name)
                elif words[0] == "fn":
                    ts.function_name == ""
                    ts.function_name = words[1].split("(")[0].rstrip()
                    ts.opening_brackets = 1
                else:
                    if line.lstrip().startswith("#"):
                        for _ in range(0, cur_indent):
                            line = indentation + line
                        ts.final_string += line
                        continue
                    if "}" in line:
                        ts.indentation_count -= 1
                        line = line.replace("}", "")
                    cur_indent = ts.indentation_count
                    line += "\n"
                    if "{" in line:
                        ts.indentation_count += 1
                        line = line.replace(" {", ":")
                        line = line.replace("{", ":")
                    line = line.lstrip()
                    if "@" in line:
                        line = line.split("@")
                        words = line[0].split(" ")
                        type_name = words[0]
                        new_var = words[1]
                        expression = ''.join(line[1:]).lstrip().rstrip().replace(";", "")
                        line = f"{new_var}: {type_name} = {type_name}() @ ({expression})\n"
                    for _ in range(0, cur_indent):
                        line = indentation + line
                    ts.final_string += line

        elif ts.struct_name != "":
            translate_struct(ts)

        elif ts.bitfield_name != "":
            translate_bitfield(ts)

        elif ts.function_name != "":
            for char in line:
                if char == "{":
                    ts.opening_brackets += 1
                elif char == "}":
                    ts.opening_brackets -= 1
            
            if ts.opening_brackets == 0:
                ts.function_name = ""

    return ts.final_string

def translate_text(text: str, indentation: str="    ", extra_paths: List[str]=[]) -> str:
    lines = text.splitlines(keepends=True)
    return translate_lines(lines, indentation, extra_paths)

def translate_text_to_file(text: str, output_file_path: str, indentation: str="    ", extra_paths: List[str]=[]):
    lines = text.splitlines(keepends=True)
    ts.final_string = translate_lines(lines, indentation, extra_paths)
    with open(output_file_path, "w") as f:
        f.write(ts.final_string)

def translate_file(input_file_path: str, output_file_path: str, indentation: str="    ", extra_paths: List[str]=[]):
    with open(input_file_path, "r") as f:
        lines = f.readlines()

    ts.final_string = translate_lines(lines, indentation, extra_paths)

    with open(output_file_path, "w") as f:
        f.write(ts.final_string)

if __name__ == "__main__":
    input_file_path = ""
    output_file_path = ""

    translate_file(input_file_path, output_file_path)