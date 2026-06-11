from Logic.guess_number import random_number
from Logic.comparison import comparison
from Logic.score import Score
from utils.user_input import valid_input

def main():
    game_score = Score()
    computer_guess = random_number(1, 100)

    while True:
        org_input = valid_input("\nPlease Enter an int number betweeen 1 and 100: ", 1, 100)
        if computer_guess == org_input:
            print("\nYOU DID IT!! your guess is correct :)")
            print(game_score.show_score())
            break
            
        else:
            hint = comparison(computer_guess, org_input)
            print(hint)
            game_score.reduce_score()

        
if __name__ == '__main__':
    main()
