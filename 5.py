import math


def main(z, x):
    z.insert(0, "0")
    x.insert(0, "0")
    s = 0
    n = len(x)
    for i in range(1, n):
        s += 8 * (x[i] - z[n - math.ceil(i / 2)] ** 2) ** 3
    return 28 * s


if __name__ == '__main__':
    print(main([0.51, -0.89, -0.32, 0.51, -0.49, 0.13, 0.29],
               [-0.71, 0.84, 0.15, -0.4, -0.17, 0.16, 0.13]))
