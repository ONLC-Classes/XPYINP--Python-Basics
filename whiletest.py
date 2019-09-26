"""
Created on Thu Sep 26 12:18:36 2019

@author: Student
"""

students = 11
while students >  0:

    print("student #", students)
    students = students - 1 
    # same as students -= 1      


again = 'y'
#another option to the below line:
#while again == 'y' or again == 'Y'
while again.lower() == 'y':
    print("here is a statement")
    print()
    again = input("do you want to continue? y/n: ")
    print()
    
    
 


while True:
    print("here is a statement")
    again = input("do you want to continue? y/n: ")
    if again.lower() != 'y':
        break
    

while True:
    print("welcome!")
    print("press 1 to do something, 2 for something else, 3 to exit:")
    
    choice = input("what is your selection? ")
    
    if choice == "3":
        break

print("bye!")


while True:
    score = float(input("Please enter a score or 999 to exit:\t"))
    
    if score == 999:
        break
    else:
        print("letter grade: everyone gets an A")
        
    



again = 'y'

while again.lower() == 'y':
    score = float(input("Please enter a score \t"))
    print("letter grade: everyone gets an A")    
    
    again = input("do you want to continue? y/n: ")
    print()

