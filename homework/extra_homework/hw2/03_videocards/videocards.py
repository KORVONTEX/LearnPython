def main():
    n = int(input("Количество видеокарт: "))
    cards = []

    for i in range(1, n + 1):
        card = int(input(f"{i} Видеокарта: "))
        cards.append(card)

    max_card = max(cards)
    new_cards = [x for x in cards if x != max_card]

    print(f"Старый список видеокарт: {cards}")
    print(f"Новый список видеокарт: {new_cards}")

if __name__ == "__main__":
    main()
