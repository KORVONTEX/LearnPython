def main():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]

    cnt = int(input("Сколько песен выбрать? "))
    names_list = [x[0] for x in violator_songs]
    new = []
    total = 0

    for i in range(1, cnt + 1):
        name = input(f"Название {i}-й песни: ")

        if name in new:
            print("Эта песня уже добавлена!")
            continue

        if name not in names_list:
            print("Такой песни нет!")
            continue

        for names in violator_songs:
            if names[0] == name:
                total += names[1]
                new.append(name)
                break

    print(f"\nОбщее время звучания песен: {round(total, 2)} мин.")

if __name__ == "__main__":
    main()
