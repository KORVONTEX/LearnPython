def main():
    cnt_skates = int(input("Кол-во коньков: "))
    if cnt_skates < 0:
        print("Коньков не может быть меньше чем нисколько!")
        return
    skates = []

    for i in range(1, cnt_skates + 1):
        size = int(input(f"Размер {i}-й пары: "))

        if size < 1:
            print("Нулевого размера и меньше нет...")
            return

        skates.append(size)

    cnt_humans = int(input("\nКол-во людей: "))
    if cnt_humans < 0:
        print("Людей не может быть меньше чем нисколько!")
        return
    humans = []

    for i in range(1, cnt_humans + 1):
        size = int(input(f"Размер ноги {i}-го человека: "))

        if size < 1:
            print("Нулевого размера и меньше нет...")
            return

        humans.append(size)

    humans.sort()
    skates.sort()
    total = i = j = 0

    while i < len(humans) and j < len(skates):
        if skates[j] == humans[i]:
            total += 1
            i += 1
            j += 1
        elif skates[j] < humans[i]:
            j += 1
        else:
            i += 1

    print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {total}")

if __name__ == "__main__":
    main()
