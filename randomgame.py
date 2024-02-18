import random as r
def Gambling_game():
    a=r.choice(range(1,100))
    print()
    print()
    print("-"*65,"Welcome to Gambling","-"*65)
    print()
    n=int(input("Number of guesses: "))
    print()
    print("*"*150)
    i=1
    def lose():
            print()
            print("You Lost")
            print("The number is ",a)           
    while i<=n:
        print(f"Guess Number {i}:")
        print()
        x=int(input("Guess a number from 1 to 100: "))
        b=a
        if x>a:
            print("The guessed number is greater")
            print()
            print("*"*150)
            if i==n:
                lose()
                i+=n
            else: i+=1
        elif x<a:
            print("The guessed number is less")
            print()
            print("*"*150)
            if i==n:
                lose()
                i+=n
            else: i+=1
        else:
            print("*"*150)
            print()
            print(" "*65,"Hurryyy.........You Won!!!!")
            i+=n
    print()
    print("*"*150)
    print("Thank you")
Gambling_game()





















