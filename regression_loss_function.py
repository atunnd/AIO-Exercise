import math
import random
import numpy as np
random.seed(1)

# Calculate regresison loss on 3 methods
def regression_loss_function(n, loss_name):
    
    if (n.isnumeric() == False):  # Check for n to be a number
        print(f'number of samples must be an integer number')
        return None
    
    n = int(n) # Convert n to a number of input for n is string
    
    if(loss_name == 'MAE'):  # Calculate the MAE loss
        loss = 0
        for i in range(n):
           prediction = random.uniform(0, 10)
           target = random.uniform(0, 10)
           loss += abs(target - prediction)
           print(f'loss name: {loss_name}, sample: {i}, pred: {prediction}, target: {target},')
           print(f'\tloss: {loss}')
        
        final_loss = loss/n
        print(f'final {loss_name}: {final_loss}')

    elif(loss_name == 'MSE'):  # Calculate the MSE loss
        loss = 0
        for i in range(n):
           prediction = random.uniform(0, 10)
           target = random.uniform(0, 10)
           loss += (target - prediction)**2
           print(f'loss name: {loss_name}, sample: {i}, pred: {prediction}, target: {target},')
           print(f'\tloss: {loss}')
        
        final_loss = loss/n
        print(f'final {loss_name}: {final_loss}')
    
    elif(loss_name == 'RMSE'):  # Calculate the RMSE loss
        loss = 0
        for i in range(n):
           prediction = random.uniform(0, 10)
           target = random.uniform(0, 10)
           loss += abs(target - prediction)
           print(f'loss name: {loss_name}, sample: {i}, pred: {prediction}, target: {target},')
           print(f'\tloss: {loss}')
        
        final_loss = math.sqrt(loss/n)
        print(f'final {loss_name}: {final_loss}')

# Main function
def main():
    input_n = input('Input number of samples (integer number) which are generated: ')
    if (input_n.isnumeric() == False):  # Check for n to be a number
        print(f'number of samples must be an integer number')
        return None
    loss_name = input('Input loss name: ')
    regression_loss_function(input_n, loss_name)

if __name__ == '__main__':
    main()
