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

    def __index__(self):
        return self.offset.__index__()

    def __repr__(self):
        return self.offset.__repr__()
    
    def __str__(self):
        return self.offset.__str__()

    def __lt__(self, other):
        return self.offset.__lt__(other)

    def __le__(self, other):
        return self.offset.__le__(other)

    def __eq__(self, other):
        return self.offset.__eq__(other)

    def __ne__(self, other):
        return self.offset.__ne__(other)

    def __gt__(self, other):
        return self.offset.__gt__(other)

    def __ge__(self, other):
        return self.offset.__ge__(other)
    
    def __hash__(self) -> int:
        return self.offset.__hash__()
    
    def __bool__(self):
        return self.offset.__bool__()
    
    def __len__(self):
        return self.offset.__len__()
    
    def __length_hint__(self):
        return self.offset.__length_hint__()
    
    def __add__(self, other):
        return self.offset.__add__(other)

    def __sub__(self, other):
        return self.offset.__sub__(other)

    def __mul__(self, other):
        return self.offset.__mul__(other)

    def __truediv__(self, other):
        return self.offset.__truediv__(other)

    def __floordiv__(self, other):
        return self.offset.__floordiv__(other)

    def __mod__(self, other):
        return self.offset.__mod__(other)

    def __divmod__(self, other):
        return self.offset.__divmod__(other)

    def __pow__(self, other):
        return self.offset.__pow__(other)

    def __lshift__(self, other):
        return self.offset.__lshift__(other)

    def __rshift__(self, other):
        return self.offset.__rshift__(other)
    
    def __and__(self, other):
        return self.offset.__and__(other)

    def __xor__(self, other):
        return self.offset.__xor__(other)

    def __radd__(self, other):
        return self.offset.__radd__(other)

    def __rsub__(self, other):
        return self.offset.__rsub__(other)

    def __rmul__(self, other):
        return self.offset.__rmul__(other)

    def __rtruediv__(self, other):
        return self.offset.__rtruediv__(other)

    def __rfloordiv__(self, other):
        return self.offset.__rfloordiv__(other)

    def __rmod__(self, other):
        return self.offset.__rmod__(other)

    def __rdivmod__(self, other):
        return self.offset.__rdivmod__(other)

    def __rpow__(self, other):
        return self.offset.__rpow__(other)

    def __rlshift__(self, other):
        return self.offset.__rlshift__(other)

    def __rrshift__(self, other):
        return self.offset.__rrshift__(other)

    def __rand__(self, other):
        return self.offset.__rand__(other)

    def __rxor__(self, other):
        return self.offset.__rxor__(other)

    def __ror__(self, other):
        return self.offset.__ror__(other)

    def __iadd__(self, other):
        return self.offset.__iadd__(other)

    def __isub__(self, other):
        return self.offset.__isub__(other)

    def __imul__(self, other):
        return self.offset.__imul__(other)

    def __itruediv__(self, other):
        return self.offset.__itruediv__(other)

    def __ifloordiv__(self, other):
        return self.offset.__ifloordiv__(other)

    def __imod__(self, other):
        return self.offset.__imod__(other)

    def __ipow__(self, other):
        return self.offset.__ipow__(other)

    def __ilshift__(self, other):
        return self.offset.__ilshift__(other)

    def __irshift__(self, other):
        return self.offset.__irshift__(other)

    def __iand__(self, other):
        return self.offset.__iand__(other)

    def __ixor__(self, other):
        return self.offset.__ixor__(other)

    def __ior__(self, other):
        return self.offset.__ior__(other)

    def __neg__(self, other):
        return self.offset.__neg__(other)

    def __pos__(self, other):
        return self.offset.__pos__(other)

    def __abs__(self, other):
        return self.offset.__abs__(other)

    def __invert__(self, other):
        return self.offset.__invert__(other)
    
    def __complex__(self):
        return self.offset.__complex__()

    def __int__(self):
        return self.offset

    def __float__(self):
        return self.offset.__float__()

    def __round__(self):
        return self.offset.__round__()

    def __trunc__(self):
        return self.offset.__trunc__()

    def __floord__(self):
        return self.offset.__floord__()

    def __ceil__(self):
        return self.offset.__ceil__()

class Struct:
    def __init__(self, name: str, starting_offset: Dollar, end_offset: Dollar):
        self.name = name
        self.address = starting_offset.offset
        self.size = end_offset.offset

