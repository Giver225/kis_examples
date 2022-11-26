def main(x):
    f = (0x80000000 & x) >> 27
    e = (0x7C000000 & x) >> 21
    d = (0x03C00000 & x) >> 22
    c = (0x003FC000 & x) << 10
    b = (0x00003F80 & x) << 3
    a = (0x0000007F & x) << 17
    return c | b | a | d | e | f


if __name__ == '__main__':
    print(hex(main(0x8f84e0b0)))
