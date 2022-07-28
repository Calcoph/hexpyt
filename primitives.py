from __future__ import annotations
import struct
from typing import TypeVar, Union

struct_names = [
    "u8", "u16", "u24", "u32", "u48", "u64", "u96", "u128",
    "s8", "s16", "s24", "s32", "s48", "s64", "s96", "s128",
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
        return self.offset.__lt__(int(other))

    def __le__(self, other):
        return self.offset.__le__(int(other))

    def __eq__(self, other):
        return self.offset.__eq__(int(other))

    def __ne__(self, other):
        return self.offset.__ne__(int(other))

    def __gt__(self, other):
        return self.offset.__gt__(int(other))

    def __ge__(self, other):
        return self.offset.__ge__(int(other))
    
    def __hash__(self) -> int:
        return self.offset.__hash__()
    
    def __bool__(self):
        return self.offset.__bool__()
    
    def __len__(self):
        return self.offset.__len__()
    
    def __length_hint__(self):
        return self.offset.__length_hint__()
    
    def __add__(self, other):
        return self.offset.__add__(int(other))

    def __sub__(self, other):
        return self.offset.__sub__(int(other))

    def __mul__(self, other):
        return self.offset.__mul__(int(other))

    def __truediv__(self, other):
        return self.offset.__truediv__(int(other))

    def __floordiv__(self, other):
        return self.offset.__floordiv__(int(other))

    def __mod__(self, other):
        return self.offset.__mod__(int(other))

    def __divmod__(self, other):
        return self.offset.__divmod__(int(other))

    def __pow__(self, other):
        return self.offset.__pow__(int(other))

    def __lshift__(self, other):
        return self.offset.__lshift__(int(other))

    def __rshift__(self, other):
        return self.offset.__rshift__(int(other))
    
    def __and__(self, other):
        return self.offset.__and__(int(other))

    def __xor__(self, other):
        return self.offset.__xor__(int(other))

    def __radd__(self, other):
        return self.offset.__radd__(int(other))

    def __rsub__(self, other):
        return self.offset.__rsub__(int(other))

    def __rmul__(self, other):
        return self.offset.__rmul__(int(other))

    def __rtruediv__(self, other):
        return self.offset.__rtruediv__(int(other))

    def __rfloordiv__(self, other):
        return self.offset.__rfloordiv__(int(other))

    def __rmod__(self, other):
        return self.offset.__rmod__(int(other))

    def __rdivmod__(self, other):
        return self.offset.__rdivmod__(int(other))

    def __rpow__(self, other):
        return self.offset.__rpow__(int(other))

    def __rlshift__(self, other):
        return self.offset.__rlshift__(int(other))

    def __rrshift__(self, other):
        return self.offset.__rrshift__(int(other))

    def __rand__(self, other):
        return self.offset.__rand__(int(other))

    def __rxor__(self, other):
        return self.offset.__rxor__(int(other))

    def __ror__(self, other):
        return self.offset.__ror__(int(other))

    def __iadd__(self, other):
        self.offset += int(other)
        return self

    def __isub__(self, other):
        self.offset -= int(other)
        return self

    def __imul__(self, other):
        self.offset += int(other)
        return self

    def __itruediv__(self, other):
        self.offset /= int(other)
        return self

    def __ifloordiv__(self, other):
        self.offset //= int(other)
        return self

    def __imod__(self, other):
        self.offset %= int(other)
        return self

    def __ipow__(self, other):
        self.offset **= int(other)
        return self

    def __ilshift__(self, other):
        self.offset <<= int(other)
        return self

    def __irshift__(self, other):
        self.offset >>= int(other)
        return self

    def __iand__(self, other):
        self.offset &= int(other)
        return self

    def __ixor__(self, other):
        self.offset ^= int(other)
        return self

    def __ior__(self, other):
        self.offset |= int(other)
        return self

    def __neg__(self, other):
        return self.offset.__neg__(int(other))

    def __pos__(self, other):
        return self.offset.__pos__(int(other))

    def __abs__(self, other):
        return self.offset.__abs__(int(other))

    def __invert__(self, other):
        return self.offset.__invert__(int(other))
    
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
        self.breaked = False
    
    def init_struct(self, starting_offset: Dollar, end_offset: Dollar):
        self.address = starting_offset.offset
        self.dollar = end_offset
        self.size = end_offset.offset - self.address

class IntStruct(Struct):
    def __init__(self, name: str=""):
        self.value: int
        super().__init__(name)

    def to_dollar(self) -> Dollar:
        return Dollar(self.value, self.dollar.byts)

    def __repr__(self) -> str:
        return self.value.__repr__()
    
    def __str__(self) -> str:
        return self.value.__str__()

    def __format__(self, format_spec) -> str:
        return self.value.__format__(format_spec)

    def __lt__(self, other) -> bool:
        return self.value.__lt__(int(other))

    def __le__(self, other) -> bool:
        return self.value.__le__(int(other))

    def __eq__(self, other) -> bool:
        return self.value.__eq__(int(other))

    def __ne__(self, other) -> bool:
        return self.value.__ne__(int(other))

    def __gt__(self, other) -> bool:
        return self.value.__gt__(int(other))

    def __ge__(self, other) -> bool:
        return self.value.__ge__(int(other))
    
    def __hash__(self) -> int:
        return self.value.__hash__()
    
    def __bool__(self) -> bool:
        return self.value.__bool__()
    
    def __add__(self, other) -> IntStruct:
        result = self.value.__add__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __sub__(self, other) -> IntStruct:
        result = self.value.__sub__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __mul__(self, other) -> IntStruct:
        result = self.value.__mul__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __truediv__(self, other):
        return self.value.__truediv__(int(other))

    def __floordiv__(self, other) -> IntStruct:
        result = self.value.__floordiv__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __mod__(self, other) -> IntStruct:
        result = self.value.__mod__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __divmod__(self, other):
        return self.value.__divmod__(other)

    def __pow__(self, other) -> IntStruct:
        result = self.value.__pow__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __lshift__(self, other) -> IntStruct:
        result = self.value.__lshift__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rshift__(self, other) -> IntStruct:
        result = self.value.__rshift__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result
    
    def __and__(self, other) -> IntStruct:
        result = self.value.__and__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __xor__(self, other) -> IntStruct:
        result = self.value.__xor__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __radd__(self, other) -> IntStruct:
        result = self.value.__radd__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rsub__(self, other) -> IntStruct:
        result = self.value.__rsub__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rmul__(self, other) -> IntStruct:
        result = self.value.__rmul__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rtruediv__(self, other) -> IntStruct:
        result = self.value.__rtruediv__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rfloordiv__(self, other) -> IntStruct:
        result = self.value.__rfloordiv__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rmod__(self, other) -> IntStruct:
        result = self.value.__rmod__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rdivmod__(self, other):
        return self.value.__rdivmod__(int(other))

    def __rpow__(self, other):
        return self.value.__rpow__(int(other))

    def __rlshift__(self, other) -> IntStruct:
        result = self.value.__rlshift__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rrshift__(self, other) -> IntStruct:
        result = self.value.__rrshift__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rand__(self, other) -> IntStruct:
        result = self.value.__rand__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __rxor__(self, other) -> IntStruct:
        result = self.value.__rxor__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __ror__(self, other) -> IntStruct:
        result = self.value.__ror__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __iadd__(self, other):
        self.value += int(other)
        return self

    def __isub__(self, other):
        self.value -= int(other)
        return self

    def __imul__(self, other):
        self.value *= int(other)
        return self

    def __itruediv__(self, other):
        self.value /= int(other)
        return self

    def __ifloordiv__(self, other):
        self.value //= int(other)
        return self

    def __imod__(self, other):
        self.value %= int(other)
        return self

    def __ipow__(self, other):
        self.value **= int(other)
        return self

    def __ilshift__(self, other):
        self.value <<= int(other)
        return self

    def __irshift__(self, other):
        self.value >>= int(other)
        return self

    def __iand__(self, other):
        self.value &= int(other)
        return self

    def __ixor__(self, other):
        self.value ^= int(other)
        return self

    def __ior__(self, other):
        self.value |= int(other)
        return self

    def __neg__(self, other) -> IntStruct:
        result = self.value.__neg__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __pos__(self, other) -> IntStruct:
        result = self.value.__pos__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __abs__(self, other) -> IntStruct:
        result = self.value.__abs__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result

    def __invert__(self, other) -> IntStruct:
        result = self.value.__invert__(int(other))
        result = type(self)(result)
        result.dollar = self.dollar.copy()
        return result
    
    def __complex__(self):
        return self.value.__complex__()

    def __int__(self):
        return self.value

    def __float__(self):
        return self.value.__float__()

    def __round__(self) -> IntStruct:
        return self.value.__round__()

    def __trunc__(self) -> IntStruct:
        return self.value.__trunc__()

    def __floord__(self):
        return self.value.__floord__()

    def __ceil__(self) -> IntStruct:
        return self.value.__ceil__()
    
    def __index__(self):
        return self.value

class UnsignedLe(IntStruct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
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

class u24(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(3, value, name)

class u32(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(4, value, name)

class u48(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(6, value, name)

class u64(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(8, value, name)

class u96(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(12, value, name)

class u128(UnsignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(16, value, name)

class SignedLe(IntStruct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)

    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.value = le_to_int(other.read(self.length))
        
        negative_threshold_bytes = b'\x80'
        for _ in range(1,self.length):
            negative_threshold_bytes = b'\x00' + negative_threshold_bytes
        negative_threshold = 0
        for (exponent, byte) in enumerate(negative_threshold_bytes):
            negative_threshold += byte << 8*exponent
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

class s24(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(3, value, name)

class s32(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(4, value, name)

class s48(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(6, value, name)

class s64(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(8, value, name)

class s96(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(12, value, name)

class s128(SignedLe):
    def __init__(self, value: int=0, name: str=""):
        super().__init__(16, value, name)

class RealNum(Struct):
    def __init__(self, length: int, value: float=0.0, name: str=""):
        self.length = length
        self.value = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
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
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
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
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
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
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
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

T = TypeVar('T', bound=Struct)
class Array(list[T], Struct):
    def __init__(self, type_: T, length: int | str) -> None:
        self.type_ = type_
        self.length = length
        list.__init__(self)
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        self.clear()
        if isinstance(self.length, int):
            for _ in range(0, self.length):
                self.append(self.type_() @ other)
                if self[-1].breaked:
                    break
        elif "while" in self.length:
            bool_statement = self.length.split("while(")[1].split(")")[0].replace("_dollar___offset", "other")
            while eval(bool_statement):
                self.append(self.type_() @ other)
                if self[-1].breaked:
                    break
        else:
            raise Exception(f"Array lengths other than int or while statements are not supported. Received length: {self.length}")
        return self


def sizeof(struct: Struct) -> int:
    return struct.size

def addressof(struct: Struct) -> int:
    return struct.address
