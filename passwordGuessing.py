#Word Guessing Game , easy , mid , hard 

import random

easy_words = [
    "cat", "dog", "sun", "book", "tree",
    "ball", "fish", "milk", "star", "rain"
]

medium_words = [
    "adventure", "curious", "imagine", "journey", "discover",
    "protect", "whisper", "mountain", "puzzle", "create"
]

hard_words = [
    "ambiguous", "meticulous", "paradox", "intricate", "ephemeral",
    "resilient", "ubiquitous", "conundrum", "serendipity", "tenacious"
]

print("Welcome to the GAME")
print("Choose a difficulty level")

level= input("Enter difficulty: ").lower()
if level=="easy":
    secret= random.choice(easy_words)
elif level=="medium":
    secret= random.choice(medium_words)
elif level=="hard":
    secret= random.choice(hard_words)
else:
    print("Invalid Choice")
    secret= random.choice(easy_words)
    
    
attempts=0
print("\n Guess the Secret key")

while True:
    guess= input("Enter your guess: ").lower()
    attempts= attempts+1
    
    if guess==secret:
        print(f"Congratulation: attempts {attempts}")
        break
    
    
    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]== secret[i]:
            hint+= guess[i]
        else:
            hint+="_"
    print("Hint:- "+ hint)
    
print("Game Over")