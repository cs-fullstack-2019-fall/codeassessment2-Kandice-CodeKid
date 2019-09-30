# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
# list_of_claim_nums_1 = [2, 4, 6, 8, 10]
# list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```


# merge the two list to make one list.
## access the index of claim 1
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
for eachClaim1 in list_of_claim_nums_1:
    print(eachClaim1)

## access the index of claim 1
list_of_claim_nums_2 = [1, 3, 5, 7, 9]
for eachClaim2 in list_of_claim_nums_2:
    print(eachClaim2)
# after merge print the numbers
print(eachClaim1 + eachClaim2)