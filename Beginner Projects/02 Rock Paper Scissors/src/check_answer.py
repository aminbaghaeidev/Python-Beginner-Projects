from typing import List

def check_answer() -> bool:
    """Will check the answer that user enters for continue game or not
    :return: True or False
    """

    answer_list: List[str] = ['y', 'Y', 'n', 'N']
    while True:
        ans: str = input("Do you want to play again? (y for yes/ n for no): ")
        if (ans in answer_list) and (ans in ['n', 'N']):
            return True
        elif (ans in ['y', 'Y']):
            return False
        else:
            print("Enter a valid input.")
