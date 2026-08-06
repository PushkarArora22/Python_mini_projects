def main():
    name=input("Enter your name")
    m=int(input("Enter marks in Math: "))
    s=int(input("Enter marks in Science: "))
    e=int(input("Enter marks in English: "))
    if m < 0 or m > 100 or s < 0 or s > 100 or e < 0 or e > 100:
        print("Invalid marks. Please enter a value between 0 and 100.")
        return
    total_marks=(total(m,s,e))
    avg=average(m,s,e)
    print("\n")
    print(f"Student: {name}")
    print(f"Math: {m}")
    print(f"Science: {s}")
    print(f"English: {e}")
    print("                     ")
    print(f"Total: {total_marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {calculate_grade(avg)}")
    print(f"Status: {check_status(avg)}")

def total(a,b,c):
    return a+b+c

def average(a,b,c):
    return (a+b+c)/3


def calculate_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "F"

def check_status(avg):
    if avg>=60:
        return "Pass"
    else:
        return "Fail"

main()