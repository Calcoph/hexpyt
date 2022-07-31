from __future__ import annotations
import struct
from typing import Type, TypeVar, Union

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
        self.____name________ = name
        self.___breaked___ = False
    
    def init_struct(self, starting_offset: Dollar, end_offset: Dollar):
        self.__address____ = starting_offset.offset
        self.___dollar______ = end_offset
        self.__size_______ = end_offset.offset - self.__address____
    
    def name(self) -> str:
        return self.____name________
    
    def breaked(self) -> bool:
        return self.___breaked___
    
    def dollar(self) -> Dollar:
        return self.___dollar______
    
    def size(self) -> int:
        self.__size_______

class IntStruct(Struct):
    def __init__(self, name: str=""):
        self.___value_____: int
        super().__init__(name)
    
    def value(self) -> int:
        self.___value_____

    def to_dollar(self) -> Dollar:
        return Dollar(self.___value_____, self.___dollar______.byts)

    def __repr__(self) -> str:
        return self.___value_____.__repr__()
    
    def __str__(self) -> str:
        return self.___value_____.__str__()

    def __format__(self, format_spec) -> str:
        return self.___value_____.__format__(format_spec)

    def __lt__(self, other) -> bool:
        return self.___value_____.__lt__(int(other))

    def __le__(self, other) -> bool:
        return self.___value_____.__le__(int(other))

    def __eq__(self, other) -> bool:
        return self.___value_____.__eq__(int(other))

    def __ne__(self, other) -> bool:
        return self.___value_____.__ne__(int(other))

    def __gt__(self, other) -> bool:
        return self.___value_____.__gt__(int(other))

    def __ge__(self, other) -> bool:
        return self.___value_____.__ge__(int(other))
    
    def __hash__(self) -> int:
        return self.___value_____.__hash__()
    
    def __bool__(self) -> bool:
        return self.___value_____.__bool__()
    
    def __add__(self, other) -> IntStruct:
        result = self.___value_____.__add__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __sub__(self, other) -> IntStruct:
        result = self.___value_____.__sub__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __mul__(self, other) -> IntStruct:
        result = self.___value_____.__mul__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __truediv__(self, other):
        return self.___value_____.__truediv__(int(other))

    def __floordiv__(self, other) -> IntStruct:
        result = self.___value_____.__floordiv__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __mod__(self, other) -> IntStruct:
        result = self.___value_____.__mod__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __divmod__(self, other):
        return self.___value_____.__divmod__(other)

    def __pow__(self, other) -> IntStruct:
        result = self.___value_____.__pow__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __lshift__(self, other) -> IntStruct:
        result = self.___value_____.__lshift__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rshift__(self, other) -> IntStruct:
        result = self.___value_____.__rshift__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result
    
    def __and__(self, other) -> IntStruct:
        result = self.___value_____.__and__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __xor__(self, other) -> IntStruct:
        result = self.___value_____.__xor__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __radd__(self, other) -> IntStruct:
        result = self.___value_____.__radd__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rsub__(self, other) -> IntStruct:
        result = self.___value_____.__rsub__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rmul__(self, other) -> IntStruct:
        result = self.___value_____.__rmul__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rtruediv__(self, other) -> IntStruct:
        result = self.___value_____.__rtruediv__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rfloordiv__(self, other) -> IntStruct:
        result = self.___value_____.__rfloordiv__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rmod__(self, other) -> IntStruct:
        result = self.___value_____.__rmod__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rdivmod__(self, other):
        return self.___value_____.__rdivmod__(int(other))

    def __rpow__(self, other):
        return self.___value_____.__rpow__(int(other))

    def __rlshift__(self, other) -> IntStruct:
        result = self.___value_____.__rlshift__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rrshift__(self, other) -> IntStruct:
        result = self.___value_____.__rrshift__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rand__(self, other) -> IntStruct:
        result = self.___value_____.__rand__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __rxor__(self, other) -> IntStruct:
        result = self.___value_____.__rxor__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __ror__(self, other) -> IntStruct:
        result = self.___value_____.__ror__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __iadd__(self, other):
        self.___value_____ += int(other)
        return self

    def __isub__(self, other):
        self.___value_____ -= int(other)
        return self

    def __imul__(self, other):
        self.___value_____ *= int(other)
        return self

    def __itruediv__(self, other):
        self.___value_____ /= int(other)
        return self

    def __ifloordiv__(self, other):
        self.___value_____ //= int(other)
        return self

    def __imod__(self, other):
        self.___value_____ %= int(other)
        return self

    def __ipow__(self, other):
        self.___value_____ **= int(other)
        return self

    def __ilshift__(self, other):
        self.___value_____ <<= int(other)
        return self

    def __irshift__(self, other):
        self.___value_____ >>= int(other)
        return self

    def __iand__(self, other):
        self.___value_____ &= int(other)
        return self

    def __ixor__(self, other):
        self.___value_____ ^= int(other)
        return self

    def __ior__(self, other):
        self.___value_____ |= int(other)
        return self

    def __neg__(self, other) -> IntStruct:
        result = self.___value_____.__neg__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __pos__(self, other) -> IntStruct:
        result = self.___value_____.__pos__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __abs__(self, other) -> IntStruct:
        result = self.___value_____.__abs__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result

    def __invert__(self, other) -> IntStruct:
        result = self.___value_____.__invert__(int(other))
        result = type(self)(result)
        result.___dollar______ = self.___dollar______.copy()
        return result
    
    def __complex__(self):
        return self.___value_____.__complex__()

    def __int__(self):
        return self.___value_____

    def __float__(self):
        return self.___value_____.__float__()

    def __round__(self) -> IntStruct:
        return self.___value_____.__round__()

    def __trunc__(self) -> IntStruct:
        return self.___value_____.__trunc__()

    def __floord__(self):
        return self.___value_____.__floord__()

    def __ceil__(self) -> IntStruct:
        return self.___value_____.__ceil__()
    
    def __index__(self):
        return self.___value_____

