def main():
    line = input("Введите строку: ")

    first = line.find('h')
    last = line.rfind('h')

    seq = line[first + 1:last][::-1]

    print(f"Развёрнутая последовательность между первым и последним h: {seq}")

if __name__ == "__main__":
    main()
