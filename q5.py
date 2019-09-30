# ### Problem 5
# Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p, team_city, and team_ranking_p.
# The class should have a method to change a Team’s ranking. 
# The class should implement the ```__str__``` method so that when an instance of the SportsTeam is printed it will output a string containing the team name, team city, and team rank (use f strings to format the output).
# Your program should create a SportsTeam instance with an initial ranking of 2.
# Print out the class.
# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).


# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```

# create a team class
class SportsTeam:
    # properties:team_name_p, team_city, and team_ranking_p
    def __init__(self, name_p, team_city, team_ranking_p):
        self.name_p = name_p
        self.team_city = team_city
        self.team_ranking_p = team_ranking_p
    #use the string method to show team name, team city, and team rank using a f' string
    def __str__(self):
        return f'The {self.name_p} are from {self.team_city} and is {self.team_ranking_p} in the rankings.'


# change team ranking
team1 = SportsTeam('Tigers', 'Whitehave', 3)
# print class
print(team1)
newRanking = SportsTeam("Tigers",'Whitehaven', 1)
print(newRanking)
