bitfield Flags {
    unused: 4;
    f_variable: 1;
    // This comment will appear in the .py file
    f_u16: 1; // This comment won't appear in the .py file. But it will in the docstring
    f_u32: 1;
};

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

struct Header {
    char header_name[8];
    u32 header_size;
    u32 data_size;
    u8 element_amount;
};

struct File {
    Header header;
    padding[3];
    Data data[header.element_amount];
};

// The line below will be translated to python, but it won't run because 0x00 is an int instead of a dollar
// Manually replace the line below.
// from:
//     @ (0x00)
// to:
//     @ Dollar(0x00, byts)
File file @ 0x00;
