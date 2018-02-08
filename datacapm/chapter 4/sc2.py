# chapter 4
# Multidimensional NumPy arrays

# baseball array
baseball = [[ 74, 180],
            [ 74, 215],
            [ 72, 210],
            [ 72, 210],
            [ 73, 188],
            [ 69, 176],
            [ 69, 209],
            [ 71, 200],
            [ 75, 205],
            [ 75, 190],
            [ 73, 195],
            [ 73, 180]]
# Import numpy package
import numpy as np
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)
# Print out the 10th row of np_baseball
print(np_baseball[9,:])
# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]
# Print out height of 12th player
print(np_baseball[11,0])

# 2d arithmetic, convert from inches and pounds to meters and kilos
updated = np.array([1,1])
# Print out addition of np_baseball and updated
print(np_baseball+updated)
# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592])
# Print out product of np_baseball and conversion
print(np_baseball * conversion)

# avarage and median values
np_baseball = np.array(baseball)
# Create np_height from np_baseball
np_height = np_baseball[:,0]
# Print out the mean of np_height
print(np.mean(np_height))
# Print out the median of np_height
print(np.median(np_height))

# mean, median, std, corrcoef examples 
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))

# FIFA stats
# football playres params
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170, 187, 183, 173, 188, 183, 180, 188, 175, 193, 180, 185, 170, 183, 173, 185, 185, 168, 190]
positions = ['GK', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'A', 'A', 'M', 'D', 'A', 'D', 'M', 'GK', 'D', 'D', 'M', 'M', 'M', 'M', 'D', 'M', 'GK']

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights) 
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
