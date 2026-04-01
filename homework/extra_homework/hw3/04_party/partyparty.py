def main():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    limit = 6
    sleep = False
    cnt = len(guests)

    while not sleep:
        print(f"Сейчас на вечеринке {cnt} человек: {guests}")
        answer = input("Гость пришёл или ушёл? ").lower()

        if answer == 'пришёл' or answer == 'пришел':
            name = input("Имя гостя: ")
            if cnt == 6:
                print(f"Прости, {name}, но мест нет.\n")
            else:
                print(f"Привет, {name}!\n")
                guests.append(name)
                cnt += 1

        elif answer == 'ушёл' or answer == 'ушел':
            name = input("Имя гостя: ")
            if name in guests:
                print(f"Пока, {name}!\n")
                guests.remove(name)
                cnt -= 1
            else:
                print("Такого гостя на вечеринке нет.\n")

        elif answer == "пора спать":
            print("\nВечеринка закончилась, все легли спать.")
            sleep = True

        else:
            print("Такого варианта ответа нет :(\n")

if __name__ == "__main__":
    main()
