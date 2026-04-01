def main():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]

    a.extend(b)
    cnt_5 = a.count(5)

    print("Результат работы программы:")
    print(f"Кол-во цифр 5 при первом объединении: {cnt_5}")

    while 5 in a:
        a.remove(5)

    a.extend(c)
    cnt_3 = a.count(3)

    print(f"Кол-во цифр 3 при втором объединении: {cnt_3}")
    print(f"Итоговый список: {a}")

if __name__ == "__main__":
    main()
