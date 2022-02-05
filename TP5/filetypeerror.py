# LAI KHANG DUY
import argparse
import datetime
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help='Name of the file', default='error.log')
    args = parser.parse_args()

    file_date = {}

    with open(args.file_name) as f:
        for line in f.readlines():
            file = re.findall('/\S+', line)

            if file:
                file = file[-1]
                date_time = line.split(']')[0][1:]
                date = f'{date_time.split()[2]} {date_time.split()[1]} {date_time.split()[4]}'
                date = datetime.datetime.strptime(date, '%d %b %Y')

                if file in file_date:
                    file_date[file][1] = date
                else:
                    file_date[file] = [date, date]

    for key, value in file_date.items():
        print(f"{key}: {value[0].strftime('%d/%m/%Y')} {value[1].strftime('%d/%m/%Y')}")

    # print('...')
    # print(f'{len(file_count)} urls en défaut')


if __name__ == '__main__':
    main()
