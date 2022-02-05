def main():
    # 1.
    l = [9, 7, 3, 2, 7, 8, 3, 8, 4, 2, 7, 0, 5, 3, 2, 0, 9, 6, 0, 5, 6, 2, 2, 4, 5, 2, 6, 3, 5, 2]
    print(l)
    # 2.
    odd_only = [x for x in l if x % 2 == 1]
    print(odd_only)
    # 3.
    even_only = [x for x in l if x % 2 == 0]
    print(even_only)
    # 4.
    even_only_four = [x for x in even_only if x > 4]
    print(even_only_four)


if __name__ == '__main__':
    main()
