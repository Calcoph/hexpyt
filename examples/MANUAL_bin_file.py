from bin_file import *
from primitives import u8
def bytes_to_int(bytes_: list[u8]):
    value = 0
    for (exponent, byte) in enumerate(bytes_):
        value += int(byte) * 256**exponent
    return value

with open("binary_files/bin_file.bin", "rb") as f:
    byts = f.read()

file = File("file", Dollar(0x00, byts))

print()
print(f"{file.header.header_name=}")
print(f"{int(file.header.header_size)=:02X}")
print(f"{int(file.header.data_size)=:02X}")
print(f"{int(file.header.element_amount)=}")
for index, datum in enumerate(file.data):
    if datum.flags.f_variable == 1:
        print(f"    datum {index:02}: {bytes_to_int(datum.data)=}")
    elif datum.flags.f_u16 == 1 or datum.flags.f_u32 == 1:
        print(f"    datum {index:02}: {int(datum.data)=}")
