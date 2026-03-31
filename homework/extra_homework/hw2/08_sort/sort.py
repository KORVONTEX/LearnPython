def main():
    nums = list(map(int, input("Введите числа через пробел: ").split()))

    print(f"Изначальный список: {nums}")

    for i in range(len(nums) - 1):
        isSwapped = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                isSwapped = True
        if not isSwapped:
            break

    print(f"Отсортированный список: {nums}")

if __name__ == "__main__":
    main()
