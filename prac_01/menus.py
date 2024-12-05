# Constants
MENU = """
(H)ello
(G)oodbye
(Q)uit
"""

# User's name
name = input("Enter name: ")
choice = None

# Continue looping until the user chooses to quit
while choice != 'Q':
    print(MENU)
    choice = input(">>> ").strip().upper()

# According to the user input different letters for different operations
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    elif choice != 'Q':
        print("Invalid choice")

print("Finished.")


