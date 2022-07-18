import struct

struct_names = [
    "u8", "u16", "u32", "u64", "u128",
    "s8", "s16", "s32", "s64", "s128",
    "float", "double",
    "char", "char16",
    "bool"
    ]

def le_to_int(byts: bytes):
    value = 0
    for (exponent, byte) in enumerate(byts):
        value += byte * 256**exponent
    return value

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
    def __init__(self, name: str=""):
        self.name = name
    
    def init_struct(self, starting_offset: Dollar, end_offset: Dollar):
        self.address = starting_offset.offset
        self.size = end_offset.offset

class IntStruct(Struct):
    def __init__(self, name: str=""):
        super().__init__(name)

    def __repr__(self):
        return self.value.__repr__()
    
    def __str__(self):
        return self.value.__str__()

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)

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
    def __init__(self, length: int, value: int=0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = le_to_int(other.read(self.length))
        super().init_struct(starting_offset, other.copy())
        return self

class u8(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(1, value, name)

class u16(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(2, value, name)

class u32(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(4, value, name)

class u64(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(8, value, name)

class u128(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(16, value, name)

class SignedLe(IntStruct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)

    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = le_to_int(other.read(self.length))
        
        negative_threshold_bytes = b'\x80'
        for _ in range(1,self.length):
            negative_threshold_bytes = b'\x00' + negative_threshold_bytes
        negative_threshold = 0
        for (exponent, byte) in enumerate(other.read(negative_threshold_bytes)):
            negative_threshold += byte * 256**exponent
        max_ = negative_threshold*2+1
        self.value = -(max_ - self.value)-1
        super().init_struct(starting_offset, other.copy())
        return self

class s8(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(1, value, name)

class s16(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(2, value, name)

class s32(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(4, value, name)

class s64(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(8, value, name)

class s128(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(16, value, name)

class RealNum(Struct):
    def __init__(self, length: int, value: float=0.0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = other.read(self.length)
        if self.length == 4:
            format_ = "<f"
        elif self.length == 8:
            format_ = "<d"
        self.value = struct.unpack(format_, self.value)
        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return self.value.__repr__()
    
    def __str__(self):
        return self.value.__str__()

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)

class Float(RealNum):
    def __init__(self, value: float=0.0, name: str=""):
        super().__init__(4, value, name)

class double(RealNum):
    def __init__(self, value: float=0.0, name: str=""):
        super().__init__(8, value, name)

class Character(Struct):
    def __init__(self, length: int, value: str="\0", name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = other.read(self.length)
        self.value = "".join(map(chr, self.value))
        super().init_struct(starting_offset, other.copy())
        return self

    def __repr__(self):
        return self.value.__repr__()
    
    def __str__(self):
        return self.value.__str__()

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)

class char(Character):
    def __init__(self, value: str="\0", name: str=""):
        super().__init__(1, value, name)

class char16(Character):
    def __init__(self, value: str="\0\0", name: str=""):
        super().__init__(2, value, name)

class Bool(Struct):
    def __init__(self, value: bool=False, name: str="", false_range=range(0x00,0x01), true_range=range(0x01,0xFF)):
        self.false_range = false_range
        self.true_range = true_range
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = le_to_int(other.read(1))
        if self.false_range == range(0x00,0x01):
            if self.value in self.true_range:
                self.value = True
            else:
                self.value = False
        else:
            if self.value in self.false_range:
                self.value = False
            else:
                self.value = True

        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return self.value.__repr__()
    
    def __str__(self):
        return self.value.__str__()

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)

class Padding(Struct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not isinstance(other, Dollar):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        starting_offset = other.copy()
        self.value = other.read(self.length)
        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return f"padding[{self.length}]"
    
    def __str__(self):
        return f"padding[{self.length}]"

    def __format__(self, format_spec):
        return f"padding[{self.length}]".__format__(format_spec)

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
    def __init__(self, name: str=""):
        super().__init__(name)

def sizeof(struct: Struct) -> int:
    return struct.size

def addressof(struct: Struct) -> int:
    return struct.address
