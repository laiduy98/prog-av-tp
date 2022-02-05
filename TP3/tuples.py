def minmax(l):
    l_non_duplicated = list(set(l))
    l_non_duplicated.sort()
    #      Min                  Max
    return l_non_duplicated[0], l_non_duplicated[-1]


def main():
    l = [9, 7, 3, 2, 7, 8, 3, 8, 4, 2, 7, 0, 5, 3, 2, 0, 9, 6, 0, 5, 6, 2, 2, 4, 5, 2, 6, 3, 5, 2]
    num_min, num_max = minmax(l)

    mean_min_max = (num_max + num_min) / 2

    print(mean_min_max)


if __name__ == '__main__':
    main()