class UnsignedLe(IntStruct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.___length_______ = length
        self.___value_____ = value
        super().__init__(name)
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value_____ = le_to_int(other.read(self.___length_______))
        super().init_struct(starting_offset, other.copy())
        return self
    
    def length(self) -> int:
        return self.___length_______

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
        self.___length_____ = length
        self.___value_____ = value
        super().__init__(name)

    def length(self) -> int:
        return self.___length_____

    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value_____ = le_to_int(other.read(self.___length_____))
        
        negative_threshold_bytes = b'\x80'
        for _ in range(1,self.___length_____):
            negative_threshold_bytes = b'\x00' + negative_threshold_bytes
        negative_threshold = 0
        for (exponent, byte) in enumerate(negative_threshold_bytes):
            negative_threshold += byte << 8*exponent
        max_ = negative_threshold*2+1
        self.___value_____ = -(max_ - self.___value_____)-1
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
        self.___length________ = length
        self.___value_______ = value
        super().__init__(name)
    
    def length(self) -> int:
        return self.___length________
    
    def value(self) -> float:
        return self.___value_______
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value_______ = other.read(self.___length________)
        if self.___length________ == 4:
            format_ = "<f"
        elif self.___length________ == 8:
            format_ = "<d"
        self.___value_______ = struct.unpack(format_, self.___value_______)
        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return self.___value_______.__repr__()
    
    def __str__(self):
        return self.___value_______.__str__()

    def __format__(self, format_spec):
        return self.___value_______.__format__(format_spec)

class Float(RealNum):
    def __init__(self, value: float=0.0, name: str=""):
        super().__init__(4, value, name)

class double(RealNum):
    def __init__(self, value: float=0.0, name: str=""):
        super().__init__(8, value, name)

class Character(Struct):
    def __init__(self, length: int, value: str="\0", name: str=""):
        self.___length_____ = length
        self.___value_____ = value
        super().__init__(name)
    
    def length(self) -> int:
        return self.___length_____
    
    def value(self) -> str:
        return self.___value_____

    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value_____ = other.read(self.___length_____)
        self.___value_____ = "".join(map(chr, self.___value_____))
        super().init_struct(starting_offset, other.copy())
        return self

    def __repr__(self):
        return self.___value_____.__repr__()
    
    def __str__(self):
        return self.___value_____.__str__()

    def __format__(self, format_spec):
        return self.___value_____.__format__(format_spec)

class char(Character):
    def __init__(self, value: str="\0", name: str=""):
        super().__init__(1, value, name)

class char16(Character):
    def __init__(self, value: str="\0\0", name: str=""):
        super().__init__(2, value, name)

class Bool(Struct):
    def __init__(self, value: bool=False, name: str="", false_range=range(0x00,0x01), true_range=range(0x01,0xFF)):
        self.___false_range_____ = false_range
        self.___true_range_____ = true_range
        self.___value_____ = value
        super().__init__(name)
    
    def false_range(self) -> range:
        return self.false_range

    def true_range(self) -> range:
        return self.true_range
    
    def value(self) -> bool:
        return self.___value_____

    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value_____ = le_to_int(other.read(1))
        if self.___false_range_____ == range(0x00,0x01):
            if self.___value_____ in self.___true_range_____:
                self.___value_____ = True
            else:
                self.___value_____ = False
        else:
            if self.___value_____ in self.___false_range_____:
                self.___value_____ = False
            else:
                self.___value_____ = True

        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return self.___value_____.__repr__()
    
    def __str__(self):
        return self.___value_____.__str__()

    def __format__(self, format_spec):
        return self.___value_____.__format__(format_spec)

class Padding(Struct):
    def __init__(self, length: int, value: int=0, name: str=""):
        self.___length______ = length
        self.___value___ = value
        super().__init__(name)
    
    def length(self) -> int:
        return self.___length______
    
    def value(self) -> int:
        return self.___value___

    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        starting_offset = other.copy()
        self.___value___ = other.read(self.___length______)
        super().init_struct(starting_offset, other.copy())
        return self
    
    def __repr__(self):
        return f"padding[{self.___length______}]"
    
    def __str__(self):
        return f"padding[{self.___length______}]"

    def __format__(self, format_spec):
        return f"padding[{self.___length______}]".__format__(format_spec)

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
    def __init__(self, type_: Type[T], length: int | str, name: str="") -> None:
        self.___type_____ = type_
        self.___length__ = length
        list.__init__(self)
        Struct.__init__(self, name)
    
    def __matmul__(self, other):
        if not (isinstance(other, Dollar) or isinstance(other, IntStruct)):
            raise Exception(f'An object of class "Dollar" must be used with the "@" operator. {type(other)} was used instead')
        if isinstance(other, IntStruct):
            other = other.to_dollar()
        other_copy = other.copy()
        self.clear()
        if isinstance(self.___length__, int) or isinstance(self.___length__, IntStruct):
            for _ in range(0, self.___length__):
                self.append(self.___type_____() @ other)
                if self[-1].___breaked___:
                    break
        elif "while" in self.___length__:
            bool_statement = self.___length__.split("while(")[1].split(")")[0].replace("_dollar___offset", "other")
            while eval(bool_statement):
                self.append(self.___type_____() @ other)
                if self[-1].___breaked___:
                    break
        else:
            raise Exception(f"Array lengths other than int or while statements are not supported. Received length: {self.___length__}")
        Struct.init_struct(self, other_copy, other.copy())
        return self

class EnumException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

V = TypeVar('V', bound=IntStruct|RealNum|Character|Bool)

class Enum(UnsignedLe):
    __lengthed__types_____ = [type(UnsignedLe), type(SignedLe), type(RealNum), type(Character), type(Bool)]
    def __init__(self, type_: Type[V]|int, value: V=None, name: str=""):
        if isinstance(type_, int):
            byte_amount = type_
        elif type(type_) in self.__lengthed__types_____:
            byte_amount = type_().length()
        elif type(type_) == type(Bool):
            byte_amount = 1
        else:
            errormsg = "Enum types must be one of the following: \n"
            errormsg += "\tan integer (amount of bytes per enum value)\n"
            errormsg += "\tUnsignedLe: u8, u16, ...\n"
            errormsg += "\tSignedLe: s8, s16, ...\n"
            errormsg += "\tFloat, double\n"
            errormsg += "\tchar, char16\n"
            errormsg += "\tBool"
            raise EnumException(errormsg)
        super().__init__(byte_amount, value, name)

    def name(self) -> str:
        if super().name(self) != "":
            name = super().name(self)
            if self.value() in self._enum__dict___:
                name = f"{name}: {self._enum__dict___[self.value()]}"
            else:
                name = f"{name}: ???"
        else:
            if self.value() in self._enum__dict___:
                name = f"{self._enum__dict___[self.value()]}"
            else:
                name = f"???"
        return name

def sizeof(struct: Struct) -> int:
    return struct.__size_______

def addressof(struct: Struct) -> int:
    return struct.__address____
