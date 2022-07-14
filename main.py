def make_struct(name: str, attributes, indentation: str="    "):
    string = f"""\
class {name}(Struct):
{indentation}def __init__(self, name: str, offset: Dollar):
{indentation}{indentation}starting_offset = offset.copy()\n"""
    for (class_name, att_name, array_length) in attributes:
        string += f"{indentation}{indentation}"
        if class_name == "float":
            class_name = "Float"
        elif class_name == "bool":
            class_name = "Bool"

        if class_name == "Padding":
            string += f"self.{att_name} = {class_name}('{att_name}', offset, {length})\n"
        else:
            if array_length == 0:
                string += f"self.{att_name} = {class_name}('{att_name}', offset)\n"
            else:
                string += f"self.{att_name} = []\n"
                string += f"{indentation}{indentation}"
                string += f"for i in range(0,{array_length}):\n"
                string += f"{indentation}{indentation}{indentation}"
                string += f"self.{att_name}.append({class_name}(f'{att_name}_{{i}}', offset))\n"

    string += f"{indentation}{indentation}"
    string += "super().__init__(name, starting_offset, offset.copy())\n"
    return string

with open("ignore/testpath.txt", "r") as f:
    file_path = f.readlines()[0]

with open(file_path, "r") as f:
    lines = f.readlines()

padding_count = 0
final_string = "from primitives import Dollar, Struct, u8, u16, u32, u64, u128, s8, s16, s32, s64, s128, Float, double, char, char16, Bool, Padding\n\n"
struct_name = ""
attribs = []
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
    else:
        if line[0] == "}":
            final_string += make_struct(struct_name, attribs)
            attribs = []
            struct_name = ""
        else:
            line.lstrip()
            line.rstrip()
            while line[0] == "\t":
                line = "".join(list(line)[1:])
            line = line.split(";")[0]
            words = line.split(" ")
            try_padding = words[0].split("[")
            if try_padding[0] == "padding":
                length = int(try_padding[1].split("]")[0])
                pad_name = f"padding_{padding_count}"
                padding_count += 1
                attribs.append(("Padding", pad_name, length))
            else:
                class_name = words[0]
                att_name = words[1]
                if "[" in att_name:
                    (att_name, length) = att_name.split("[")
                    length = int(length.split("]")[0])
                    attribs.append((class_name, att_name, length))
                else:
                    attribs.append((class_name, att_name, 0))

with open("ignore/test.py", "w") as f:
    f.write(final_string)
