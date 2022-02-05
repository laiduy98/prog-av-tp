# LAI KHANG DUY
import argparse
import re


def main():
    parser = argparse.ArgumentParser('One over two')
    parser.add_argument('-f', '--first', help='First file name', default='forbidden.txt')
    args = parser.parse_args()

    i = []

    with open(args.first) as f:
        for line in f.readlines():
            i.append(line.strip())
    password = input('Enter your password here to check: ')

    if re.fullmatch(r'^(?=.*[A-Z])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,12}$', password) and password not in i:
        print('Password OK')
    else:
        print('Your password does not meet the requirements.')


if __name__ == '__main__':
    main()
