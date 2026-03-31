def main():
    nums = list(map(int, input("Введите числа через пробел: ").split()))
    k = int(input("Сдвиг: "))
    n = len(nums)

    if  n == 0:
        print("Сдвинутый список: []")
        return

    k = k % n

    if k == 0:
        print(f"Сдвинутый список: {nums}")
        return
    else:
        shifted = nums[-k:] + nums[:-k]
    print(f"Сдвинутый список: {shifted}")

if __name__ == "__main__":
    main()
