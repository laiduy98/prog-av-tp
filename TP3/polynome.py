def polynome(x):
    return 3 * x ** 2 + 5 * x - 10


def main():
    print(polynome(0))
    # range cannot take step as float
    # so instead put x/2 and step == 1
    for i in [x / 2 for x in range(-10, 11, 1)]:
        print(f'P({i})={polynome(i)}')


if __name__ == '__main__':
    main()
