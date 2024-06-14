"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_new_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    teachers_information = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer
            teachers_information.append(parts)
    return teachers_information


def display_new_data(data):
    """Display the details of each subject."""
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")


main()
