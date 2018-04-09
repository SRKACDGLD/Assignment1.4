# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:15:07 2018

@author: srk
Assignment 1.4: Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3
"""

Sphere_dia = 12 # Diameter of the sphere is given as 12cm

Sphere_rad = Sphere_dia / 2  # Calculating the radius value

Sphere_vol = (4/3) * (3.1416) * (Sphere_rad**3) # Calculation as per Volume of Sphere formula

print("Volume of the Sphere with 12cm as Diameter is: ",Sphere_vol) # printing of output - Sphere volume value

# End of the code