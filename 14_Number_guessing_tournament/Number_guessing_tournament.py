import random


def main():
    attempts_per_round = []
    round_number = 1

    while True:
        attempts = guesser(round_number)
        attempts_per_round.append(attempts)

        user = input("\nDo you want to play again? (Y/N): ").strip().lower()

        if user == "y":
            round_number += 1

        elif user == "n":
            print("\nHave a nice day!")
            results(attempts_per_round)
            break

        else:
            print("Enter a valid choice. Please enter Y or N.")


def guesser(round_number):
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\n=== Round {round_number} ===")

    while True:
        try:
            user = int(input("Guess the number (1-100): "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if not 1 <= user <= 100:
            print("Number is not valid. Enter a number between 1 and 100.")
            continue

        attempts += 1

        if user > secret_number:
            print("Too high!")

        elif user < secret_number:
            print("Too low!")

        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

    return attempts


def results(attempts_per_round):
    print("\n=== Tournament Results ===")

    rounds_played = len(attempts_per_round)
    print(f"Rounds played: {rounds_played}")

    total_attempts = 0

    for attempts in attempts_per_round:
        total_attempts += attempts

    print(f"Total attempts: {total_attempts}")
    print(f"Average attempts per round: {total_attempts / rounds_played}")

    lowest = attempts_per_round[0]

    for attempts in attempts_per_round:
        if attempts < lowest:
            lowest = attempts

    print(f"Best round: {lowest} attempts")


main()