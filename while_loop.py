
'''
i = 1
while i <= 10:
    print(i)
    i += 1

print("done")


'''

secret_word = "Boss Eshan"
guess = ""
guess_count = 0
guess_limits = 3
out_of_guesses = False

while guess !=secret_word and not(out_of_guesses):
    if guess_count < guess_limits:
        guess = input("Enter your guess: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You lose")
else:
    print("you win")