class IntStruct(Struct):
    def __init__(self, name: str, starting_offset: Dollar, end_offset: Dollar):
        super().__init__(name, starting_offset, end_offset)

    def __repr__(self):
        return self.value.__repr__()
    
    def __str__(self):
        return self.value.__str__()

    def __lt__(self, other):
        return self.value.__lt__(other)

    def __le__(self, other):
        return self.value.__le__(other)

    def __eq__(self, other):
        return self.value.__eq__(other)

    def __ne__(self, other):
        return self.value.__ne__(other)

    def __gt__(self, other):
        return self.value.__gt__(other)

    def __ge__(self, other):
        return self.value.__ge__(other)
    
    def __hash__(self) -> int:
        return self.value.__hash__()
    
    def __bool__(self):
        return self.value.__bool__()
    
    def __len__(self):
        return self.value.__len__()
    
    def __length_hint__(self):
        return self.value.__length_hint__()
    
    def __add__(self, other):
        return self.value.__add__(other)

    def __sub__(self, other):
        return self.value.__sub__(other)

    def __mul__(self, other):
        return self.value.__mul__(other)

    def __truediv__(self, other):
        return self.value.__truediv__(other)

    def __floordiv__(self, other):
        return self.value.__floordiv__(other)

    def __mod__(self, other):
        return self.value.__mod__(other)

    def __divmod__(self, other):
        return self.value.__divmod__(other)

    def __pow__(self, other):
        return self.value.__pow__(other)

    def __lshift__(self, other):
        return self.value.__lshift__(other)

    def __rshift__(self, other):
        return self.value.__rshift__(other)
    
    def __and__(self, other):
        return self.value.__and__(other)

    def __xor__(self, other):
        return self.value.__xor__(other)

    def __radd__(self, other):
        return self.value.__radd__(other)

    def __rsub__(self, other):
        return self.value.__rsub__(other)

    def __rmul__(self, other):
        return self.value.__rmul__(other)

    def __rtruediv__(self, other):
        return self.value.__rtruediv__(other)

    def __rfloordiv__(self, other):
        return self.value.__rfloordiv__(other)

    def __rmod__(self, other):
        return self.value.__rmod__(other)

    def __rdivmod__(self, other):
        return self.value.__rdivmod__(other)

    def __rpow__(self, other):
        return self.value.__rpow__(other)

    def __rlshift__(self, other):
        return self.value.__rlshift__(other)

    def __rrshift__(self, other):
        return self.value.__rrshift__(other)

    def __rand__(self, other):
        return self.value.__rand__(other)

    def __rxor__(self, other):
        return self.value.__rxor__(other)

    def __ror__(self, other):
        return self.value.__ror__(other)

    def __iadd__(self, other):
        return self.value.__iadd__(other)

    def __isub__(self, other):
        return self.value.__isub__(other)

    def __imul__(self, other):
        return self.value.__imul__(other)

    def __itruediv__(self, other):
        return self.value.__itruediv__(other)

    def __ifloordiv__(self, other):
        return self.value.__ifloordiv__(other)

    def __imod__(self, other):
        return self.value.__imod__(other)

    def __ipow__(self, other):
        return self.value.__ipow__(other)

    def __ilshift__(self, other):
        return self.value.__ilshift__(other)

    def __irshift__(self, other):
        return self.value.__irshift__(other)

    def __iand__(self, other):
        return self.value.__iand__(other)

    def __ixor__(self, other):
        return self.value.__ixor__(other)

    def __ior__(self, other):
        return self.value.__ior__(other)

    def __neg__(self, other):
        return self.value.__neg__(other)

    def __pos__(self, other):
        return self.value.__pos__(other)

    def __abs__(self, other):
        return self.value.__abs__(other)

    def __invert__(self, other):
        return self.value.__invert__(other)
    
    def __complex__(self):
        return self.value.__complex__()

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value.__float__()

    def __round__(self):
        return self.value.__round__()

    def __trunc__(self):
        return self.value.__trunc__()

    def __floord__(self):
        return self.value.__floord__()

    def __ceil__(self):
        return self.value.__ceil__()
    
    def __index__(self):
        return self.value

class UnsignedLe(IntStruct):
    def __init__(self, name: str, offset: Dollar, length: bytes):
        starting_offset = offset.copy()
        self.value = 0
        for (exponent, byte) in enumerate(offset.read(length)):
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

class SignedLe(IntStruct):
    def __init__(self, name: str, offset: Dollar, length: int):
        starting_offset = offset.copy()
        self.value = 0
        for (exponent, byte) in enumerate(offset.read(length)):
            self.value += byte * 256**exponent
        # TODO: make signed
        
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
