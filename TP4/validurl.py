# LAI KHANG DUY
import re


def main():
    url = input('Enter your url here to check: ')

    if re.fullmatch(r"(http|ftp|https)://([\w_-]+(?:\.[\w_-]+)+)([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])", url):
        print('URL OK')
    else:
        print('Your URL is incorrect.')


if __name__ == '__main__':
    main()
