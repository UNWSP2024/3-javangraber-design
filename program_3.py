# Programmer: Javan Graber
# Date: February 5, 2026

# Programming Exercise 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	                            Price Per Pound
# 2 pounds or less   	                    $1.50
# Over 2 pounds but not more than 6 pounds  $3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	                        $4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0

    ######################
    # Calculate for less than or equal to 2 pounds
    if weight <= 2:
        shippingCost = 1.50

    # Calculate for greater than 2 but no more than 6 pounds
    elif weight > 2 and weight <= 6:
        shippingCost = 3.00

    # Calculate for greater than 6 but no more than 10 pounds
    elif weight > 6 and weight <= 10:
        shippingCost = 4.00

    # Calculate for over 10 pounds
    elif weight > 10:
        shippingCost = 4.75

    # Create the total shipping cost formula
    totalShippingCost = shippingCost * weight

    # Print the total shipping cost
    print(f'Total shipping cost: $ {totalShippingCost:.2f}')
    ######################

    return shippingCost


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))
