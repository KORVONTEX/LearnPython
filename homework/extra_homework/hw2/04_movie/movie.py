def main():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
    favorites = []

    n = int(input("Сколько фильмов хотите добавить? "))

    for i in range(1, n + 1):
        name = input("Введите название фильма: ")

        if name not in films:
            print(f"Ошибка: фильма {name} у нас нет :(")
            continue

        favorites.append(name)

    print(f"Ваш список любимых фильмов: {', '.join(favorites)}")

if __name__ == "__main__":
    main()
