# LAI KHANG DUY
import argparse


def main():
    parser = argparse.ArgumentParser('One over two')
    parser.add_argument('-f', '--first', help='First file name', default='forbidden.txt')
    parser.add_argument('-s', '--second', help='Second file name', default='dummy.txt')
    args = parser.parse_args()

    i = []

    with open(args.first) as f:
        for line in f.readlines():
            i.append(line)

    f2 = open("dummy.txt", "w")
    for element in i:
        f2.write(element)


if __name__ == '__main__':
    main()
