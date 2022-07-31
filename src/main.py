from typing import List, Tuple

from hexpyt_lib.hp_namespace import remove_namespaces
from hexpyt_lib.hp_struct import translate_struct
from hexpyt_lib.hp_bitfield import translate_bitfield
from hexpyt_lib.hp_consts import *
from hexpyt_lib.hp_enum import translate_enum
from hexpyt_lib.hp_preproc import try_preproc

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

def translate_nameless(ts: TranslateState):
    words = ts.cur_line.lstrip().split(" ")
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
    elif words[0] == "enum":
        ts.docstring = ts.old_line
        ts.final_string += "\n"
        enum_name = "".join(words[1:])
        split = enum_name.split(":")
        enum_type = list(split[1])
        if enum_type[-1] == "\n":
            enum_type = enum_type[:-1]
        if enum_type[-1] == "{":
            enum_type = enum_type[:-1]
        enum_type = "".join(enum_type)
        ts.enum_desc = (split[0], enum_type)
        ts.type_names.append(split[0])
    elif words[0] == "fn":
        ts.function_name == ""
        ts.function_name = words[1].split("(")[0].rstrip()
        ts.opening_brackets = 1
    else:
        if ts.cur_line.lstrip().startswith("#"):
            for _ in range(0, ts.indentation_count):
                ts.cur_line = ts.indentation + ts.cur_line
            ts.final_string += ts.cur_line
        else:
            if "}" in ts.cur_line:
                ts.indentation_count -= 1
                ts.cur_line = ts.cur_line.replace("}", "")
            ts.indentation_count = ts.indentation_count
            ts.cur_line += "\n"
            if "{" in ts.cur_line:
                ts.indentation_count += 1
                ts.cur_line = ts.cur_line.replace(" {", ":")
                ts.cur_line = ts.cur_line.replace("{", ":")
            ts.cur_line = ts.cur_line.lstrip()
            if "@" in ts.cur_line:
                ts.cur_line = ts.cur_line.split("@")
                words = ts.cur_line[0].split(" ")
                type_name = words[0]
                new_var = words[1]
                expression = ''.join(ts.cur_line[1:]).lstrip().rstrip().replace(";", "")
                ts.cur_line = f"{new_var}: {type_name} = {type_name}() @ ({expression})\n"
            for _ in range(0, ts.indentation_count):
                ts.cur_line = ts.indentation + ts.cur_line
            ts.final_string += ts.cur_line

def translate_lines(lines: List[str], indentation: str="    ", extra_paths: List[str]=[]) -> str:
    lines = remove_namespaces(lines)

    header = get_header()
    ts = TranslateState(header, indentation)
    for line in lines:
        ts.cur_line = line
        ts.old_line = ts.cur_line
        for (const, replacement) in ts.defines:
            ts.cur_line = ts.cur_line.replace(const, replacement)
        if ts.struct_name == "" and ts.bitfield_name == "" and ts.function_name == "" and ts.enum_desc == ("", ""):
            if not try_preproc(ts, extra_paths):
                translate_nameless(ts)

        elif ts.struct_name != "":
            translate_struct(ts)

        elif ts.bitfield_name != "":
            translate_bitfield(ts)

        elif ts.enum_desc != ("", ""):
            translate_enum(ts)

        elif ts.function_name != "":
            for char in ts.cur_line:
                if char == "{":
                    ts.opening_brackets += 1
                elif char == "}":
                    ts.opening_brackets -= 1
            
            if ts.opening_brackets == 0:
                ts.function_name = ""

    ts.final_string = ts.final_string.replace("\0", ";")
    return ts.final_string

def translate_text(text: str, indentation: str="    ", extra_paths: List[str]=[]) -> str:
    lines = text.splitlines(keepends=True)
    return translate_lines(lines, indentation, extra_paths)

def translate_text_to_file(text: str, output_file_path: str, indentation: str="    ", extra_paths: List[str]=[]):
    lines = text.splitlines(keepends=True)
    final_string = translate_lines(lines, indentation, extra_paths)
    with open(output_file_path, "w") as f:
        f.write(final_string)

def translate_file(input_file_path: str, output_file_path: str, indentation: str="    ", extra_paths: List[str]=[]):
    with open(input_file_path, "r") as f:
        lines = f.readlines()

    final_string = translate_lines(lines, indentation, extra_paths)

    with open(output_file_path, "w") as f:
        f.write(final_string)

if __name__ == "__main__":
    input_file_path = ""
    output_file_path = ""

    translate_file(input_file_path, output_file_path)