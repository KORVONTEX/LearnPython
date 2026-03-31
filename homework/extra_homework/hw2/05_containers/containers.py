def main():
    n = int(input("Количество контейнеров: "))

    if n < 1:
        print("N должно быть натуральным")
        return

    limit = 200
    containers = []

    for i in range(1, n + 1):
        m = int(input(f"Введите вес контейнера: "))

        if m > 200:
            print("Превышен весовой лимит!")
            continue

        containers.append(m)

    containers = sorted(containers)[::-1]
    x = int(input("Введите вес нового контейнера: "))

    cnt = 1

    for i in range(len(containers)):
        if x > containers[i]:
            print(f"Номер, который получит новый контейнер: {cnt}")
            return
        else:
            cnt += 1
    print(f"Номер, который получит новый контейнер: {cnt}")

if __name__ == "__main__":
    main()
