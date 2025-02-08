# Write your solution here
from string import ascii_uppercase

input_layers = int(input("Layers: "))

# the formula to use at multiple places
loop_through = input_layers + (input_layers - 1)
center = ( loop_through ) // 2 

# looping through 
for i in range(loop_through):
    for j in range(loop_through):
        # computing both the row and column distance from center
        row_distance_from_center = abs(center - i)
        column_distance_from_center  = abs(center - j)
         
        # comparing and using that distance value as index value
        if row_distance_from_center <= column_distance_from_center:
            print(ascii_uppercase[column_distance_from_center],end="")
        else:
            print(ascii_uppercase[row_distance_from_center],end="")

    print()