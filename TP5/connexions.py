# LAI KHANG DUY
import argparse
import datetime
from matplotlib import pyplot as plt
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help='Name of the file', default='error.log')
    args = parser.parse_args()

    date_time_count = {}

    with open(args.file_name) as f:
        for line in f.readlines():
            # take the time out
            line = re.findall("\[(.*?)\]", line)

            if line:
                line = line[0]
                # take only day month year and remove hour minute
                date_time = f'{line.split()[2]} {line.split()[1]} {line.split()[4]}'
                date_time = datetime.datetime.strptime(date_time, '%d %b %Y')

                if date_time in date_time_count:
                    date_time_count[date_time] += 1
                else:
                    date_time_count[date_time] = 1

    dates = list(date_time_count.keys())
    numbers = list(date_time_count.values())
    # ax.plot_date(dates, prices, '-')
    plt.plot(dates, numbers)
    plt.show()


if __name__ == '__main__':
    main()
