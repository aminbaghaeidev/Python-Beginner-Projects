import random
from typing import List

class RockPaperScissors:
    """
    The main class of the game rock-paper-scissors
    """

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choices: List[str] = ['rock', 'paper', 'scissors']

    def get_user_choice(self) -> str:
        """
        Get the input from user and check the input

        :raises ValueError: if user enter something except rock, paper
        or scissors
        :return: will return the user choice
        """

        try:
            user_choice: str = input("Enter your choice(rock, paper, scissors): ")
            if user_choice not in self.choices or user_choice.isdigit():
                raise ValueError
            return user_choice
        except ValueError:
            print("Invailid input! Please enter (scissors, paper or rock ).")
            return self.get_user_choice()

    def get_computer_choice(self) -> str:
        """
        The computer will choose here.

        :return: return the computer choice
        """

        return random.choice(self.choices)

    def logic(self, user_choice: str, computer_choice: str) -> str:
        """
        Will choose the winner based on game rules.

        :param user_choice: The user's choice.
        :param computer_choice: The computer's choice.
        :return: will return hint messages and calculate the winner score.
        """

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or\
             (user_choice == "paper" and computer_choice == "rock") or\
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            return f"""Congrats! You won ;) Your choice {user_choice} & computer choice: {computer_choice}
            User score: [{self.user_score}]"""
        else:
            self.computer_score += 1
            return f"""Oh no! Computer beat you! Your choice: {user_choice} & computer choice: {computer_choice}
            Comuter score: [{self.computer_score}]"""

    def play(self):
        """
        will call and get both user choice and computer choice
        then pass them to logic function.
        """

        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(self.logic(user_choice, computer_choice))
