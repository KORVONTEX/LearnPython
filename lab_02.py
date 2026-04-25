class Element:
    def __init__(self, name):
        self.name = name
        self.discovered = False

class Recipe:
    def __init__(self, element1, element2, result):
        self.element1 = element1
        self.element2 = element2
        self.result = result

    def matches(self, e1, e2):
        return (e1 == self.element1 and e2 == self.element2) or \
            (e1 == self.element2 and e2 == self.element1)

class AlchemyGame:
    def __init__(self):
        self.elements = {}
        self.discovered_elements = set()
        self.recipes = []

        self._initialize_elements()
        self._initialize_recipes()

    def _initialize_elements(self):
        base_elements = ["вода", "огонь", "воздух", "земля"]

        for name in base_elements:
            element = Element(name)
            self.elements[name] = element
            self.discovered_elements.add(name)

    def _initialize_recipes(self):
        recipes_data = [
            ("вода", "земля", "грязь"),
            ("огонь", "земля", "камень"),
            ("вода", "огонь", "пар"),
            ("земля", "воздух", "пыль"),
            ("вода", "воздух", "облако"),
            ("огонь", "воздух", "энергия"),
            ("облако", "вода", "дождь"),
        ]

        for e1, e2, result in recipes_data:
            self.recipes.append(Recipe(e1, e2, result))

    def combine(self, element1_name, element2_name):
        if element1_name not in self.discovered_elements:
            return f"Элемент {element1_name} ещё не открыт!"
        if element2_name not in self.discovered_elements:
            return f"Элемент {element2_name} ещё не открыт!"

        for recipe in self.recipes:
            if recipe.matches(element1_name, element2_name):
                result_name = recipe.result

                if result_name in self.discovered_elements:
                    return f"Уже есть {result_name}!"
                if result_name not in self.elements:
                    new_element = Element(result_name)
                    self.elements[result_name] = new_element

                self.discovered_elements.add(result_name)

                return f"Успех {element1_name} + {element2_name} = {result_name}!"
        return f"Ничего не вышло"

    def show_elements(self):
        if not self.discovered_elements:
            print(f"У вас ничего нет")
            return

        print("\nВаши элементы:")
        for name in sorted(self.discovered_elements):
            print(f"- {name}")
        print()

    def play(self):
        print("АЛХИМИЯ")
        print("Команды: элементы, выход")

        while True:
            command = input("> ").strip().lower()

            if command == "элементы":
                self.show_elements()

            elif command == "выход":
                print("\nКонец игры")
                break

            elif " " in command:
                parts = command.split()
                if len(parts) == 2:
                    e1, e2 = parts[0], parts[1]
                    result = self.combine(e1, e2)
                    print (result + "\n")
                else:
                    print("Нужно 2 элемента через пробел")

            else:
                print("\nНеизвестная команда")


if __name__ == "__main__":
    game = AlchemyGame()
    game.play()
