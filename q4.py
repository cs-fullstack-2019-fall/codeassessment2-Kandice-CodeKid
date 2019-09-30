# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```


def wordComp(user1, user2):
    if user1 > user2:
        return True
    if user1 < user2:
        return False




# ask for two words from user
userInput1 = input("enter a word ").lower()
userInput2 = input('enter another word ').lower()

print(wordComp(userInput1, userInput2))
