def main():
    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

    print(f"Ответ: {[num for matrix in nice_list for row in matrix for num in row]}")

if __name__ == "__main__":
    main()
