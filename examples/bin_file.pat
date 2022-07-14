bitfield Flags {
    unused: 4;
    f_variable: 1;
    f_u16: 1;
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

// The line below won't be translated to python, it will be ignored
File file @ 0x00;
