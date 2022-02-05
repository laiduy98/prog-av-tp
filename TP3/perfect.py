def is_parfait(num):
    sum_num = 0
    for i in range(1, num):
        if num % i == 0:
            sum_num = sum_num + i
    if sum_num == num:
        return True
    else:
        return False


def main():
    for i in range(1, 1000):
        print(i) if is_parfait(i) else None


if __name__ == '__main__':
    main()
