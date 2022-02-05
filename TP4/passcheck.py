# LAI KHANG DUY
import re


def main():
    password = input('Enter your password here to check: ')

    if re.fullmatch(r'^(?=.*[A-Z])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,12}$', password):
        print('Password OK')
    else:
        print('Your password is not meet the requirements.')


if __name__ == '__main__':
    main()
