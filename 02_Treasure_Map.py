# Make 3 lists with 3 elements for the Map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

# Make a map(list) of the 3 lists above
map = [row1, row2, row3]

# Print out the map
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Put the Treasure in the Map
map[int(position[0]) - 1][int(position[1]) - 1] = "X "

# Print out the Map
print(f"{map[0]}\n{map[1]}\n{map[2]}")
