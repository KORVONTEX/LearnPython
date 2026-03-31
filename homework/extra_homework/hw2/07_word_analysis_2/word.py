def isPalindrome(word):
    return word == word[::-1]

def main():
    word = input("Введите слово: ").lower()

    if isPalindrome(word):
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

if __name__ == "__main__":
    main()
