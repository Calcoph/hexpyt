from typing import Tuple
from hexpyt_lib.hp_consts import *

def make_struct(name: str, attributes: list[Tuple[str, str, int, int]], docstring: str, indentation):
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
{indentation}{indentation}if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
{indentation}{indentation}{indentation}raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {{type(_dollar___offset)}} was used instead')
{indentation}{indentation}if isinstance(_dollar___offset, IntStruct):
{indentation}{indentation}{indentation}_dollar___offset = _dollar___offset.to_dollar()
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
                if "while" in array_length:
                    array_length = f'"{array_length}"'
                string += f"{att_name}: Array[{class_name}] = Array({class_name}, {array_length}) @ _dollar___offset\n"
                string += f"{indentation}{indentation}{current_indentation}"
                string += f"self.{att_name} = {att_name}\n"

    string += f"\n{indentation}{indentation}"
    string += "super().init_struct(_dollar___offset_copy, _dollar___offset.copy())\n"
    string += f"{indentation}{indentation}"
    string += "return self\n"
    return string

def translate_struct(ts: TranslateState):
    ts.docstring += ts.old_line
    if ts.cur_line[0] == "}":
        ts.final_string += make_struct(ts.struct_name, ts.attribs, ts.docstring, ts.indentation)
        ts.attribs = []
        ts.current_attribs = []
        ts.struct_name = ""
        ts.docstring = ""
    else:
        ts.cur_line = ts.cur_line.lstrip()
        ts.cur_line = ts.cur_line.rstrip()
        ts.cur_line = ts.cur_line.split(";")[0]
        words = ts.cur_line.split(" ")
        try_padding = words[0].split("[")
        if try_padding[0] == "padding":
            length = try_padding[1]
            i = 2
            while "]" not in try_padding[1]:
                length += words[i]
                i += 1
            length = length.split("]")[0]
            length = f"{length}"
            pad_name = f"padding_{ts.padding_count}"
            ts.padding_count += 1
            ts.attribs.append(("Padding", pad_name, length, ts.indentation_count))
        elif words[0] in ts.type_names:
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
                ts.attribs.append((class_name, att_name, length, ts.indentation_count))
                ts.current_attribs.append(att_name)
            else:
                ts.attribs.append((class_name, att_name, 0, ts.indentation_count))
                ts.current_attribs.append(att_name)
        else:
            print(ts.cur_line)
            if "}" in ts.cur_line:
                ts.indentation_count -= 1
                ts.cur_line = ts.cur_line.replace("}", "")
            cur_indent = ts.indentation_count
            ts.cur_line += "\n"
            if "{" in ts.cur_line:
                print(ts.cur_line)
                ts.indentation_count += 1
                ts.cur_line = ts.cur_line.replace(" {", ":")
                ts.cur_line = ts.cur_line.replace("{", ":")
            ts.cur_line = ts.cur_line.lstrip()
            print(cur_indent)
            ts.attribs.append((plain_text,
                            ts.cur_line,
                            0,
                            cur_indent
                        ))