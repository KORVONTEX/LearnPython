def main():
    n = int(input("Введите длину списка: "))

    s = [1 if x % 2 == 0 else x % 5 for x in range(n)]

    print(f"Результат: {s}")

if __name__ == "__main__":
    main()
