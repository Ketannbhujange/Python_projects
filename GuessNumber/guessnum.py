import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}"))
        # print(guess)
        if guess<random_number:
            print("Sorry, guess again. Too low.")
        elif guess>random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay Congrats!! you have guessed the number correctly {random_number}")
    
# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feed_back = ""
    guess = 0
    while feed_back != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feed_back = input(f'Is {guess} too high(H), too low(L), or correct(C)???').lower()
        # print(feed_back)
        if feed_back == 'h':
            high  = guess-1
        elif feed_back == 'l':
            low = guess+1
            
    print(f"Yay the number {guess} is guessed correctly by computer")        
            
computer_guess(10)