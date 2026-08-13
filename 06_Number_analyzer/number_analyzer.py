def main():
    n=int(input("Enter a number"))

    if n == 0:
        print("Number of digits: 1")
        print("Sum of digits: 0")
        print("Largest digit: 0")
        print("Smallest digit: 0")
        print("Even digits: 1")
        print("Odd digits: 0")
        print("Reversed number: 0")
        return
    
    print(f"Number of digits: {n_digits(n)}")
    print(f"Sum of digits: {sum_digits(n)}")
    print(f"Largest digit: {largest_digit(n)}")
    print(f"Smallest digit: {smallest_digit(n)}")
    print(f"Even digits: {even_digit(n)}")
    print(f"Odd digits: {odd_digit(n)}")
    print(f"Reversed number: {reverse_digit(n)}")

def n_digits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

def sum_digits(n):
    s_digits=0
    while n>0:
        a=n%10
        s_digits+=a
        n=n//10
    return s_digits

def largest_digit(n):
    largest=0
    while n>0:
        a=n%10
        if a>largest:
            largest=a
        n=n//10
    return largest

def smallest_digit(n):
    smallest=9
    while n>0:
        a=n%10
        if a<smallest:
            smallest=a
        n=n//10
    return smallest

def even_digit(n):
    a=0
    while n>0:
        b=n%10
        if b%2==0:
            a+=1
        n=n//10
    return a

def odd_digit(n):
    a=0
    while n>0:
        b=n%10
        if b%2!=0:
            a+=1
        n=n//10
    return a

def reverse_digit(n):
    reverse=0
    while n>0:    
        a=n%10
        reverse=reverse*10+a
        n=n//10
    return reverse
    
    

main()