""""=========================================================================
Author: Mabasa Ntshembo 
github: https://github.com/MabasaNv
Date: 2024-06-01
Description: This is a python script to Calculate the area and perimeter of
Rectangular Tables for Customers
============================================================================="""


print("Welcome to the Rectangular Table Area and Perimeter Calculator!")

def calculate_area(length, width):
      """Calculate the area of a rectangle."""
      area = length * width
      return area
def calculate_perimeter(length, width):
      """Calculate the perimeter of a rectangle."""
      perimeter = 2 * (length + width)
      return perimeter

while True:
      try:
            t_length = float(input("Please enter the length of the table (in meters): "))
            t_width = float(input("Please enter the width of the table (in meters): "))
            if t_length <= 0 or t_width <= 0:
                  print("Length and width must be positive numbers. Please try again.")
                  continue
            area = calculate_area(t_length, t_width)
            perimeter = calculate_perimeter(t_length, t_width)
            print(f"The area of the table is {area} square meters.")
            print(f"The perimeter of the table is {perimeter} meters.")
            break
      except ValueError:
            print("Invalid input. Please enter a valid number.")