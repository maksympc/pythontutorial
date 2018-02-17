# Chapter 2
# ---Lists---
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]
# Print out house
print(house)
# Print out the type of house
print(type(house))

# ---List slising---
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[:6]
# Use slicing to create upstairs
upstairs = areas[-4:]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)