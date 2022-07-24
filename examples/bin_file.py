from typing import List
from primitives import Dollar, Struct, u8, u16, u32, u64, u128, s8, s16, s32, s64, s128, Float, double, char, char16, Bool, Padding, BitField, sizeof, addressof


class Flags(BitField):
    """
hexpat definition:
```hexpat
bitfield Flags {
    unused: 4;
    f_variable: 1;
    // This comment will appear in the .py file
    f_u16: 1; // This comment won't appear in the .py file
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
        if not isinstance(_dollar___offset, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset_copy)} was used instead')
        _dollar___offset_copy = _dollar___offset.copy()
        cur_byte = _dollar___offset.read(1)[0]
        self.unused: int = (cur_byte >>0) & self._bit_field___masks_dict[4]
        self.f_variable: int = (cur_byte >>4) & self._bit_field___masks_dict[1]
        # This comment will appear in the .py file
        self.f_u16: int = (cur_byte >>5) & self._bit_field___masks_dict[1]
        self.f_u32: int = (cur_byte >>6) & self._bit_field___masks_dict[1]
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
        if not isinstance(_dollar___offset, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset_copy)} was used instead')
        _dollar___offset_copy = _dollar___offset.copy()
        flags: Flags = Flags('flags') @ _dollar___offset
        self.flags = flags
        if (flags.f_variable == 1):
            amount: u8 = u8('amount') @ _dollar___offset
            self.amount = amount
            self.data: List[u8] = []
            for i in range(0,eval('amount')):
                self.data.append(u8(f'data_{i}') @ _dollar___offset)
        
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
        if not isinstance(_dollar___offset, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset_copy)} was used instead')
        _dollar___offset_copy = _dollar___offset.copy()
        self.header_name: List[char] = []
        for i in range(0,eval('8')):
            self.header_name.append(char(f'header_name_{i}') @ _dollar___offset)
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
        if not isinstance(_dollar___offset, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(_dollar___offset_copy)} was used instead')
        _dollar___offset_copy = _dollar___offset.copy()
        header: Header = Header('header') @ _dollar___offset
        self.header = header
        self.padding_0: Padding = Padding(eval('3'), 'padding_0') @ _dollar___offset
        self.data: List[Data] = []
        for i in range(0,eval('header.element_amount')):
            self.data.append(Data(f'data_{i}') @ _dollar___offset)
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self
