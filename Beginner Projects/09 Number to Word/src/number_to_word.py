from CONSTANTS import UNDER_20, TENS, MORE_THAN_100


def number_to_word(num: int):
    """
    Convert number to word form
    :Note: This function only works with number less than 10^15 and greater than 0
    :Input: you can input scientific number for more convenience.
    >>> input = 1e12
    >>> input = 1e6

    :param num: number that user inputed
    :return: word of the user's number
    :rtype: str

    >>> number_to_word(2345)
    'Two Thousand Three Hundered Fourty Five'
    >>> number_to_word(0)
    'Zero'
    >>> number_to_word(1000000)
    'One Million'
    """
    if num < 20:
        return f"{UNDER_20[num]}"

    if 20 <= num < 100:
        ten_part = num // 10
        units = num - (ten_part * 10)
        return f"{TENS[ten_part-2]}{" " + (UNDER_20[units]) if units != 0 else ""}"

    pivot = max([key for key in MORE_THAN_100 if key <= num])
    g = number_to_word(num // pivot)
    remainder = num % pivot
    p1 = number_to_word(remainder) if remainder != 0 else ""
    return f'{g} {MORE_THAN_100[pivot]} {p1}'


if __name__ == '__main__':
    while True:
        try:
            user_input = input("Enter your number (use e for large numbers): ").strip()
            if 'e' in user_input.lower():
                user_input = int(float(user_input))
            user_input = int(user_input)
            if 0 <= user_input < int(1e15):
                print(number_to_word(user_input))
                break
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Please enter a number.")
