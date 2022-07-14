from primitives import Dollar, Struct, u8, u16, u32, u64, u128, s8, s16, s32, s64, s128, Float, double, char, char16, Bool, Padding, BitField, sizeof, addressof


class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good{
    u8 a;
};
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
        a: u8 = u8('a', _dollar___offset)
        self.a = a
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good {
    u8 a;
};
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
        a: u8 = u8('a', _dollar___offset)
        self.a = a
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good        {
    u8 a;
};
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
        a: u8 = u8('a', _dollar___offset)
        self.a = a
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good        {
    u8 a;
} // Even though hexpat needs a ; at the end of the structs, hexpyt doesn't
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
        a: u8 = u8('a', _dollar___offset)
        self.a = a
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Bad(Struct):
    """
hexpat definition:
```hexpat
struct Bad
{ // This opening bracket should be in the line above

};
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
        : # This opening bracket should be in the line above
            
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good {
    u8 goodIf;
    if (goodIf){
        u8 nice;
    }
}
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
            goodIf: u8 = u8('goodIf', _dollar___offset)
            self.goodIf = goodIf
            if (goodIf):
                nice: u8 = u8('nice', _dollar___offset)
                self.nice = nice
            
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good {
    u8 goodIf;
    if (goodIf) {
        u8 nice;
    }
}
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
            goodIf: u8 = u8('goodIf', _dollar___offset)
            self.goodIf = goodIf
            if (goodIf):
                nice: u8 = u8('nice', _dollar___offset)
                self.nice = nice
            
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Good(Struct):
    """
hexpat definition:
```hexpat
struct Good {
    u8 goodIf;
    if (goodIf)  { // here the code will mess up and translate to <if (goodIf) :> instead of <if (goodIf):>. But python doesn't care, so still good
        u8 nice;
    }
}
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
            goodIf: u8 = u8('goodIf', _dollar___offset)
            self.goodIf = goodIf
            if (goodIf) : # here the code will mess up and translate to <if (goodIf) :> instead of <if (goodIf):>. But python doesn't care, so still good
                nice: u8 = u8('nice', _dollar___offset)
                self.nice = nice
            
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Bad(Struct):
    """
hexpat definition:
```hexpat
struct Bad {
    u8 badIf;
    if (badIf)
    { // Same as with structs, this bracked should be in the line above
        u8 nice;
    }
}
```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
            badIf: u8 = u8('badIf', _dollar___offset)
            self.badIf = badIf
            if (badIf)
            : # Same as with structs, this bracked should be in the line above
                nice: u8 = u8('nice', _dollar___offset)
                self.nice = nice
            
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())

class Bad(Struct):
    """
hexpat definition:
```hexpat
struct Bad {
    u8 badIf;
    if (badIf) // Even if there is only 1 line, there must be brackets.
        // This is not a critical failure, you can manually fix it in the.py after (see bad_and_good_examples.py to see what it would output)
        u8 nice;
}```"""
    def __init__(self, _thisstruct_s_name: str, _dollar___offset: Dollar):
        """
        struct

        Args:
            _thisstruct_s_name (str): The name of this instance. Can be whatever you want or just an empty string
            _dollar___offset (Dollar): Dollar pointing to the start of this struct
        """
        _dollar___offset_copy = _dollar___offset.copy()
            badIf: u8 = u8('badIf', _dollar___offset)
            self.badIf = badIf
            if (badIf) # Even if there is only 1 line, there must be brackets.
            # This is not a critical failure, you can manually fix it in the.py after (see bad_and_good_examples.py to see what it would output)
            nice: u8 = u8('nice', _dollar___offset)
            self.nice = nice
        super().__init__(_thisstruct_s_name, _dollar___offset_copy, _dollar___offset.copy())
