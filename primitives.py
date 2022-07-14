class Dollar(int):
    def __init__(self, offset: int, byts: bytes):
        self.parent().__init__(offset)
        self.byts = byts
    
    def read(self, amount: int):
        self.byts[self.offset:self.offset+amount]
        self.offset += amount
    
    def copy(self):
        return Dollar(self.offset, self.byts)

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
        for (exponent, byte) in enumerate(offset.read(length)):
            self.value += byte * 256**exponent
        
        super().__init__(name, starting_offset, offset.copy())

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
        super().__init__(name, offset)

class char16(Character):
    def __init__(self, name: str, offset: Dollar):
        super().__init__(name, offset)

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
