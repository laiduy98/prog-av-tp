def is_pythagoricien(x, y, z):
    if x < y < z:
        if x ** 2 + y ** 2 == z ** 2:
            return True
        else:
            return False
    else:
        return False


def main():
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if is_pythagoricien(x, y, z):
                    print(f'x={x}, y={y}, z={z}')


if __name__ == '__main__':
    main()
