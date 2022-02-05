# LAI KHANG DUY
import argparse
import re


def main():
    parser = argparse.ArgumentParser('One over two')
    parser.add_argument('-f', '--file_name', help='First file name', default='test.html')
    args = parser.parse_args()

    i = []

    with open(args.file_name) as f:
        for line in f.readlines():
            i.append(re.sub(r"<[^>]*>", "", line))

    f2 = open(f"{args.file_name.split('.')[0]}.nohtml", "w")
    for element in i:
        f2.write(element)
    f2.close()


if __name__ == '__main__':
    main()
