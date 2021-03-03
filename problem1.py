"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Takes input from the user on how many wins or losses they had. It then sorts them into a group based on those given statistics.
 
Author: Ku.T
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

#Title printing and white space for visual effect
print("")
print("*****  Tournament Tracker  *****")
print("")

#User friendly prompt
print("Enter the wins and losses for your team via w/l:")

#Setting up the win counter variable
win_count = 0

#Counts only for "w" and adds +1 to the win counter. Repeats 6 times
for i in range(6):
  score = input("")
  if score == "w":
    win_count = win_count + 1

#If, elif, else statements to siphon score into a corresponding group
if win_count >= 5:
  print("")
  print("Your team is in Group 1")

elif win_count >= 3 and win_count <= 4:
  print("")
  print("Your team is in Group 2")

elif win_count >= 1 and win_count <= 2:
  print("")
  print("Your team is in Group 3")

else:
  print("")
  print("Your team is eliminated from the tournament")