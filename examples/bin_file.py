from primitives import Dollar, Struct, BitField, IntStruct, u8, u16, u24, u32, u48, u64, u96, u128, s8, s16, s24, s32, s48, s64, s96, s128, Float, double, char, char16, Bool, Padding, Array, sizeof, addressof

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

class Flags(BitField):
    """
hexpat definition:
```hexpat
bitfield Flags {
    unused: 4;
    f_variable: 1;
    // This comment will appear in the .py file
    f_u16: 1; // This comment won't appear in the .py file. But it will in the docstring
    f_u32: 1;
};

```"""
    def __init__(self, name: str=""):
        """
        bitfield

        Args:
            name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
        """

        super().__init__(name)

    def __matmul__(self, _dollar___offset):
        if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset)} was used instead')
        if isinstance(_dollar___offset, IntStruct):
            _dollar___offset = _dollar___offset.to_dollar()
        _dollar___offset_copy = _dollar___offset.copy()
        _read__able____bytes: bytes = _dollar___offset.read(1)
        self.f_u32 = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[1]
        self.f_u16 = (_read__able____bytes[0] >> 1) & self._bit_field___masks_dict[1]
        # This comment will appear in the .py file
        self.f_variable = (_read__able____bytes[0] >> 2) & self._bit_field___masks_dict[1]
        self.unused = (_read__able____bytes[0] >> 3) & self._bit_field___masks_dict[4]
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class Data(Struct):
    """
hexpat definition:
```hexpat
struct Data {
    Flags flags;
    if (flags.f_variable == 1) {
        u8 amount;
        u8 data[amount];
    }
    if (flags.f_u16 == 1) {
        u16 data;
    }
    if (flags.f_u32 == 1) {
        u32 data;
    }
};

```"""
    def __init__(self, name: str=""):
        """
        struct

        Args:
            name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
        """
        super().__init__(name)

    def __matmul__(self, _dollar___offset):
        if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset)} was used instead')
        if isinstance(_dollar___offset, IntStruct):
            _dollar___offset = _dollar___offset.to_dollar()
        _dollar___offset_copy = _dollar___offset.copy()
        flags: Flags = Flags('flags') @ _dollar___offset
        self.flags = flags
        if (flags.f_variable == 1):
            amount: u8 = u8('amount') @ _dollar___offset
            self.amount = amount
            data: Array[u8] = Array(u8, amount) @ _dollar___offset
            self.data = data
        if (flags.f_u16 == 1):
            data: u16 = u16('data') @ _dollar___offset
            self.data = data
        if (flags.f_u32 == 1):
            data: u32 = u32('data') @ _dollar___offset
            self.data = data

        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class Header(Struct):
    """
hexpat definition:
```hexpat
struct Header {
    char header_name[8];
    u32 header_size;
    u32 data_size;
    u8 element_amount;
};

```"""
    def __init__(self, name: str=""):
        """
        struct

        Args:
            name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
        """
        super().__init__(name)

    def __matmul__(self, _dollar___offset):
        if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset)} was used instead')
        if isinstance(_dollar___offset, IntStruct):
            _dollar___offset = _dollar___offset.to_dollar()
        _dollar___offset_copy = _dollar___offset.copy()
        header_name: Array[char] = Array(char, 8) @ _dollar___offset
        self.header_name = header_name
        header_size: u32 = u32('header_size') @ _dollar___offset
        self.header_size = header_size
        data_size: u32 = u32('data_size') @ _dollar___offset
        self.data_size = data_size
        element_amount: u8 = u8('element_amount') @ _dollar___offset
        self.element_amount = element_amount

        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class File(Struct):
    """
hexpat definition:
```hexpat
struct File {
    Header header;
    padding[3];
    Data data[header.element_amount];
};

```"""
    def __init__(self, name: str=""):
        """
        struct

        Args:
            name (str, optional): The name of this instance. Can be whatever you want or just an empty string. Defaults to "".
        """
        super().__init__(name)

    def __matmul__(self, _dollar___offset):
        if not (isinstance(_dollar___offset, Dollar) or isinstance(_dollar___offset, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset)} was used instead')
        if isinstance(_dollar___offset, IntStruct):
            _dollar___offset = _dollar___offset.to_dollar()
        _dollar___offset_copy = _dollar___offset.copy()
        header: Header = Header('header') @ _dollar___offset
        self.header = header
        self.padding_0: Padding = Padding(3, 'padding_0') @ _dollar___offset
        data: Array[Data] = Array(Data, header.element_amount) @ _dollar___offset
        self.data = data

        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self
# The line below will be translated to python, but it won't run because 0x00 is an int instead of a dollar
# Manually replace the line below.
# from:
#     @ (0x00)
# to:
#     @ Dollar(0x00, byts)
file: File = File() @ Dollar(0x00, byts) # This line has been altered manually
