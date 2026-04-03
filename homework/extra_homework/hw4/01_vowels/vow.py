def main():
    text = input("Введите текст: ").lower()
    vowels = 'ёуеыаоэяию'

    cnt = [x for x in text if x in vowels]

    print(f"Список гласных букв: {cnt}")
    print(f"Длина списка: {len(cnt)}")

if __name__ == "__main__":
    main()
