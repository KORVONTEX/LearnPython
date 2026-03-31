def main():
    nums = list(map(int, input("Введите числа через пробел: ").split()))

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] % 2 == 0:
            print(nums[i], end=" ")

if __name__ == "__main__":
    main()
