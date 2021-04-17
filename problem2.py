"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  The program is a travel log that allows the user to input the distance driven in a day until they pass 100km. When it does, the program displays days taken to surpass 100km and the average distance driven per day.
 
Author: Ku.T
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""

#Print for looks
print("**** Welcome to the DoorDash Distance Tracker ****")
print("")
print("*** Travel Log ***")

#Base variables
distance_traveled = 0
days_taken = 0

#Initial distance logging
travel = int(input("Enter the distance travelled for the day: "))
distance_traveled = distance_traveled + travel 
days_taken = days_taken + 1

#While loop for the distance logging
while distance_traveled < 100:
  travel = int(input("Enter the distance travelled for the day: "))
  distance_traveled = distance_traveled + travel
  days_taken = days_taken + 1

#Titles and whitespace for looks
print("")
print("** Tracker Summary **")

#Days taken statement
print("It took", days_taken, "days to surpass 100km driven.")

#Average distance calculations
average_distance = distance_traveled / days_taken
print("The average distance driven per day is", average_distance, "km.")