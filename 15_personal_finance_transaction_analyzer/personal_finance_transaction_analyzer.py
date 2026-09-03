def main():

    transactions=[]

    while True:

        print("========== PERSONAL FINANCE ANALYZER ==========\n")

        print("\n")

        print("1. Add transaction\n")

        print("2. View transactions\n")

        print("3. Filter transactions\n")

        print("4. Financial statistics\n")

        print("5. Spending by category\n")

        print("6. Highest spending category\n")

        print("7. Financial summary\n")

        print("8. Exit\n")

        choice=int(input("Enter your choice"))

        if choice==1:

            add_transaction(transactions)

        elif choice==2:

            view_transaction(transactions)

        elif choice==3:

            filter_transaction(transactions)

        elif choice==4:

            financial_statistics(transactions)

        elif choice==5:

            spending_by_category(transactions)

        elif choice==6:

            highest_spending_category(transactions)

        elif choice==7:

            financial_summary(transactions)

        elif choice==8:

            break

        else:

            print("Enter a valid choice")


def add_transaction(transactions):

    description=input("Enter descriptions: ")

    category=input("Enter category: ")

    transaction_type=input("Enter type: ")

    amount=float(input("Enter amount: "))

    transaction={

        "description": description,

        "category": category,

        "type": transaction_type,

        "amount": amount

    }

    transactions.append(transaction)


def view_transaction(transactions):

    if not transactions:

        print("No transactions found")

        return

    for i in transactions:

        for key, value in i.items():

            print(f"{value} | ",end="")

        print()


def filter_transaction(transactions):

    if not transactions:

        print("No transactions available")

        return

    print("1.Filter by category\n","2.Filter by type")

    choice=int(input("Enter which filter you want to use(1 or 2)"))

    if choice==1:

        filter=input("Enter category: ")

        found=False

        for i in transactions:

            if i["category"]==filter:

                print(i)

                found=True

        if not found:

            print("No matching transactions found")

    elif choice==2:

        type=input("Enter type: ")

        found=False

        for i in transactions:

            if i["type"]==type:

                print(i)

                found=True

        if not found:

            print("No matching transactions found")

    else:

        print("invalid filter")


def financial_statistics(transactions):

    if not transactions:

        print("No transactions available")

        return

    Total_income=0

    Total_expense=0

    largest=0

    expense_found=False

    for i in transactions:

        if i["type"]=="income":

            Total_income+=i["amount"]

        elif i["type"]=="expense":

            Total_expense+=i["amount"]

            expense_found=True

            if i["amount"]>largest:

                largest=i["amount"]

    current_balance=Total_income-Total_expense

    print(f"Total income: {Total_income}")

    print(f"Total expenses: {Total_expense}")

    print(f"Current balance: {current_balance}")

    if expense_found:

        print(f"Largest expense: {largest}")

    else:

        print("Largest expense: No expenses")


def spending_by_category(transactions):

    if not transactions:

        print("No transactions found")

        return

    category=input("Enter category: ")

    total_amount=0

    for i in transactions:

        if category==i["category"]:

            if i["type"]=="expense":

                total_amount+=i["amount"]

    print(f"Total amount spent: {total_amount}")


def highest_spending_category(transactions):

    if not transactions:

        print("No transaction found")

        return

    spending={}

    for i in transactions:

        if i["type"]=="expense":

            category=i["category"]

            if category in spending:

                spending[category]+=i["amount"]

            else:

                spending[category]=i["amount"]

    if not spending:

        print("No expense found")

        return

    highest=0

    for key, value in spending.items():

        if value>highest:

            highest=value

            highest_category=key

    print(f"Highest category: {highest_category}")

    print(f"Highest expense: {highest}")


def financial_summary(transactions):

    financial_statistics(transactions)

    highest_spending_category(transactions)


main()