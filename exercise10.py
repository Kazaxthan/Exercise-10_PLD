#Exercise 10: Create a new list from two list using the following condition
#Create a new list from two list using the following condition
#Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def create_new_list(list1, list2):
    #  odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]

    #  even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]

    # Combine the odd numbers from the first list and even numbers from the second list
    new_list = odd_numbers + even_numbers

    return new_list

# Get user input 
user_input1 = input("Enter the first list of numbers separated by spaces: ")
user_input2 = input("Enter the second list of numbers separated by spaces: ")

# Convert user input into lists of integers
try:
    list1 = [int(i) for i in user_input1.split()]
    list2 = [int(i) for i in user_input2.split()]
except ValueError:
    print("Invalid input. Please enter valid lists of numbers.")
    exit()

# Create the new list based on the given condition
result_list = create_new_list(list1, list2)
# result
print(f"The new list is: {result_list}")