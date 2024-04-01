#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:45:27 2024

@author: devin
"""

import math

# Basic shape class
class Shape:
    # parent area method -- should never actually run
    def area():
        print("This is the main shape class.")
        
    # parent perim method -- should never actually run
    def perimeter():
        print("This is the main shape class.")
        
# Circle Class - inherits shape
class Circle(Shape):
    # Constructs objects with attribute radius
    def __init__(self, radius):
        self.radius = radius
        
    # circle area method
    def area(self):
        # Area of a circle
        area = 3.14*(self.radius**2)
        # Display result
        print(f"The area of the circle with radius {self.radius} is {area:.2f}")
        
    # Circle perim method
    def perimeter(self):
        # Perim of a circle
        perimeter = 2*3.14*self.radius
        # display result
        print(f"The perimeter of the circle with radius {self.radius} is {perimeter:.2f}")
        
# Rectangle class (inherits shape)
class Rectangle(Shape):
    # Constructs objects with attributes length and width
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    # Area method for rectangle
    def area(self):
        # Area of a rectangle formula
        area = self.length*self.width
        # Display result
        print(f"The area of the rectangle with length {self.length} and width {self.width} is {area:.2f}")

    # Rectangle perim method
    def perimeter(self):
        # Perim of a rectangle formula
        perimeter = 2*(self.length+self.width)
        # Display result
        print(f"The perimeter of the rectangle with length {self.length} and width {self.width} is {perimeter:.2f}")

# Triangle class (inherits shape)
class Triangle (Shape):
    # Constructs objects with attributes base and height
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    # Area method for triangle
    def area(self):
        # Formula for area of a triangle
        area = 0.5*self.base*self.height
        # Display results
        print(f"The area of the triangle with base {self.base} and height {self.height} is {area:.2f}")

    # Perim of triangle method (Assumes right triangle)
    def perimeter(self):
        # Calculates hypotenuse 
        hyp = math.sqrt((self.base)**2 + (self.height)**2)
        # Calculates perimeter
        perimeter = self.base + self.height + hyp
        # Display results
        print(f"The perimeter of the triangle with base {self.base} and height {self.height} is {perimeter:.2f}")

def main():
    # Creates test objects from each class
    circle = Circle(7)
    rectangle = Rectangle(4,9)
    triangle = Triangle(3,4)
    # List of the objects
    shape_list = [circle,rectangle,triangle]
    # Iterate over the list
    for item in shape_list:
        # Invoke the specific area and perimeter methods for each
        item.area()
        item.perimeter()
        
main()
    
    

        
    
    
