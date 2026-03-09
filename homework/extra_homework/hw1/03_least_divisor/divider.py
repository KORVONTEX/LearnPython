def divider(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return d
    return n

def main():
    try:
        n = int(input("Введите число: "))
        if n <= 1:
            print("Ошибка: число должно быть натуральным и больше 1")
            return
        d = divider(n)
        print(f"Наименьший делитель, отличный от единицы: {d}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
