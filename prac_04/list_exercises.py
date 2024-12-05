def main():
    # Part 1: Handling Numbers
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    # Collect 5 numbers from the user
    for i in range(5):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print("\nYou entered these numbers:")
    for num in numbers:
        print(f"Number: {num}")

    # Print the first and last number
    print(f"\nThe first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")

    # Print the smallest, largest, and average of the numbers
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")

    # Part 2: Username Security Checker
    username = input("\nEnter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
