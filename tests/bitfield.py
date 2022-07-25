from primitives import Dollar, Struct, BitField, IntStruct, u8, u16, u24, u32, u48, u64, u96, u128, s8, s16, s24, s32, s48, s64, s96, s128, Float, double, char, char16, Bool, Padding, Array, sizeof, addressof

# Template to read from a file. follow the instructions.
# _dollar___offset has this name so it doesn't clash with others. Feel free to rename it. 
if False: # Change this from "if True" to "if False", then put the file path below.
    byts = b''
else:
    file_path = "../examples/binary_files/bin_file.bin" # Put the file path here and change the above "if True" to "if False".
    with open(file_path, "rb") as f:
        byts = f.read()
_dollar___offset = Dollar(0x00, byts)
# End of template
# The values in the comments in the comments are the ones when reading examples/binary_files/bin_file.bin in imhex


class bit1(BitField):
    """
hexpat definition:
```hexpat
bitfield bit1 {
	a: 1; // 0
	b: 1; // 1
	c: 1; // 0
	d: 1; // 0
	e: 1; // 0
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(1)))
        self.a = (_read__able____bytes[0] >> 4) & self._bit_field___masks_dict[1]
        self.b = (_read__able____bytes[0] >> 3) & self._bit_field___masks_dict[1]
        self.c = (_read__able____bytes[0] >> 2) & self._bit_field___masks_dict[1]
        self.d = (_read__able____bytes[0] >> 1) & self._bit_field___masks_dict[1]
        self.e = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[1]
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit2(BitField):
    """
hexpat definition:
```hexpat
bitfield bit2 {
	a: 7; // 0
	b: 7; // 0
	c: 7; // 0
	d: 7; // 0
	e: 7; // 4 = 100
	f: 7; // 34 = 100010
	g: 7; // 5 = 101
	h: 7; // 10 = 1010
	i: 7; // 72 = 1001000
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(8)))
        self.a = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[7]
        _read__able____bytes = _read__able____bytes[1:]
        self.b = (_read__able____bytes[0] >> 1) & self._bit_field___masks_dict[7]
        c = 0
        c += (_read__able____bytes[0] >> 7) & self._bit_field___masks_dict[1]
        _read__able____bytes = _read__able____bytes[1:]
        c <<= 8
        c += _read__able____bytes[0] & self._bit_field___masks_dict[6]
        self.c = c
        d = 0
        d += (_read__able____bytes[0] >> 6) & self._bit_field___masks_dict[2]
        _read__able____bytes = _read__able____bytes[1:]
        d <<= 8
        d += _read__able____bytes[0] & self._bit_field___masks_dict[5]
        self.d = d
        e = 0
        e += (_read__able____bytes[0] >> 5) & self._bit_field___masks_dict[3]
        _read__able____bytes = _read__able____bytes[1:]
        e <<= 8
        e += _read__able____bytes[0] & self._bit_field___masks_dict[4]
        self.e = e
        f = 0
        f += (_read__able____bytes[0] >> 4) & self._bit_field___masks_dict[4]
        _read__able____bytes = _read__able____bytes[1:]
        f <<= 8
        f += _read__able____bytes[0] & self._bit_field___masks_dict[3]
        self.f = f
        g = 0
        g += (_read__able____bytes[0] >> 3) & self._bit_field___masks_dict[5]
        _read__able____bytes = _read__able____bytes[1:]
        g <<= 8
        g += _read__able____bytes[0] & self._bit_field___masks_dict[2]
        self.g = g
        h = 0
        h += (_read__able____bytes[0] >> 2) & self._bit_field___masks_dict[6]
        _read__able____bytes = _read__able____bytes[1:]
        h <<= 8
        h += _read__able____bytes[0] & self._bit_field___masks_dict[1]
        self.h = h
        self.i = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[7]
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit3(BitField):
    """
hexpat definition:
```hexpat
bitfield bit3 {
	a: 16; // 17736 = 100010101001000
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(2)))
        a = 0
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        self.a = a
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit4(BitField):
    """
hexpat definition:
```hexpat
bitfield bit4 {
	a: 20; // 83272 = 10100010101001000
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(3)))
        a = 0
        a += (_read__able____bytes[0] >> 4) & self._bit_field___masks_dict[4]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        self.a = a
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit5(BitField):
    """
hexpat definition:
```hexpat
bitfield bit5 {
	a: 3; // 1
	b: 16; // 17736 = 100010101001000
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(3)))
        self.a = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[3]
        _read__able____bytes = _read__able____bytes[1:]
        b = 0
        b += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        b <<= 8
        b += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        self.b = b
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit6(BitField):
    """
hexpat definition:
```hexpat
bitfield bit6 {
	a: 3; // 4 = 100
	b: 20; // 83272 = 10100010101001000
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(3)))
        self.a = (_read__able____bytes[0] >> 4) & self._bit_field___masks_dict[3]
        b = 0
        b += (_read__able____bytes[0] >> 4) & self._bit_field___masks_dict[4]
        _read__able____bytes = _read__able____bytes[1:]
        b <<= 8
        b += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        b <<= 8
        b += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        self.b = b
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit7(BitField):
    """
hexpat definition:
```hexpat
bitfield bit7 {
	a: 16; // 10409 = 10100010101001
	b: 3; // 0
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(3)))
        a = 0
        a += (_read__able____bytes[0] >> 5) & self._bit_field___masks_dict[3]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[5]
        self.a = a
        self.b = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[3]
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self

class bit8(BitField):
    """
hexpat definition:
```hexpat
bitfield bit8 {
	a: 20; // 534697 = 10000010100010101001
	b: 3; // 0
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
        _read__able____bytes: bytes = bytes(reversed(_dollar___offset.read(3)))
        a = 0
        a += (_read__able____bytes[0] >> 1) & self._bit_field___masks_dict[7]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[8]
        _read__able____bytes = _read__able____bytes[1:]
        a <<= 8
        a += _read__able____bytes[0] & self._bit_field___masks_dict[5]
        self.a = a
        self.b = (_read__able____bytes[0] >> 0) & self._bit_field___masks_dict[3]
        super().init_struct(_dollar___offset_copy, _dollar___offset.copy())
        return self
b1: bit1 = bit1() @ Dollar(0x00, byts)
b2: bit2 = bit2() @ Dollar(0x00, byts)
b3: bit3 = bit3() @ Dollar(0x00, byts)
b4: bit4 = bit4() @ Dollar(0x00, byts)
b5: bit5 = bit5() @ Dollar(0x00, byts)
b6: bit6 = bit6() @ Dollar(0x00, byts)
b7: bit7 = bit7() @ Dollar(0x00, byts)
b8: bit8 = bit8() @ Dollar(0x00, byts)
