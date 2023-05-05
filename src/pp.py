import random

def main(): #function

    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess > number:
            print("Too high")
            continue

        if guess < number:
            print("Too low")
            continue

        else:
            print("Correctly guessed")
            break


if __name__ == "__main__":
    main()

