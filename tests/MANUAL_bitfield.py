from bitfield import *
# file_path = "../examples/binary_files/bin_file.bin"
assert b1.a == 0
print(b1.a)
print(b1.b)
print(b1.c)
print(b1.d)
print(b1.e)
assert b1.b == 1
assert b1.c == 0
assert b1.d == 0
assert b1.e == 0

assert b2.a == 0
assert b2.b == 0
assert b2.c == 0
assert b2.d == 0
assert b2.e == 4
assert b2.f == 34
assert b2.g == 5
assert b2.h == 10
assert b2.i == 72

assert b3.a == 17736

assert b4.a == 83272

assert b5.a == 1
assert b5.b == 17736

assert b6.a == 4
assert b6.b == 83272

assert b7.a == 10409
assert b7.b == 0

assert b8.a == 534697
assert b8.b == 0
