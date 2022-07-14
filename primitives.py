struct_names = [
    "u8", "u16", "u32", "u64", "u128",
    "s8", "s16", "s32", "s64", "s128",
    "float", "double",
    "char", "char16",
    "bool"
    ]

class Dollar:
    def __init__(self, offset: int, byts: bytes):
        self.offset = int(offset)
        self.byts = byts
    
    def read(self, amount: int) -> bytes:
        read_bytes = self.byts[self.offset:self.offset+amount]
        self.offset += amount
        return read_bytes
    
    def copy(self):
        return Dollar(self.offset, self.byts)
    
    def __int__(self):
        return self.offset

class Struct:
    def __init__(self, name: str, starting_offset: Dollar, end_offset: Dollar):
        self.name = name
        self.address = starting_offset.offset
        self.size = end_offset.offset

class UnsignedLe(Struct):
    def __init__(self, name: str, offset: Dollar, length: bytes):
        starting_offset = offset.copy()
        exponent = 0
        self.value = 0
        for (exponent, byte) in enumerate(reversed(offset.read(length))):
            self.value += byte * 256**exponent
        
        super().__init__(name, starting_offset, offset.copy())
    
    def __int__(self):
        return self.value
    
    def __index__(self):
        return self.value

class u8(UnsignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 1)

class u16(UnsignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 2)

class u32(UnsignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 4)

class u64(UnsignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 8)

class u128(UnsignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 8)

class SignedLe(Struct):
    def __init__(self, name: str, offset: Dollar, length: int):
        starting_offset = offset.copy()
        exponent = 0
        self.value = 0
        for (exponent, byte) in enumerate(reversed(offset.read(length))):
            self.value += byte * 256**exponent
        # TODO: make signed
        
        super().__init__(name, starting_offset, offset.copy())
    
    def __int__(self):
        return self.value
    
    def __index__(self):
        return self.value

class s8(SignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 1)

class s16(SignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 2)

class s32(SignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 4)

class s64(SignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 8)

class s128(SignedLe):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 8)

class RealNum(Struct):
    def __init__(self, name: str, offset: Dollar, length: int):
        starting_offset = offset.copy()
        self.value = offset.read(length)
        # TODO
        super().__init__(name, starting_offset, offset.copy())

class Float(RealNum):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 4)

class double(RealNum):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 8)

class Character(Struct):
    def __init__(self, name: str, offset: Dollar, length: int):
        starting_offset = offset.copy()
        self.value = offset.read(length)
        # TODO
        super().__init__(name, starting_offset, offset.copy())

class char(Character):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 1)

class char16(Character):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset, 2)

class Bool(Struct):
    def __init__(self, name: str, offset: Dollar):
        starting_offset = offset.copy()
        self.value = offset.read(1)
        # TODO
        super().__init__(name, starting_offset, offset.copy())

class Padding(Struct):
    def __init__(self, name: str, offset: Dollar, length: int):
        starting_offset = offset.copy()
        self.value = offset.read(length)
        # TODO
        super().__init__(name, starting_offset, offset.copy())

class BitField(Struct):
    _bit_field___masks_dict = {
        1: 0b00000001,
        2: 0b00000011,
        3: 0b00000111,
        4: 0b00001111,
        5: 0b00011111,
        6: 0b00111111,
        7: 0b01111111,
        8: 0b11111111,
    }
    def __init__(self, name: str, starting_offset: Dollar, end_offset: Dollar):
        super().__init__(name, starting_offset, end_offset)

def sizeof(struct: Struct) -> int:
    return struct.size

def addressof(struct: Struct) -> int:
    return struct.address
