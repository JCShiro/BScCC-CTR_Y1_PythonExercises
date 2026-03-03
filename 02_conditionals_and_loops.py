# Exercise One
# Create a boolean variable and assign it a value of either True or False
boolean_variable = True
# Create an if / else statement that prints "is true" when the variable is True, and "is false" when the variable is False.
if boolean_variable:
    print("True!")
else:
    print("False!")
# Run the script and change the variable's value to test the difference.

# Exercise Two
# Create a variable with name x and assign it the value 10
x = 10
# Create a variable with name y and assign it the value 5
y = 5
# Create an if / else statement that prints "x is higher than y" or "y is higher than x" accordingly.
if x > y:
    print("X is higher than Y")
else:
    print("Y is higher than X")
# Run the script and switch the values of x and y around to test the difference.


# Exercise Three
# Create a function called `is_even` that takes a number as an argument and returns True if the number is even, and False if it is odd.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
# Hint: You may need to use google to learn how to test if a number is odd or even!
# Call the `is_even` function with an even number and print the result to see the output.
test = is_even(22)
print(test)
# Call the `is_even` function with an odd number and print the result to see the output.
print(is_even(15))
# Exercise Four
# Create a while loop that loops through 100 values of a variable `i` and prints them
i = 0
while i in range(100):
    print(i)
    i += 1
# Execise Five
# Create a for loop that achieves the same as the loop in exercise Four
i = 0
for i in range(100):
    print(i)