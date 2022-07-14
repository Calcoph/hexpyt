import primitives

plain_text = "PlainText_thisisalongnameonpurposesonobodywoulduseitonaccident"
indentation = "    "

def make_struct(name: str, attributes):
    string = f"""\
class {name}(Struct):
{indentation}def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
{indentation}{indentation}\"\"\"
{indentation}{indentation}struct

{indentation}{indentation}Args:
{indentation}{indentation}{indentation}_thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
{indentation}{indentation}{indentation}_dollar___offset (Dollar): Dollar pointing to the start of this struct
{indentation}{indentation}\"\"\"
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()\n"""
    for (class_name, att_name, array_length) in attributes:
        string += f"{indentation}{indentation}"
        if class_name == "float":
            class_name = "Float"
        elif class_name == "bool":
            class_name = "Bool"

        if class_name == "Padding":
            string += f"self.{att_name}: {class_name} = {class_name}('{att_name}', _dollar___offset, {array_length})\n"
        elif class_name == plain_text:
            string += att_name
        else:
            if array_length == 0:
                string += f"{att_name}: {class_name} = {class_name}('{att_name}', _dollar___offset)\n"
                string += f"{indentation}{indentation}"
                string += f"self.{att_name} = {att_name}\n"
            else:
                string += f"self.{att_name}: list[{class_name}] = []\n"
                string += f"{indentation}{indentation}"
                string += f"for i in range(0,{array_length}):\n"
                string += f"{indentation}{indentation}{indentation}"
                string += f"self.{att_name}.append({class_name}(f'{att_name}_{{i}}', _dollar___offset))\n"

    string += f"{indentation}{indentation}"
    string += "super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())\n"
    return string

"""bitfield Params {
	unknown: 4;
	width: 3;
	height: 3;
	format: 3;
	cPalette_id: 1;
	unknown: 2;
};"""

def make_bitfield(name: str, attributes):
    string = f"""\
class {name}(BitField):
{indentation}def __init__(self, _thisbitfield_s_name: str, _dollar___offset: Dollar):
{indentation}{indentation}\"\"\"
{indentation}{indentation}bitfield

{indentation}{indentation}Args:
{indentation}{indentation}{indentation}_thisbitfield_s_name (str): The name of this instance. Can be whatever you want or just an empty string
{indentation}{indentation}{indentation}_dollar___offset (Dollar): Dollar pointing to the start of this bitfield
{indentation}{indentation}\"\"\"
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()
{indentation}{indentation}cur_byte = _dollar___offset.read(1)[0]\n"""
    size = 0
    for name, b_size in attributes:
        while size >= 8:
            string += f"{indentation}{indentation}cur_byte = _dollar___offset.read(1)[0]\n"
            size -= 8
        string += f"{indentation}{indentation}"
        prev_size = size
        size = prev_size + b_size
        if size > 8:
            string += f"self.{name}: int = 0\n"
            while size >= 8:
                bits_to_read = 8-prev_size
                string += f"{indentation}{indentation}"
                string += f"self.{name} += cur_byte & self._bit_field___masks_dict[{bits_to_read}]\n"
                prev_size = 0
                b_size -= bits_to_read
                if b_size > 0:
                    string += f"{indentation}{indentation}"
                    string += f"self.{name} <<= {b_size%8}\n"
                    string += f"{indentation}{indentation}"
                    string += f"cur_byte = _dollar___offset.read(1)[0]\n"
                size -= 8
            if b_size > 0:
                string += f"{indentation}{indentation}"
                string += f"self.{name} += (cur_byte >> 8-{size}) & self._bit_field___masks_dict[{b_size}]\n"
        else:
            string += f"self.{name}: int = (cur_byte >> 8-{size}) & self._bit_field___masks_dict[{b_size}]\n"

    string += f"{indentation}{indentation}"
    string += "super().__init__(_thisbitfield_s_name, _dollar___offset_copy, _dollar___offset.copy())\n"
    return string

with open("ignore/testpath.txt", "r") as f:
    file_path = f.readlines()[0]

with open(file_path, "r") as f:
    lines = f.readlines()

padding_count = 0
final_string = "from primitives import Dollar, Struct, u8, u16, u32, u64, u128, s8, s16, s32, s64, s128, Float, double, char, char16, Bool, Padding, BitField, sizeof, addressof\n\n"
struct_name = ""
bitfield_name = ""
type_names = primitives.struct_names
current_attribs = []
attribs = []
indentation_count = 0
for line in lines:
    if struct_name == "" and bitfield_name == "":
        words = line.split(" ")
        if words[0] == "struct":
            final_string += "\n"
            struct_name = list(words[1])
            if struct_name[-1] == "\n":
                struct_name = struct_name[:-1]
            if struct_name[-1] == "{":
                struct_name = struct_name[:-1]
            struct_name = "".join(struct_name)
            type_names.append(struct_name)
        if words[0] == "bitfield":
            final_string += "\n"
            bitfield_name = list(words[1])
            if bitfield_name[-1] == "\n":
                bitfield_name = bitfield_name[:-1]
            if bitfield_name[-1] == "{":
                bitfield_name = bitfield_name[:-1]
            bitfield_name = "".join(bitfield_name)
            type_names.append(bitfield_name)

    elif struct_name != "":
        if line[0] == "}":
            final_string += make_struct(struct_name, attribs)
            attribs = []
            current_attribs = []
            struct_name = ""
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
                length = f"eval('{length}')"
                pad_name = f"padding_{padding_count}"
                padding_count += 1
                attribs.append(("Padding", pad_name, length))
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
                    length = f"eval('{length}')"
                    attribs.append((class_name, att_name, length))
                    current_attribs.append(att_name)
                else:
                    attribs.append((class_name, att_name, 0))
                    current_attribs.append(att_name)
            else:
                if "}" in line:
                    indentation_count -= 1
                    line = line.replace("}", "")
                for _ in range(0, indentation_count):
                    line = indentation + line
                line += "\n"
                if "{" in line:
                    indentation_count += 1
                    line = line.replace(" {", ":")
                    line = line.replace("{", ":")
                line = line.replace("//", "#")
                attribs.append((plain_text,
                                line,
                                0
                              ))

    elif bitfield_name != "":
        if line[0] == "}":
            final_string += make_bitfield(bitfield_name, attribs)
            attribs = []
            current_attribs = []
            bitfield_name = ""
        else:
            line = line.lstrip()
            line = line.rstrip()
            line = line.split(";")[0]
            words = line.split(": ")
            attribs.append((words[0], int(words[1])))

with open("ignore/test.py", "w") as f:
    f.write(final_string)
