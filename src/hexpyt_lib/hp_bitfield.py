from typing import Tuple

from hexpyt_lib.hp_consts import *

def make_bitfield(name: str, attributes: list[Tuple[str, int]], docstring: str, indentation):
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
{indentation}{indentation}if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
{indentation}{indentation}{indentation}raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {{type(_dollar___offset)}} was used instead')
{indentation}{indentation}if isinstance(_dollar___offset, IntStruct):
{indentation}{indentation}{indentation}_dollar___offset = _dollar___offset.to_dollar()
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()
"""
    total_size = 0
    for name, b_size in attributes:
        if name != plain_text:
            total_size += b_size
    total_bytes = total_size//8
    padding = total_size % 8
    if padding > 0:
        total_bytes += 1
    string += f"{indentation}{indentation}"
    string += f"_read__able____bytes: bytes = _dollar___offset.read({total_bytes})\n"
    
    bits_read = 0
    for name, b_size in reversed(attributes):
        if name == plain_text:
            string += f"{indentation}{indentation}{b_size}\n"
            continue
        if bits_read == 8:
            string += f"{indentation}{indentation}"
            string += f"_read__able____bytes = _read__able____bytes[1:]\n"
            bits_read = 0
        if b_size > 8 or b_size+bits_read > 8:
            string += f"{indentation}{indentation}"
            string += f"{name} = 0\n"
            bit_shift = 0
            while b_size > 8 or b_size+bits_read > 8:
                bits_to_read = 8-bits_read
                string += f"{indentation}{indentation}"
                string += f"{name} += ((_read__able____bytes[0] >> {bits_read}) & self._bit_field___masks_dict[{bits_to_read}]) << {bit_shift}\n"
                string += f"{indentation}{indentation}"
                string += f"_read__able____bytes = _read__able____bytes[1:]\n"
                bits_read = 0
                b_size -= bits_to_read
                bit_shift += bits_to_read
            if b_size > 0:
                string += f"{indentation}{indentation}"
                string += f"{name} += (_read__able____bytes[0] & self._bit_field___masks_dict[{b_size}]) << {bit_shift}\n"
                bits_read = b_size
            else:
                string += f"{indentation}{indentation}"
                string += f"{name} >>= 8\n"
            string += f"{indentation}{indentation}"
            string += f"self.{name} = {name}\n"
        else:
            string += f"{indentation}{indentation}"
            string += f"self.{name} = (_read__able____bytes[0] >> {bits_read}) & self._bit_field___masks_dict[{b_size}]\n"
            bits_read += b_size

    string += f"{indentation}{indentation}"
    string += "super().init_struct(_dollar___offset_copy, _dollar___offset.copy())\n"
    string += f"{indentation}{indentation}"
    string += "return self\n"
    return string

def translate_bitfield(ts: TranslateState):
    ts.docstring += ts.old_line
    if ts.cur_line.lstrip()[0] == "}":
        ts.final_string += make_bitfield(ts.bitfield_name, ts.attribs, ts.docstring, ts.indentation)
        ts.attribs = []
        ts.current_attribs = []
        ts.bitfield_name = ""
        ts.docstring = ""
    else:
        ts.cur_line = ts.cur_line.lstrip()
        ts.cur_line = ts.cur_line.rstrip()
        ts.cur_line = ts.cur_line.split(";")[0]
        if "#" in ts.cur_line:
            ts.attribs.append((plain_text, ts.cur_line))
        else:
            words = ts.cur_line.split(": ")
            ts.attribs.append((words[0], int(words[1])))