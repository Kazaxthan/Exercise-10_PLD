#Exercise 10: Create a new list from two list using the following condition
#Create a new list from two list using the following condition
#Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def create_new_list(list1, list2):
    # Extract odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]

    # Extract even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]

    # Combine the odd numbers from the first list and even numbers from the second list
    new_list = odd_numbers + even_numbers

    return new_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Create the new list based on the given condition
result_list = create_new_list(list1, list2)

print(f"The new list is: {result_list}")
