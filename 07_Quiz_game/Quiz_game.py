def main():
    questions=["Which planet hass the most moons in our Solar System?","What does CPU stand for?","Which number is a prime number?","What is the largest ocean on Earth","In Python,which symbol is used for exponentiation?"]
    answers=["B","A","C","D","C"]
    c=0
    d=0
    score=0
    print("===============")
    print("   Quiz Game   ")
    print("===============")
    for i in questions:
        d+=1
        print(f"\nQuestion {d}/5")
        print(i)
        if i==questions[0]:
            print("A.Jupiter",
                  "\nB.Saturn",
                  "\nC.Uranus",
                  "\nD.Neptune")
        elif i==questions[1]:
            print("A.Central Processing Unit" ,
                  "\nB.Computer Personal Unit" ,
                  "\nC.Central Program Utility" ,
                  "\nD.Computer Processing Utility")
        elif i==questions[2]:
            print("A.21",
                  "\nB.27",
                  "\nC.29",
                  "\nD.33")
        elif i==questions[3]:
            print("A.Atlantic Ocean",
                  "\nB.Indian Ocean",
                  "\nC.Arctic Ocean",
                  "\nD.Pacific Ocean")
        elif i==questions[4]:
            print("A.^",
                  "\nB.//",
                  "\nC.**",
                  "\nD.%")
        user=input("Enter your answer").upper()
        if user==answers[c]:
            score+=1
        c+=1
    print(f"Score: {score}/5")

    
main()