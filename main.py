import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses += 1
    a=int(input("Guess the number:"))

    if (a>n):
        print("Enter the lower number")
    else:
        print("Enter the higher number")
    
print(f"You have guessed the number {n} in {guesses} attempts ")