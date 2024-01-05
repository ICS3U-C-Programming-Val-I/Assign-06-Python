#!/usr/bin/env python3

# Created By: Val Ijaola
# Date:Jan 3, 2024
# This programme asks the user to enter 10 numbers ,
# It then asks them for a number that was input,
# And it finds what index the number is at.

# Initializing variables and constants
num_to_find = 0
MAX_LIST_SIZE = 10


def find_index(list_of_floats, find_num):
    # Finds and returns the index of a specific number
    index = -1
    for counter in range(len(list_of_floats)):
        if list_of_floats[counter] == find_num:
            index = counter
            break
    return index

def main():
    # Initial greeting/message
    print("Hello and Welcome!")
    print("Enter 10 numbers and I’ll tell you what index you placed a specific number")

    # Initializing list
    list_of_numbers = []

    # Getting numbers from the user
    for counter in range(MAX_LIST_SIZE):
        num_added_str = input("Enter a number: ")

        # Catching errors
        try:
            num_added = float(num_added_str)
            list_of_numbers.append(num_added)
            print(f"{num_added} was added")
        except ValueError:
            print(f"{num_added_str} is not a number.")
            return 0

    # Getting num_to_find from user
    num_to_find_str = input("Enter a number to find its index: ")
    try:
        num_to_find = float(num_to_find_str)
        index_found = find_index(list_of_numbers, num_to_find)
        # Displaying result
        if index_found == -1:
            print(f"{num_to_find} is not in the list.")
        else:
            print(f"Index of {num_to_find}: {index_found}")
    except ValueError:
        print(f"{num_to_find_str} is not a number.")

if __name__ == "__main__":
    main()