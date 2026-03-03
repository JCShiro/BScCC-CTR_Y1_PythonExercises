# Exercise One
# Create an array called `fruits` that contains the following strings: "apple", "banana", "cherry".
array = ["apple", "banana", "cherry"]
print(array)

# Exercise Two
# Print the length of the `fruits` array.
print(len(array))

# Exercise Three
# Add the string "orange" at the end of the `fruits` array.
array.append("orange")
# Print the `fruits` array to see the changes.
print(array)

# Exercise Four
# Remove the last element from the `fruits` array.
array.pop()
# Print the `fruits` array to see the changes.
print(array)

# Exercise Five
# Remove the first element from the `fruits` array.
array.pop(0)
# Print the `fruits` array to see the changes.
print(array)

# Exercise Six
# Modify the code form Exercise Five to remove the second element from the `fruits` array instead.
new_array = ["Mercury", "Venus", "Earth", "Mars"]
print(new_array)
new_array.pop(1)
print(new_array)

# Exercise Seven
# Create a new array called `more_fruits` that contains the following strings: "grape", "melon".
more_fruits = ["grape", "melon"]
# Combine the `fruits` and `more_fruits` arrays into a new array called `all_fruits`.
all_fruits = array + more_fruits
# Print the `all_fruits` array to see the combined list of fruits.
print(all_fruits)

# Exercise Eight
# Create a function called `add_fruit` that takes an array of fruits as an argument and a string representing a new fruit.
def add_fruit(fruits):
    
# The function should add the new fruit to the array and return the updated array.
# Call the `add_fruit` function with the `all_fruits` array and a new fruit, then print the result.

# Exercise Nine
# Create a function called `print_fruits` that takes an array of fruits as an argument and prints each fruit on a new line.
# Call the `print_fruits` function with the `all_fruits` array to see the output.
