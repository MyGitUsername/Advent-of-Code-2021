def binary_to_decimal(binary):
   return int(binary, 2)

def hex_to_binary(hex):
    bin_str = ''
    for c in hex:
        bin_str += bin(int(c, 16))[2:].zfill(4)# f'Ox{hex}:0>4b'
    return bin_str

def decode_version(blob):
    return binary_to_decimal(blob[:3])

def decode_typeID(blob):
    return binary_to_decimal(blob[3:6])

