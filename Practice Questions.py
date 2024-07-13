# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:56:59 2024

@author: Hp
"""

#to convert radian into degrees 
rad=float(input("Enter the Radian value"))

degree=(rad*180/3.142)

print(degree)

# to convert degree into radian
degree=float(input("Enter the degree value"))

radian=(degree*3.142/180)

print(radian)
#------------------------------------------------------------------
"""
 Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""
    
print("""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you ar""")

#--------------------------------------------------------------------
#to display the version of the python
import sys  # Import the sys module to access system-specific parameters and functions

# Print the Python version to the console
print("Python version")

# Use the sys.version attribute to get the Python version and print it
print(sys.version)

# Print information about the Python version
print("Version info.")

# Use the sys.version_info attribute to get detailed version information and print it
print(sys.version_info)

#--------------------------------------------------------------------
#to display the current datetime
# Import the 'datetime' module to work with date and time
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a datetime object representing the current date and time

# Display a message indicating what is being printed
print("Current date and time : ")

# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Use the 'strftime' method to format the datetime object as a string with the desired format

#---------------------------------------------------------------
"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504"""


r=float(input("Enter the Radius of the Circle"))

area=3.142*r*r

print(f"Area is {area}")
#===========================================================
"""Write a Python program that accepts the user's
 first and last name and prints them in reverse order with a space between them.
"""

fn=input("Enter your First Name")
ln=input("Enter your Last Name")

fnr=fn[::-1]
lnr=ln[::-1]

reverse_order=lnr +" " +fnr

print(reverse_order)
#---------------------------------------------------------------
"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Sample data: 3, 5, 7, 23

Python list:"""

# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Input some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
list = values.split(",")

# Convert the 'list' into a tuple and store it in the 'tuple' variable
tuple = tuple(list)

# Print the list
print('List : ', list)

# Print the tuple
print('Tuple : ', tuple)