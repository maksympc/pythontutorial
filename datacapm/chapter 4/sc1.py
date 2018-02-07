# chapter 4
# Numpy
#
# Multiplication and division with numpy arrays
# height and weight are available as a regular lists
height = [66,67,68,69,70,71,75,76,77,78]
weight = [160,162,164,166,168,170,172,174,176,178]
# Import numpy
import numpy as np
# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254
# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight)*0.453592
# Calculate the BMI: bmi
bmi = np_weight_kg/(np_height_m**2)
# Print out bmi
print(bmi)

# Boolean arrays
# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = bmi < 21
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Subsetting
# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)
# Print out the weight at index 50
print(np_weight[50]) 
# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
