#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:17:58 2024

@author: devin
"""

# Parent employee class
class Employee:
    # Every employee object is constructed with a name and position
    def __init__(self,name,position):
        self.name = name
        self.position = position
        
    # Runs the salary method of the specific object
    def runSalaryMethod(self):
        # Runs the salary method for the current object
        self.calculateSalary()
        
# Child hourly employee class
class HourlyEmployee(Employee):
    # Overrides the employee constructor
    def __init__(self,name,position,hourly_wage,hours_worked):
        # This ensures that name and position are stored at the employee level
        # This makes sense since every employee has a name and position 
        super().__init__(name,position)
        # Additional attributes defined
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        
    # Calculate salary method for hourly employee
    def calculateSalary(self):
        # Hours * hourly wage
        salary = self.hourly_wage*self.hours_worked
        # Print salary
        print(f"{self.name}, {self.position}, has a salary of ${salary}")
        
    
# Child salary employee class
class SalaryEmployee(Employee):
    # Overrides the employee constructor
    def __init__(self,name,position,salary):
        # This ensures that name and position are stored at the employee level
        super().__init__(name,position)
        # Defines additional attribute
        self.salary = salary
        
    # Calculate salary mehthod for salary employees
    def calculateSalary(self):
        # Print salary attribute -- no calculation necessary
        print(f"{self.name}, {self.position}, has a salary of ${self.salary}")
        
# Child commission employee class
class CommissionEmployee(Employee):
    # Overrides the employee constructor
    def __init__(self,name,position,price_per_commission,commissions_completed):
        # This ensures that name and position are stored at the employee level
        super().__init__(name,position)
        # Defines additional attributes
        self.price_per_commission = price_per_commission
        self.commissions_completed = commissions_completed
        
    # Calculate salary mehthod for commission employees
    def calculateSalary(self):
        # salary = amount of commissions * price charged per each commission
        salary = self.price_per_commission*self.commissions_completed
        print(f"{self.name}, {self.position}, has a salary of ${salary}")
    
def main():
    # Defines test objects for each type of employee 
    hour = HourlyEmployee('Jesse','Fast Food Worker',15,1500)
    sal = SalaryEmployee('Mary','Electrical Engineer',134000)
    comm = CommissionEmployee('Bob','Car Salesman',550,120)
    # Puts these objects in a list
    employees= [hour,sal,comm]
    # Iteration over the list
    for employee in employees:
        # Run the run salary method, which then runs the calculate salary method
        # Could also do employee.calaculateSalary()
        employee.runSalaryMethod()

    
main()