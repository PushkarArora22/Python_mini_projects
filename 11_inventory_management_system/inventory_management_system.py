def add_product(inventory):
    name = input("Enter product name: ").strip()

    while True:
        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity < 0:
                print("Price must be greater than 0 and quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid price and quantity.")

    inventory.append([name, price, quantity])
    print("Product added successfully.\n")


def view_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.\n")
        return

    print("\n--- Inventory ---")

    for i, product in enumerate(inventory, start=1):
        print(
            f"{i}. {product[0]} | "
            f"₹{product[1]:.2f} | "
            f"Stock: {product[2]}"
        )

    print()


def search_product(inventory):
    name = input("Enter product name to search: ").strip().lower()

    for product in inventory:
        if product[0].lower() == name:
            print(
                f"\nProduct found: {product[0]} | "
                f"₹{product[1]:.2f} | "
                f"Stock: {product[2]}\n"
            )
            return

    print("Product not found.\n")


def update_stock(inventory):
    name = input("Enter product name: ").strip().lower()

    for product in inventory:
        if product[0].lower() == name:
            while True:
                try:
                    quantity = int(input("Enter new quantity: "))

                    if quantity < 0:
                        print("Quantity cannot be negative.")
                        continue

                    product[2] = quantity
                    print("Stock updated successfully.\n")
                    return

                except ValueError:
                    print("Please enter a valid quantity.")

    print("Product not found.\n")


def remove_product(inventory):
    name = input("Enter product name to remove: ").strip().lower()

    for product in inventory:
        if product[0].lower() == name:
            inventory.remove(product)
            print("Product removed successfully.\n")
            return

    print("Product not found.\n")


def inventory_value(inventory):
    total = 0

    for product in inventory:
        total += product[1] * product[2]

    print(f"\nTotal Inventory Value: ₹{total:.2f}\n")


def low_stock_products(inventory):
    found = False

    print("\n--- Low Stock Products ---")

    for product in inventory:
        if product[2] <= 5:
            print(f"{product[0]} | Stock: {product[2]}")
            found = True

    if not found:
        print("No low-stock products.")

    print()


def main():
    inventory = []

    while True:
        print("=== Inventory Management System ===")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Remove Product")
        print("6. Inventory Value")
        print("7. Low Stock Products")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            view_inventory(inventory)

        elif choice == "3":
            search_product(inventory)

        elif choice == "4":
            update_stock(inventory)

        elif choice == "5":
            remove_product(inventory)

        elif choice == "6":
            inventory_value(inventory)

        elif choice == "7":
            low_stock_products(inventory)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-8.\n")


if __name__ == "__main__":
    main()
