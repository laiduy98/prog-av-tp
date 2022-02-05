# LAI KHANG DUY
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help='Name of the file', default='error.log')
    args = parser.parse_args()

    file_count = {}

    with open(args.file_name) as f:
        for line in f.readlines():
            file = re.findall('/\S+', line)

            if file:
                file = file[-1]
                if file in file_count:
                    file_count[file] += 1
                else:
                    file_count[file] = 1

    for key, value in file_count.items():
        print(f"{key}: {value}")

    print('...')
    print(f'{len(file_count)} urls en défaut')


if __name__ == '__main__':
    main()
