// The values in the comments in the comments are the ones when reading examples/binary_files/bin_file.bin in imhex

bitfield bit1 {
	a: 1; // 0
	b: 1; // 1
	c: 1; // 0
	d: 1; // 0
	e: 1; // 0
};

bitfield bit2 {
	a: 7; // 0
	b: 7; // 0
	c: 7; // 0
	d: 7; // 0
	e: 7; // 4 = 100
	f: 7; // 34 = 100010
	g: 7; // 5 = 101
	h: 7; // 10 = 1010
	i: 7; // 72 = 1001000
};

bitfield bit3 {
	a: 16; // 17736 = 100010101001000
};

bitfield bit4 {
	a: 20; // 83272 = 10100010101001000
};

bitfield bit5 {
	a: 3; // 1
	b: 16; // 17736 = 100010101001000
};

bitfield bit6 {
	a: 3; // 4 = 100
	b: 20; // 83272 = 10100010101001000
};

bitfield bit7 {
	a: 16; // 10409 = 10100010101001
	b: 3; // 0
};

bitfield bit8 {
	a: 20; // 534697 = 10000010100010101001
	b: 3; // 0
};

bit1 b1 @ 0x00;
bit2 b2 @ 0x00;
bit3 b3 @ 0x00;
bit4 b4 @ 0x00;
bit5 b5 @ 0x00;
bit6 b6 @ 0x00;
bit7 b7 @ 0x00;
bit8 b8 @ 0x00;
