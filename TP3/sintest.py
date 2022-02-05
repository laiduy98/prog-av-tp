from math import sin


def sin_calculator(x):
    return sin(x) / x


def main():
    for i in [x / 2 for x in range(-6, 7, 1)]:
        try:
            print(sin_calculator(i))
        except:
            print('>>>>>>>>>>>Pas possible avec 0.0')


if __name__ == '__main__':
    main()
