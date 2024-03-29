# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
# list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```

# Ask for a number
userNumber = int(input('Enter a number'))

# Print out the numbers in the list that are SMALLER than what the user enters
#     list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]

list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
for eachNumber in list_of_many_numbers:
    # print(eachNumber)
    print(f'you entered {userNumber}:')
    if eachNumber > userNumber:
        print(f'{eachNumber} is LARGER than {userNumber}')
        # Print out the numbers in the list that are LARGER than what the user enters
        #     list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
    if eachNumber < userNumber:
        print(f'{eachNumber} is SMALLER than {userNumber}')


# def compNumbers():
#     list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
#     for eachNumber in list_of_many_numbers:
#         return eachNumber
#     if eachNumber > userNumber:
#         return eachNumber
#         # Print out the numbers in the list that are LARGER than what the user enters
#         #     list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
#     if eachNumber < userNumber:
#         return eachNumber
#
# print(compNumbers())

