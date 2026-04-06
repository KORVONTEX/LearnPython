import time

RULES = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

class Contestant:
    def __init__(self, nickname):
        self.nick = nickname
        self.win_count = 0

    def add_win(self):
        self.win_count += 1

class Competition:
    def __init__(self):
        self.contestants = []
        self.round_total = 0

    def clear_screen(self):
        print('\n' * 100)

    def press_any_key(self, msg="Нажми Enter..."):
        input(msg)

    def register_players(self):
        self.clear_screen()
        print("=" * 50)
        print("РЕГИСТРАЦИЯ УЧАСТНИКОВ")
        print("=" * 50)

        while True:
            try:
                count = int(input("Количество игроков: "))
                if count > 0:
                    break
                print("Нужно положительное число!")
            except ValueError:
                print("Введите число!")

        for i in range(count):
            name = input(f"Игрок {i + 1}: ").strip()
            if not name:
                name = f"Игрок{i + 1}"
            self.contestants.append(Contestant(name))

    def configure_rounds(self):
        while True:
            try:
                self.round_total = int(input("\nКоличество раундов: "))
                if self.round_total > 0:
                    break
                print("Нужно больше нуля!")
            except ValueError:
                print("Введите целое число!")

    def get_gesture(self, player):
        self.clear_screen()
        print("-" * 40)
        print(f"ХОД: {player.nick}")
        print("-" * 40)

        while True:
            choice = input("Ваш выбор (камень/ножницы/бумага): ").lower().strip()

            if choice in ["камень", "к", "1"]:
                return "камень"
            elif choice in ["ножницы", "н", "2"]:
                return "ножницы"
            elif choice in ["бумага", "б", "3"]:
                return "бумага"

            print("Ошибка! Пиши: камень, ножницы или бумага")

    def determine_winners(self, choices):
        groups = {
            "камень": [],
            "ножницы": [],
            "бумага": []
        }

        for player, gesture in choices:
            groups[gesture].append(player)

        active_gestures = []
        for gesture in ["камень", "ножницы", "бумага"]:
            if groups[gesture]:
                active_gestures.append(gesture)

        if len(active_gestures) == 1 or len(active_gestures) == 3:
            return None

        for gesture in active_gestures:
            if RULES[gesture] in active_gestures:
                return groups[gesture]

        return None

    def show_scoreboard(self):
        print("\n" + "=" * 40)
        print("СЧЕТ ИГРЫ")
        print("=" * 40)

        sorted_players = sorted(self.contestants, key=lambda x: x.win_count, reverse=True)
        for player in sorted_players:
            print(f"{player.nick}: {player.win_count}")
        print("=" * 40)

    def play_round(self, round_number):
        print(f"\n===== РАУНД {round_number} =====")
        self.press_any_key("Готовы? Enter...")

        round_choices = []

        for player in self.contestants:
            gesture = self.get_gesture(player)
            round_choices.append((player, gesture))

            if player != self.contestants[-1]:
                self.press_any_key("Следующий игрок...")

        self.clear_screen()
        print("БОЙ!")
        time.sleep(0.5)
        print("РЕЗУЛЬТАТЫ:")
        print("-" * 30)

        for player, gesture in round_choices:
            print(f"{player.nick} показал: {gesture}")

        print()

        winners = self.determine_winners(round_choices)

        if winners is None:
            print("НИЧЬЯ!")
        else:
            for winner in winners:
                winner.add_win()
            print("ПОБЕДИТЕЛЬ(-ЛИ):")
            for winner in winners:
                print(f"  * {winner.nick}")

        self.show_scoreboard()

    def announce_champion(self):
        self.clear_screen()
        print("=" * 50)
        print("ИТОГИ ТУРНИРА")
        print("=" * 50)

        self.show_scoreboard()

        max_wins = max(player.win_count for player in self.contestants)
        champions = [player for player in self.contestants if player.win_count == max_wins]

        print()
        print("*" * 40)

        if len(champions) == 1:
            print(f"ЧЕМПИОН: {champions[0].nick}!")
        else:
            print("НИЧЬЯ! ПОБЕДИТЕЛИ:")
            for champ in champions:
                print(f"  - {champ.nick}")

        print("*" * 40)

    def start(self):
        self.clear_screen()
        print("=" * 40)
        print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
        print("=" * 40)
        self.press_any_key()

        self.register_players()
        self.clear_screen()
        self.configure_rounds()

        for round_num in range(1, self.round_total + 1):
            self.play_round(round_num)
            if round_num < self.round_total:
                self.press_any_key("\nДальше...")

        self.announce_champion()
        print("\nСПАСИБО ЗА ИГРУ!")


game = Competition()
game.start()
