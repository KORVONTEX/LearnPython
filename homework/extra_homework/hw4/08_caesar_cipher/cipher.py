def caesar_cipher(text, shift):
    result = []
    shift = shift % 32  # без ё

    for char in text:
        if 'а' <= char <= 'я':
            new_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            result.append(new_char)
        elif 'А' <= char <= 'Я':
            new_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def main():
    mes = input("Введите сообщение: ")
    k = int(input("Введите свдиг: "))

    final = caesar_cipher(mes, k)

    print(f"Зашифрованное сообщение: {final}")


if __name__ == "__main__":
    main()
