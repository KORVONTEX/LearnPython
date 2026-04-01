def main():
    n = int(input("Кол-во чисел: "))
    seq = []

    for i in range(n):
        num = int(input("Число: "))
        seq.append(num)

    print(f"\nПоследовательность: {seq}")

    for i in range(n):
        if seq[i:] == seq[i:][::-1]:
            add = seq[:i][::-1]
            print(f"Нужно приписать чисел: {len(add)}")
            print(f"Сами числа: {add}")
            return

if __name__ == "__main__":
    main()
