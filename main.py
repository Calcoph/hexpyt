from operator import truediv
import os
import sys
from typing import List, Tuple
import primitives

macos = "MacOs"
other = "Other"
if sys.platform.startswith("win32"):
    include_path = os.path.expandvars("%localappdata%/imhex/includes/")
    include_path2 = os.path.expandvars("%programfiles%/imhex/includes/")
elif sys.platform.startswith("darwin"):
    include_path = macos
    include_path2 = macos
else:
    include_path = other
    include_path2 = other

plain_text = "PlainText_thisisalongnameonpurposesonobodywoulduseitonaccident"

def make_struct(name: str, attributes: List[Tuple[str, str, int, int]], docstring: str, indentation):
    string = f"""\
class {name}(Struct):
{indentation}\"\"\"
hexpat definition:
```hexpat
{docstring}
```\"\"\"
{indentation}def __init__(self, name: str=""):
{indentation}{indentation}\"\"\"
{indentation}{indentation}struct

{indentation}{indentation}Args:
{indentation}{indentation}{indentation}name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
{indentation}{indentation}\"\"\"
{indentation}{indentation}super().__init__(name)

{indentation}def __matmul__(self, _dollar___offset):
{indentation}{indentation}if not isinstance(_dollar___offset, Dollar):
{indentation}{indentation}{indentation}raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {{type(_dollar___offset)}} was used instead')
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()
"""
    for (class_name, att_name, array_length, indentation_count) in attributes:
        current_indentation = ""
        for i in range(0, indentation_count):
            current_indentation += f"{indentation}"
        string += f"{indentation}{indentation}{current_indentation}"
        if class_name == "float":
            class_name = "Float"
        elif class_name == "bool":
            class_name = "Bool"

        if class_name == "Padding":
            string += f"self.{att_name}: {class_name} = {class_name}({array_length}, '{att_name}') @ _dollar___offset\n"
        elif class_name == plain_text:
            if len(att_name) > 0:
                if att_name[-1] != "\n":
                    att_name = att_name + "\n"
                string += att_name
            else:
                indent_len = len(f"{indentation}{indentation}{current_indentation}")
                string = string[:-indent_len]
        else:
            if array_length == 0:
                string += f"{att_name}: {class_name} = {class_name}('{att_name}') @ _dollar___offset\n"
                string += f"{indentation}{indentation}{current_indentation}"
                string += f"self.{att_name} = {att_name}\n"
            else:
                string += f"{att_name}: Array[{class_name}] = Array({class_name}, {array_length}) @ _dollar___offset\n"
                string += f"{indentation}{indentation}{current_indentation}"
                string += f"self.{att_name} = {att_name}\n"

    string += f"\n{indentation}{indentation}"
    string += "super().init_struct(_dollar___offset_copy, _dollar___offset.copy())\n"
    string += f"{indentation}{indentation}"
    string += "return self\n"
    return string

def make_bitfield(name: str, attributes: List[Tuple[str, int]], docstring: str, indentation):
    string = f"""\
class {name}(BitField):
{indentation}\"\"\"
hexpat definition:
```hexpat
{docstring}
```\"\"\"
{indentation}def __init__(self, name: str=""):
{indentation}{indentation}\"\"\"
{indentation}{indentation}bitfield

{indentation}{indentation}Args:
{indentation}{indentation}{indentation}name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
{indentation}{indentation}\"\"\"

{indentation}{indentation}super().__init__(name)

{indentation}def __matmul__(self, _dollar___offset):
{indentation}{indentation}if not isinstance(_dollar___offset, Dollar):
{indentation}{indentation}{indentation}raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {{type(_dollar___offset)}} was used instead')
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()
{indentation}{indentation}cur_byte = _dollar___offset.read(1)[0]
"""
    size = 0
    for name, b_size in attributes:
        if name == plain_text:
            string += f"{indentation}{indentation}{b_size}\n"
        else:
            while size >= 8:
                string += f"{indentation}{indentation}cur_byte = _dollar___offset.read(1)[0]\n"
                size -= 8
            string += f"{indentation}{indentation}"
            prev_size = size
            size = prev_size + b_size
            bits_read = 0
            if size > 8:
                string += f"self.{name}: int = 0\n"
                bits_to_read = 0
                while size >= 8:
                    last_bits_to_read = bits_to_read
                    bits_to_read = 8-prev_size
                    if last_bits_to_read == 8:
                        string += f"{indentation}{indentation}"
                        string += f"self.{name} <<= 8\n"
                    elif last_bits_to_read == 0:
                        string += f"{indentation}{indentation}"
                        string += f"self.{name} += (cur_byte >> 8-{bits_to_read}) & self._bit_field___masks_dict[{bits_to_read}]\n"
                    else:
                        string += f"{indentation}{indentation}"
                        string += f"{name} = (cur_byte >> {prev_size}) & self._bit_field___masks_dict[{b_size}]\n"
                        string += f"{indentation}{indentation}"
                        string += f"self.{name} += {name} << {last_bits_to_read}\n"
                    prev_size = 0
                    b_size -= bits_to_read
                    if b_size > 0:
                        string += f"{indentation}{indentation}"
                        string += f"cur_byte = _dollar___offset.read(1)[0]\n"
                    size -= 8
                    bits_read += bits_to_read
                if b_size > 0:
                    if bits_read % 8 == 0:
                        string += f"{indentation}{indentation}"
                        string += f"self.{name} += (cur_byte >> {prev_size%8}) & self._bit_field___masks_dict[{b_size}]\n"
                    else:
                        string += f"{indentation}{indentation}"
                        string += f"{name} = (cur_byte >> {prev_size%8}) & self._bit_field___masks_dict[{b_size}]\n"
                        string += f"{indentation}{indentation}"
                        string += f"self.{name} += {name} << {bits_read%8}\n"
            else:
                string += f"self.{name}: int = (cur_byte >>{prev_size%8}) & self._bit_field___masks_dict[{b_size}]\n"

    string += f"{indentation}{indentation}"
    string += "super().init_struct(_dollar___offset_copy, _dollar___offset.copy())\n"
    string += f"{indentation}{indentation}"
    string += "return self\n"
    return string

