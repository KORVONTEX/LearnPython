def main():
    names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    a = [names[i] for i in range(len(names)) if i % 2 == 0]
    print(f"Первый день: {a}")

if __name__ == "__main__":
    main()
