def valid_input(prompt, start_number, end_number):
    """Check the user's input"""
    while True:
        try:
            user_input = int(input(prompt))
            if start_number <= user_input <= end_number:
                return user_input
            else:
                print(f"Please enter a numbeer betweeen {start_number} and {end_number}.")
        except ValueError:
            print("Invalid input! please enter an int number")