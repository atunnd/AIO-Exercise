import math

# Check the correct type of number
def is_number(n):
    try: 
        float(n)    # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

# Calculate the value for 3 types of activation function
def activation_function(x, activation_type):

    if (activation_type not in ['sigmoid', 'relu', 'elu']):  # Check for supported activation functions
        print(f'{activation_type} is not supportted')
        return None
    
    if (is_number(x) != True):  # Check for input to be a number
        print(f'{x} must be a number')
        return None
    
    x = float(x)  # Convert x to type float if input is a number

    if (activation_type == 'sigmoid'):  # Calculatethe sigmoid activation function
        sigmoid_function = 1 / (1 + math.e ** (-x))
        print(f"{activation_type}: f({x}) = {sigmoid_function}")
    elif (activation_type == 'relu'):   # Calculate the relu activation function
        relu_function = 0 if x <= 0 else x
        print(f"{activation_type}: f({x}) = {relu_function}")
    elif (activation_type == 'elu'):    # Calculate the elu activation function
        alpha = 0.01
        elu_function = alpha * ((math.e ** x) - 1) if x <= 0 else x
        print(f"{activation_type}: f({x}) = {elu_function}")

# Main function
def main():
    input_x = input('Input x = ')
    if (is_number(input_x) != True):  # Check for input to be a number
        print(f'{input_x} must be a number')
        return None
    
    input_activation_function = input('Input activation Function (sigmoid|relu|elu): ')
    if (input_activation_function not in ['sigmoid', 'relu', 'elu']):  # Check for supported activation functions
        print(f'{input_activation_function} is not supportted')
        return None
    activation_function(input_x, input_activation_function)
    

if __name__ == '__main__':
    main()