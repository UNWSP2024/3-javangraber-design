# Programmer: Javan Graber
# Date: February 5, 2026

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

#Show prices
hot_dog = 3.50
chili_dog = 4.50
cheese = 0.50
peppers = 0.75
grilled_onions = 1.00
no_side = 0.00

# Determine what type of hotdog the user wants.
hot_dog_type = str(input('Do you want a hot dog or a chili dog (no capitals)? '))

# Determine the additions to the hotdog, if any.
hot_dog_addition = str(input('Do you want cheese, peppers, or grilled onions (or write none)? '))

# Determine the price of the hot dog if hot dog and any addition
if hot_dog_type == 'hot dog' and hot_dog_addition == 'none':
    hot_dog_price = hot_dog + no_side
elif hot_dog_type == 'hot dog' and hot_dog_addition == 'cheese':
    hot_dog_price = hot_dog + cheese
elif hot_dog_type == 'hot dog' and hot_dog_addition == 'peppers':
    hot_dog_price = hot_dog + peppers
elif hot_dog_type == 'hot dog' and hot_dog_addition == 'grilled onions':
    hot_dog_price = hot_dog + grilled_onions

# Determine the price of the hot dog if chili dog and any addition
elif hot_dog_type == 'chili dog' and hot_dog_addition == 'none':
    hot_dog_price = chili_dog + no_side
elif hot_dog_type == 'chili dog' and hot_dog_addition == 'cheese':
    hot_dog_price = chili_dog + cheese
elif hot_dog_type == 'chili dog' and hot_dog_addition == 'peppers':
    hot_dog_price = chili_dog + peppers
elif hot_dog_type == 'chili dog' and hot_dog_addition == 'grilled onions':
    hot_dog_price = chili_dog + grilled_onions
else:
    print('Sorry, you have entered an invalid input')

# Show the tax value as a decimal
tax_value = .07

# Print the original hot dog cost
print(f'The original hot dog price is ${hot_dog_price:.2f}')

# Find and print the total tax
total_tax = tax_value * hot_dog_price
print(f'The total tax is: ${total_tax:.2f}')

# Calculate the formula for the total price
total_price = hot_dog_price + total_tax

# Print the total price
print(f'The total price is ${total_price:.2f}')
