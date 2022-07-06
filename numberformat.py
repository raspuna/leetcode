def print_formatted(number):
    for i in range(1, number+1):
        padding = len(bin(number))
        print(i)
        print(oct(i), type(oct(i)))
        print(f"%6d%6s%6s%6s" % (i, oct(i)[2:], hex(i)[2:], bin(i)[2:]))
        print(f"% *d%" % (padding, i))

print_formatted(17)