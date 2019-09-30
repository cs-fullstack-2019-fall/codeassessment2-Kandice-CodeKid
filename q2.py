# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

#ask user a question
question1 = input('Is it better to be rude of kind to people?').lower()
#prompt the user to keep answering the question is the anwer isn't kind, return try again if not.
while question1 != 'kind':
    print('That’s not the answer I had hoped to hear. Try again.')
    question1 = input('Is it better to be rude of kind to people?').lower()
    #once kind is entered print ’Now that’s what I wanted to hear!’ and exit.
else:
    print('Now that’s what I wanted to hear!')