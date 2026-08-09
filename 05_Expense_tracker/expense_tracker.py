def main():
    total_expense=int(input("How many expense you want to enter"))
    expenses=[]
    monthly_budget=int(input("Enter your monthly budget"))
    total_amount=0
    for i in range(1,total_expense+1):
        expense_name=input("Enter expense name")
        amount=int(input("Enter amount"))
        expenses.append([expense_name,amount])
        total_amount+=amount
    name,amount=highest_expense(expenses)
    lowest_name,lowest_amount=lowest_expense(expenses)
    print(expenses)
    print(f"Your total amount is {total_amount}")
    print(f"Average amount is {average(total_amount,total_expense)}")
    print(f"Your highest expense is {name} of {amount}")
    print(f"Your lowest expense is {lowest_name} of {lowest_amount}")
    print(f"YOur current budget status is: {m_budget(monthly_budget,total_amount)}")

def average(total_amount,total_expense):
    return total_amount/total_expense

def highest_expense(expenses):
    highest=0
    highest_expense_name=""
    for i in expenses:
        if i[1]>highest:
            highest=i[1]
            highest_expense_name=i[0]
    return highest_expense_name,highest
    

def lowest_expense(expenses):
    lowest=expenses[0][1]
    lowest_expense_name=expenses[0][0]
    for i in expenses:
        if i[1]<lowest:
            lowest=i[1]
            lowest_expense_name=i[0]
    return lowest_expense_name,lowest

def m_budget(monthly_budget,total_amount):
    if monthly_budget>total_amount:
        return "Under budget! You will survive"
    elif monthly_budget==total_amount:
        return "Exactly at budget! You are at the brink of extinction"
    else:
        return "Over budget! You are Dead"



main()