def get_path(rel_path: str, extra_paths: List[str]):
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
    extra_paths.append(include_path)
    extra_paths.append(include_path2)
    found = False
    for e_path in extra_paths:
        path = e_path+rel_path
        file = path.split("/")[-1]
        folder = "/".join(path.split("/")[:-1])
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
Paths searched:
    * {include_path}
    * {include_path2}
""")

    return path

def get_symbols(rel_path, extra_paths: List[str]):
    path = get_path(rel_path, extra_paths)
    with open(path, "r") as f:
        lines = f.readlines()

    new_symbols = []
    struct_name = ""
    bitfield_name = ""
    for line in lines:
        if struct_name == "" and bitfield_name == "":
            words = line.split(" ")
            if words[0] == "struct":
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

        elif struct_name != "":
            if line[0] == "}":
                struct_name = ""

        elif bitfield_name != "":
            if line[0] == "}":
                bitfield_name = ""

    return new_symbols

def remove_namespaces(lines: List[str]) -> List[str]:
    final_lines = []
    namespace_lines = []
    in_namespace = False
    opening_brackets = None
    indentation_length = None
    for line in lines:
        if "namespace" in line:
            in_namespace = True
            if "{" in line:
                opening_brackets = 1
            else:
                opening_brackets = None
        else:
            if in_namespace:
                if "}" in line:
                    opening_brackets -= 1
                    if opening_brackets == 0:
                        line = line.replace("}", "")
                        if len(line) > indentation_length:
                            namespace_lines.append(line[indentation_length:])
                        else:
                            namespace_lines.append(line)
                        in_namespace = False
                        opening_brackets = None
                        indentation_length = None
                        final_lines.extend(remove_namespaces(namespace_lines))
                        namespace_lines = []
                    else:
                        if len(line) > indentation_length:
                            namespace_lines.append(line[indentation_length:])
                        else:
                            namespace_lines.append(line)
                else:
                    if opening_brackets is None:
                        if "{" in line:
                            opening_brackets = 0
                    if opening_brackets is None:
                        continue
                    if "{" in line:
                        opening_brackets += 1
                    if indentation_length is None:
                        i = 0
                        found = False
                        while line[i] != "\n" and not found:
                            if line[i] != " " and line[i] != "\t":
                                found = True
                            else:
                                i += 1
                        if found:
                            indentation_length = i
                    if indentation_length is None:
                        continue
                    if len(line) > indentation_length:
                        namespace_lines.append(line[indentation_length:])
                    else:
                        namespace_lines.append(line)
            else:
                final_lines.append(line)

    return final_lines

def translate_lines(lines: List[str], indentation: str="    ", extra_paths: List[str]=[]) -> str:
    lines = remove_namespaces(lines)
    padding_count = 0
    final_string = "from primitives import Dollar, Struct, BitField, "
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
    struct_name = ""
    bitfield_name = ""
    function_name = ""
    docstring = ""
    type_names = primitives.struct_names
    current_attribs = []
    attribs = []
    indentation_count = 0
    opening_brackets = 0
    defines = [("std::print", "print"), ("$", "_dollar___offset"), ("//", "#"), ("else if", "elif"), ("::", ".")]
    for line in lines:
        for (const, replacement) in defines:
            line = line.replace(const, replacement)
        if struct_name == "" and bitfield_name == "" and function_name == "":
            if line.startswith("#include"):
                orig_line = line
                if '"' in line:
                    path = line.split('"')[1]
                elif "<" in line:
                    path = line.split("<")[1].split(">")[0]
                else:
                    raise Exception("Error while parsing #include")
                type_names.extend(get_symbols(path, extra_paths))
                path = path.replace(".pat", "")
                path = path.replace(".hexpat", "")
                final_string += orig_line
                final_string += f"from {path.replace('/', '.')} import *\n\n"
            elif line.startswith("#define"):
                orig_line = line
                words = line.split(" ")
                const = words[1]
                replacement = " ".join(words[2:])
                defines.append((const, replacement))
                final_string += orig_line
            else:
                words = line.lstrip().split(" ")
                if words[0] == "struct":
                    docstring = line
                    final_string += "\n"
                    struct_name = list(words[1])
                    if struct_name[-1] == "\n":
                        struct_name = struct_name[:-1]
                    if struct_name[-1] == "{":
                        struct_name = struct_name[:-1]
                    struct_name = "".join(struct_name)
                    type_names.append(struct_name)
                elif words[0] == "bitfield":
                    docstring = line
                    final_string += "\n"
                    bitfield_name = list(words[1])
                    if bitfield_name[-1] == "\n":
                        bitfield_name = bitfield_name[:-1]
                    if bitfield_name[-1] == "{":
                        bitfield_name = bitfield_name[:-1]
                    bitfield_name = "".join(bitfield_name)
                    type_names.append(bitfield_name)
                elif words[0] == "fn":
                    function_name == ""
                    function_name = words[1].split("(")[0].rstrip()
                    opening_brackets = 1
                else:
                    if "}" in line:
                        indentation_count -= 1
                        line = line.replace("}", "")
                    cur_indent = indentation_count
                    line += "\n"
                    if "{" in line:
                        indentation_count += 1
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
                    final_string += line

        elif struct_name != "":
            docstring += line
            if line[0] == "}":
                final_string += make_struct(struct_name, attribs, docstring, indentation)
                attribs = []
                current_attribs = []
                struct_name = ""
                docstring = ""
            else:
                line = line.lstrip()
                line = line.rstrip()
                line = line.split(";")[0]
                line = line.replace("$", "_dollar___offset")
                words = line.split(" ")
                try_padding = words[0].split("[")
                if try_padding[0] == "padding":
                    length = try_padding[1]
                    i = 2
                    while "]" not in try_padding[1]:
                        length += words[i]
                        i += 1
                    length = length.split("]")[0]
                    length = f"{length}"
                    pad_name = f"padding_{padding_count}"
                    padding_count += 1
                    attribs.append(("Padding", pad_name, length, indentation_count))
                elif words[0] in type_names:
                    class_name = words[0]
                    att_name = words[1]
                    if "[" in att_name:
                        (att_name, length) = att_name.split("[")
                        i = 2
                        while "]" not in length:
                            length += " " + words[i]
                            i += 1
                        length = length.split("]")[0]
                        length = f"{length}"
                        attribs.append((class_name, att_name, length, indentation_count))
                        current_attribs.append(att_name)
                    else:
                        attribs.append((class_name, att_name, 0, indentation_count))
                        current_attribs.append(att_name)
                else:
                    if "}" in line:
                        indentation_count -= 1
                        line = line.replace("}", "")
                    cur_indent = indentation_count
                    line += "\n"
                    if "{" in line:
                        indentation_count += 1
                        line = line.replace(" {", ":")
                        line = line.replace("{", ":")
                    line = line.lstrip()
                    attribs.append((plain_text,
                                    line,
                                    0,
                                    cur_indent
                                ))

        elif bitfield_name != "":
            docstring += line
            if line.lstrip()[0] == "}":
                final_string += make_bitfield(bitfield_name, attribs, docstring, indentation)
                attribs = []
                current_attribs = []
                bitfield_name = ""
                docstring = ""
            else:
                line = line.lstrip()
                line = line.rstrip()
                line = line.split(";")[0]
                if "//" in line:
                    line = line.replace("//", "#")
                    attribs.append((plain_text, line))
                else:
                    words = line.split(": ")
                    attribs.append((words[0], int(words[1])))

        elif function_name != "":
            for char in line:
                if char == "{":
                    opening_brackets += 1
                elif char == "}":
                    opening_brackets -= 1
            
            if opening_brackets == 0:
                function_name = ""

    return final_string

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