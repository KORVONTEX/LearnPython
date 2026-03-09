def sum_of_digits(n):
    return sum(map(int, str(n)))

def count_digits(n):
    return len(str(n))

def main():
    n = int(input("Введите число: "))

    s = sum_of_digits(n)
    c = count_digits(n)
    diff = abs(s - c)

    print(f"Сумма чисел: {s}")
    print(f"Количество цифр в числе: {c}")
    print(f"Разность суммы и количества цифр: {diff}")

if __name__ == "__main__":
    main()
