def happy_number(number: int) -> bool:
    """check the number that is happy or unhappy

    :param number: inputed number
    :return: check the last number is equal to 1 or not
    """
    seen_numbers = set()
    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(i) ** 2 for i in str(number))
    return number == 1

while True:
    user_input = int(input("Enter your number: "))
    result = happy_number(user_input)
    print(f"{user_input} is {'a happy' if result else 'not a happy'} number!")

    answer = input("Do you want to continue? (y or n): ")
    if answer.lower() == 'n':
        print("See you later. Bye!")
        break
