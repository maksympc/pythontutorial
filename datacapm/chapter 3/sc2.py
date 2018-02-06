# chapter 3
# Import package

# Definition of radius
r = 0.43

# Import the math package
import math
from math import radians

# Calculate C
C = 2*math.pi*r
Crad = radians(360)*r

# Calculate A
A = math.pi*r**2
Arad = radians(180)*r**2

# Build printout
print("Circumference: " + str(C))
print("Circumference using radians: " + str(Crad))
print("Area: " + str(A))
print("Area using radians: " + str(Arad))
