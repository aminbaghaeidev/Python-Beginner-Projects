import random


class TicTacToe:
    """Main class of tic tac toe game with all the functionality
    """
    def __init__(self):
        self.board = [' '] * 9
        self.player = self.first_player_choice()
        self.choices = set()
        self.winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                       [1, 4, 7], [2, 5, 8], [3, 6, 9],
                       [1, 5, 9], [3, 5, 7]]

    def first_player_choice(self) -> str:
        """choose a player randomly

        :return: x or o player
        """
        return 'X' if random.randint(0, 1) == 0 else 'O'

    def show_board(self):
        """shows the game board
        """
        print("\n")
        print(self.board[:3])
        print(self.board[3:6])
        print(self.board[6:])
        print("\n")

    def user_input(self) -> int:
        """check and gives the user input

        :return: correct form of user input
        """
        while True:
            try:
                choice = int(input(f"player {self.player} enter your choice (1-9): "))
                if 1 <= choice <= 9:
                    if choice in self.choices:
                        print("This home has already been filled! Try again.")
                    else:
                        self.choices.add(choice)
                        return choice

            except ValueError:
                print("Invalid input! Try again.")

    def fill_board(self):
        """fills the board with the user inputed number
        """
        choice = self.user_input()
        self.board[choice-1] = self.player

    def swap_turn(self):
        """swap turn from one player to another
        """
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def board_filled(self) -> bool:
        """checks if the board filled or not
        """
        return ' ' not in self.board

    def set_winner(self) -> bool:
        """check which player won the game
        """
        o_list = [num for num, c in enumerate(self.board, start=1) if c == 'O']
        x_list = [num for num, c in enumerate(self.board, start=1) if c == 'X']

        for combo in self.winner:
            if all(pos in o_list for pos in combo):
                print("Player O won!")
                return True
            if all(pos in x_list for pos in combo):
                print("Player X won!")
                return True
        return False

    def start(self):
        """Logic of the game by using the last functions
        """
        while True:
            self.show_board()
            self.fill_board()
            if self.set_winner():
                self.show_board()
                break
            if self.board_filled():
                self.show_board()
                print("Draw.")
                break
            self.swap_turn()

if __name__ == '__main__':
    x = TicTacToe()
    x.start()
