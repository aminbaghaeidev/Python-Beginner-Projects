from game import RockPaperScissors
from check_answer import check_answer

if __name__ == '__main__':
    game1 = RockPaperScissors()
    game_round = 0
    while True:
        game1.play()
        game_round += 1
        if game_round % 5 == 0:
            result = check_answer()
            if result:
                break
            continue
