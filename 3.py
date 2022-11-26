import math


def main(b, z, n, m):
    s1 = 0
    for i in range(1, b + 1):
        s1 += math.sqrt(1 + i ** 3 + 88 * z) + z ** 3
    s2 = 0
    for k in range(1, m + 1):
        s3 = 0
        for i in range(1, n + 1):
            s3 += 95 + 74 * i ** 6 + k ** 14
        s2 += s3
    return s1 + s2


if __name__ == '__main__':
    print(main(4, 0.5, 4, 4))
