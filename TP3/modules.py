import random
import statistics


def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


def main():
    # 1.
    random_list = rand(10, 20, 20)
    print(random_list)
    # 2.
    average = statistics.mean(random_list)
    # average = sum(random_list)/len(random_list)
    print(average)
    # 3.
    smaller_than_average = [x for x in random_list if x <= average]
    print(smaller_than_average)
    # 4.
    greater_than_average = [x for x in random_list if x > average]
    print(greater_than_average)
    # 5.
    median = statistics.median(random_list)
    print(median)
    # 6.
    smaller_than_median = [x for x in random_list if x <= median]
    print(smaller_than_median)
    # 7.
    greater_than_median = [x for x in random_list if x > median]
    print(greater_than_median)


if __name__ == '__main__':
    main()
