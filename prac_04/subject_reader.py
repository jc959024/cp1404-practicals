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
            # print(line)  # See what a line looks like
            # print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            # print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            teachers_information.append(parts)
            # print(parts)  # See if that worked
            # print("----------")
    return teachers_information


def display_new_data(data):
    """Display the details of each subject."""
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")


main()
