import random 
n = random.randint(1,100)
guessNum = -1
guesses = 1
while guessNum != n:
    guessNum = int(input("Guess the number: "))
    if guessNum > n:
        print("Lower number please")
        guesses += 1
    elif guessNum < n:
        print("Higher number please")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempt!")