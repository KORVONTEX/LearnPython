def main():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    name = input("Название детали: ").lower()

    cnt = 0
    total = 0

    for detal in shop:
        if detal[0] == name:
            cnt += 1
            total += detal[1]

    if cnt == 0:
        print("Такой детали нет :(")
        return

    print(f"Количество деталей - {cnt}")
    print(f"Общая стоимость - {total}")

if __name__ == "__main__":
    main()
