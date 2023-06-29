from random import randint


def bones_game():
    n = int(input("загадайте число от 2 до 12: "))
    count = randint(1, 6)
    count2 = randint(1, 6)
    count3 = 1
    print("выпало:", count, "и", count2)
    while count + count2 != n:
        count = randint(1, 6)
        count2 = randint(1, 6)
        count3 += 1
        print("выпало:", count, "и", count2)
    print("прошло аж", count3, "попыток(и)!")


def main():
    bones_game()


if __name__ == "__main__":
    main()
