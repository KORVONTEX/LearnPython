def merge_sorted_lists(a, b):
    return sorted(set(a + b))

def main():
    list1 = sorted(list(map(int, input("1) Введите числа через пробел: ").split())))
    list2 = sorted(list(map(int, input("2) Введите числа через пробел: ").split())))
    merged = merge_sorted_lists(list1, list2)

    print(merged)


if __name__ == "__main__":
    main()
