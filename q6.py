# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

#Club member class, with name and role
class Clubmember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    #loop through the club member list and show name and role
    def __str__(self):
        return f'Club {self.role}: {self. name}'

# show the instances of the club members
mem1 = Clubmember('Alfred', 'President')
mem2 = Clubmember('Troy', 'Vice President')
mem3 = Clubmember('Albert', 'Secretary')
mem4 = Clubmember('Bob', 'Treasurer')
mem5 = Clubmember('Lorenzo', 'Sargent at Arms')

# loop through each instance of club member and print
members = [mem1, mem2, mem3, mem4, mem5]
for eachMember in members:
    print(eachMember)