def pyramid(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()


def reverse_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def multiplication_grid(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()


def main():
    print("=== Number Pattern Generator ===")
    print("1. Star Pyramid")
    print("2. Reverse Star Pyramid")
    print("3. Number Triangle")
    print("4. Multiplication Grid")

    choice = input("Choose a pattern: ").strip()

    try:
        n = int(input("Enter the size: "))

        if n <= 0:
            print("Size must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == "1":
        pyramid(n)

    elif choice == "2":
        reverse_pyramid(n)

    elif choice == "3":
        number_triangle(n)

    elif choice == "4":
        multiplication_grid(n)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
    