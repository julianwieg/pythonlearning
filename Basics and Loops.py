#Python Basics
#Types and Comparisons
#Conditional Statements
#Loops

#fstring format strings can print different types as strings
how_many_new_mess = 2
print(f"{how_many_new_mess} new messages")

#If else and elseif
if True:
  print("if else true is statement")

age = 75
if age >=55:
  print ("Discount applied")


points = 7600
points_needed = 8000

if points >= points_needed:
 print("You're Level 2!")
else:
 left = points_needed - points
 print("Points till Level 2:")
 print(left)


#complex decisions   AND operator skips if one or more decions are False   OR operator if all conditions are FALSE
average_grade = "B"
final_score = 1400
won_competition = True

if average_grade == "A" or final_score >= 1500 or won_competition:
 print( "OR Certificate achieved!")

#self-assign variables can be in or decreased easily
number = 1
number += 1
print(number)

#while loops   loops and stuff   counter variable
counter = 1
while counter < 4:
  print("keep going")
  counter += 1

#for loops
for i in range(6):
  print(i)



