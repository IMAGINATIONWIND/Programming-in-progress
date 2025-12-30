bin_num = (input("KINDLY ENTER THE NUMBER ( MUST BE IN BINARY ): "))
deci_num = int(bin_num , 2)
hex_conv = hex(deci_num).upper()
octal_conv = int(bin_num , 8)
print(f"THE OCTAL CONV IS : {octal_conv}")
print(f"BINARY {bin_num} TO HEXADECIMAL {hex_conv}")
# to convert others into binary u just use bin()
bin_conv = bin(int(hex_conv , 16))[2:]
print(f"THE BINARY BACK {bin_conv} FROM HEX {hex_conv}")