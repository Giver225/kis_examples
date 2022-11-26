import math


def main(n):
    if n == 0:
        return -0.73
    elif n == 1:
        return 0.68
    elif n >= 2:
        return math.atan(main(n - 2) ** 3) \
               - main(n - 1) ** 2


if __name__ == '__main__':
    print(main(6))
