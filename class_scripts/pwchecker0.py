"""
Password Checker
Created on Thu Sep 26 15:59:28 2019

@author: Student
"""

has_cap = False
has_num = False 
is_8 = False
is_valid = False

pw = input("please enter the password:\t")

for char in pw:
    if char.isupper():
        has_cap = True
    if char.isnumeric():
        has_num = True
        
if len(pw) >= 8:
    is_8 = True
    
#if has_cap == True and has_num == True and is_8==True:
if has_cap and has_num and is_8:    
    is_valid = True

if is_valid == True:
    print("this is a valid password")
else:
    print("this is not a valid password")
