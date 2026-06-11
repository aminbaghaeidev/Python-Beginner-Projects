import random
from typing import Tuple

def monty_hall_problem(switch_doors: bool, range_of_game: int) -> int:
    """Main function for logic and calculating the winning times.

    :param switch_doors: Switching door or not
    :param range_of_game: the number for repeating this game
    :return: The number of times we won
    :rtype: int
    """
    won = 0
    for _ in range(range_of_game):
        doors = ['1', '2', '3']
        random.shuffle(doors)
        main_choice = random.choice(doors)
        prize = random.choice(doors)
        monty_open = [goat for goat in doors if (goat != prize) and (goat != main_choice)]
        monty_open = random.choice(monty_open)
        if switch_doors:
            new_choice = [i for i in doors if (i != monty_open) and (i != main_choice)][0]
        else:
            new_choice = main_choice

        if new_choice == prize:
            won += 1
    return won


def main(number: int) -> Tuple[float, float]:
    """Gives us probibality of switching or without switching

    :param number: number of times for running
    :return: a tuple of percentage
    """
    if number == 0:
        raise ValueError
    num_win_switch = monty_hall_problem(switch_doors=True, range_of_game=number)
    num_win_stay = monty_hall_problem(switch_doors=False, range_of_game=number)
    num_win_switch = num_win_switch / number
    num_win_stay = num_win_stay / number
    return num_win_stay, num_win_switch


if __name__ == '__main__':
    NUM = 1000
    num_of_win_stay, num_of_win_switch = main(NUM)
    print(f"Winnig without switching percentage per {NUM} times: {num_of_win_stay:.2%}")
    print(f"Winnig with switching percentage per {NUM} times: {num_of_win_switch:.2%}")
