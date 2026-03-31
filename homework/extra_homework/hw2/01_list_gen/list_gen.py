def main():
    N = int(input("Введите число: "))
    if N < 1:
        print("N должно быть натуральным числом")
        return
    a = [x for x in range(1, N + 1) if x % 2 != 0]
    print(f"Список из нечётных чисел от одного до N: {a}")

if __name__ == "__main__":
    main()
