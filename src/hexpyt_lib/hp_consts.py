import primitives

plain_text = "PlainText_thisisalongnameonpurposesonobodywoulduseitonaccident"

class TranslateState:
    def __init__(self, header: str, indentation: str) -> None:
        self.padding_count = 0
        self.struct_name = ""
        self.bitfield_name = ""
        self.enum_desc = ("", "")
        self.function_name = ""
        self.docstring = ""
        self.type_names = primitives.struct_names
        self.current_attribs = []
        self.attribs = []
        self.indentation_count = 0
        self.opening_brackets = 0
        self.defines = [
            ("std::print", "print"),
            ("$", "_dollar___offset"),
            ("//", "#"),
            ("else if", "elif"),
            ("::", "."),
            ("break", "self.break_()\0return self"),
            ("continue", "return self"),
            ("true", "True"),
            ("false", "False"),
            ("_dollar___offset=", "_dollar___offset.address =")
            ("_dollar___offset =", "_dollar___offset.address =")
            ("_dollar___offset  =", "_dollar___offset.address =")
        ]
        self.cur_line = None

        self.final_string = header
        self.indentation = indentation
