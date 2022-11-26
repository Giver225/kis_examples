import math


def main(x):
    return 24 * x ** 15 -\
           math.ceil(62 * x - x ** 2) +\
           math.sqrt((7 * x ** 4) /
                     ((math.log10(x ** 3) ** 5) / 42 +
                      5 * math.log(x) ** 4))


if __name__ == '__main__':
    print(main(0.33))
