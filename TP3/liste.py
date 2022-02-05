def main():
    # 1.
    l = [9, 7, 3, 2, 7, 8, 3, 8, 4, 2, 7, 0, 5, 3, 2, 0, 9, 6, 0, 5, 6, 2, 2, 4, 5, 2, 6, 3, 5, 2]
    print(l)
    # 2.
    print(len(l))
    # 3.
    print(sum(1 for i in l if i == 7))
    # 4.
    l.append(9)
    # 5.
    l.remove(7)
    print(l)
    # 6.
    print(sum(1 for i in l if i == 7))
    # 7.
    print(l[::-1])
    # 8.
    l.sort()
    print(l)
    # 9.
    print(l[-5:])
    # 10.
    l_non_duplicated = list(set(l))
    print(l_non_duplicated[-5:])


if __name__ == '__main__':
    main()
