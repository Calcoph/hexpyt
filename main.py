import primitives

plain_text = "PlainText_thisisalongnameonpurposesonobodywoulduseitonaccident"
indentation = "    "

def make_struct(name: str, attributes):
    string = f"""\
class {name}(Struct):
{indentation}def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
{indentation}{indentation}_dollar___offset_copy = _dollar___offset.copy()\n"""
    for (class_name, att_name, array_length) in attributes:
        string += f"{indentation}{indentation}"
        if class_name == "float":
            class_name = "Float"
        elif class_name == "bool":
            class_name = "Bool"

        if class_name == "Padding":
            string += f"self.{att_name} = {class_name}('{att_name}', _dollar___offset, {array_length})\n"
        elif class_name == plain_text:
            string += att_name
        else:
            if array_length == 0:
                string += f"{att_name} = {class_name}('{att_name}', _dollar___offset)\n"
                string += f"{indentation}{indentation}"
                string += f"self.{att_name} = {att_name}\n"
            else:
                string += f"self.{att_name} = []\n"
                string += f"{indentation}{indentation}"
                string += f"for i in range(0,{array_length}):\n"
                string += f"{indentation}{indentation}{indentation}"
                string += f"self.{att_name}.append({class_name}(f'{att_name}_{{i}}', _dollar___offset))\n"

    string += f"{indentation}{indentation}"
    string += "super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())\n"
    return string

with open("ignore/testpath.txt", "r") as f:
    file_path = f.readlines()[0]

with open(file_path, "r") as f:
    lines = f.readlines()

padding_count = 0
final_string = "from primitives import Dollar, Struct, u8, u16, u32, u64, u128, s8, s16, s32, s64, s128, Float, double, char, char16, Bool, Padding, sizeof, addressof\n\n"
struct_name = ""
struct_names = primitives.struct_names
current_struct_attribs = []
attribs = []
indentation_count = 0
for line in lines:
    if struct_name == "":
        words = line.split(" ")
        if words[0] == "struct":
            final_string += "\n"
            struct_name = list(words[1])
            if struct_name[-1] == "\n":
                struct_name = struct_name[:-1]
            if struct_name[-1] == "{":
                struct_name = struct_name[:-1]
            struct_name = "".join(struct_name)
            struct_names.append(struct_name)
    else:
        if line[0] == "}":
            final_string += make_struct(struct_name, attribs)
            attribs = []
            current_struct_attribs = []
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
            elif words[0] in struct_names:
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
                    current_struct_attribs.append(att_name)
                else:
                    attribs.append((class_name, att_name, 0))
                    current_struct_attribs.append(att_name)
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

with open("ignore/test.py", "w") as f:
    f.write(final_string)
