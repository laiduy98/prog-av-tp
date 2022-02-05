# LAI KHANG DUY
import argparse


def main():
    parser = argparse.ArgumentParser('One over two')
    parser.add_argument('-f', '--file_name', help='First file name', default='forbidden.txt')
    args = parser.parse_args()
    i = 0
    # print(args.file_name)
    with open(args.file_name) as f:
        for line in f.readlines():
            if i % 2 == 0:
                print(line)
            i += 1


if __name__ == '__main__':
    main()
