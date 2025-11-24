def get_valid_number(prompt, data_type=int):
    """
    Repeatedly prompts user until a valid number is entered.
    Handles Non-Functional Requirement: Error Handling/Usability.
    """
    while True:
        try:
            value = data_type(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")