#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 03:48:48 2024

@author: devin
"""

# Main animal class
class Animal:
    # These two functions just run the objects specific eat and sleep methods
    # They pass in an animal object
    # Not necessarily necessary, but the instructions asked
    def letsEat(animal):
        animal.eat()
        
    def letsSleep(animal):
        animal.sleep()
        
# Mammal class - inherits animal
class Mammal(Animal):
    def eat(self):
        print("This is a mammal! It likely eats both meat and plants")
    
    def sleep(self):
        print("This is a mammal! It likely sleeps at night")
        
# Bird class - inherits animal 
class Bird(Animal):
    def eat(self):
        print("This is a bird! Today it finds some wonderful seed to eat")
        
    def sleep(self):
        print("This is a bird! It finds a nice tree to sleep in")
        
# Fish class - inherits animal
class Fish(Animal):
    def eat(self):
        print("This is a fish! It's probably finding another fish to eat")
        
    def sleep(self):
        print("This is a fish! It does not sleep like other animals")
        
# Dog class - inherits mammal (multilevel)
class Dog(Mammal):
    def eat(self):
        print("This is a dog! It gets a nice bowl of meat to eat")
        
    def sleep(self):
        print("This is a dog! It finds its favorite spot on the bed to sleep")
        
# Eagle class - inherits bird
class Eagle(Bird):
    def eat(self):
        print("This is an eagle! It finds some fish to eat")
        
    def sleep(self):
        print("This is an eagle! It locks its foot in position to sleep in a tree")
        
# Goldfish class - inherits fish
class Goldfish(Fish):
    def eat(self):
        print("This is a goldfish! It eats fish food")
        
    def sleep(self):
        print("This is a goldfish. It doesn't sleep!")
        
def main():
    # List of animal objects
    animals = [Mammal(),Bird(),Fish(),Dog(),Eagle(),Goldfish()]
    # Iterate over animal list
    for animal in animals:
        # Invoke parent method let's eat and let's sleep on object
        # That function will run the eat and sleep methods
        Animal.letsEat(animal)
        Animal.letsSleep(animal)
        
main()