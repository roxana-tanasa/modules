from random import randint
import sys

# generate a number 1~10

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user

# check that input is a number 1~10

while True:
    try:
        guess = int(input(f'Guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius")
                break
        else:
            print(f"Hey bozo, I said {sys.argv[1]}~{sys.argv[2]}")
    except ValueError:
        print("Please enter a number!")
        continue

# check if number is the right guess
# otherwise, ask again

