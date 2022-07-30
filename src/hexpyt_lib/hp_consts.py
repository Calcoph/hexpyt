import primitives

plain_text = "PlainText_thisisalongnameonpurposesonobodywoulduseitonaccident"

class TranslateState:
    def __init__(self, header: str, indentation: str) -> None:
        self.padding_count = 0
        self.struct_name = ""
        self.bitfield_name = ""
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
            ("break", "self.breaked = True\nreturn self #! TODO: INDENT THIS LIKE THE LINE ABOVE SO IT COMPILES"),
            ("continue", "return self"),
            ("true", "True"),
            ("false", "False")
        ]

        self.final_string = header
        self.indentation = indentation
