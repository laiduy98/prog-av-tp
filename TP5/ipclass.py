# LAI KHANG DUY
from matplotlib import pyplot as plt
import argparse
import re


def check_class_ip(ip):

    if ip <= 127:
        return 'class A'
    elif 128 <= ip < 191:
        return 'class B'
    elif 191 <= ip <= 223:
        return 'class C'
    else:
        return 'other'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help='Name of the file', default='access_short.log')
    args = parser.parse_args()

    ip_type = {}

    with open(args.file_name) as f:
        for line in f.readlines():
            ip = re.findall('\\S+', line)[0]
            ip_class = check_class_ip(int(ip.split('.')[0]))

            if ip_class:
                if ip_class in ip_type:
                    ip_type[ip_class] += 1
                else:
                    ip_type[ip_class] = 1

    labels = []
    sizes = []

    for x, y in ip_type.items():
        labels.append(x)
        sizes.append(y)

    plt.pie(sizes, labels=labels, autopct='%1.0f%%')

    plt.axis('equal')

    plt.show()


if __name__ == '__main__':
    main()
