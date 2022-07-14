// The code right now is very picky, here are a few things that will mess up the script
struct Good{
    u8 a;
};

struct Good {
    u8 a;
};

struct Good        {
    u8 a;
};

struct Good        {
    u8 a;
} // Even though hexpat needs a ; at the end of the structs, hexpyt doesn't

struct Bad
{ // This opening bracket should be in the line above

};

struct Good {
    u8 goodIf;
    if (goodIf){
        u8 nice;
    }
}

struct Good {
    u8 goodIf;
    if (goodIf) {
        u8 nice;
    }
}

struct Good {
    u8 goodIf;
    if (goodIf)  { // here the code will mess up and translate to <if (goodIf) :> instead of <if (goodIf):>. But python doesn't care, so still good
        u8 nice;
    }
}

struct Bad {
    u8 badIf;
    if (badIf)
    { // Same as with structs, this bracked should be in the line above
        u8 nice;
    }
}

struct Bad {
    u8 badIf;
    if (badIf) // Even if there is only 1 line, there must be brackets.
        // This is not a critical failure, you can manually fix it in the.py after (see bad_and_good_examples.py to see what it would output)
        u8 nice;
}