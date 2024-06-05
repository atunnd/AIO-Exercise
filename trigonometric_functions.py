# Check the correct type of number
def is_number(n):
    try: 
        float(n)    # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

# Calculate the factorial of number x
def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

# Calculate value for function sin
def approx_sin(x, n):
    
    assert is_number(x) and is_number(n), 'x and n must be numbers'
    assert n > 0, 'n must be larger than 0'

    x = float(x)  # Convert x to float if x is string
    n = int(n)    # Convert n to int if n is string

    sin_x = 0
    for i in range(n+1):
        sin_x += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) 
    print(sin_x)

# Calculate value for function cos
def approx_cos(x, n):
    
    assert is_number(x) and is_number(n), 'x and n must be numbers'
    assert n > 0, 'n must be larger than 0'

    x = float(x)  # Convert x to float if x is string
    n = int(n)    # Convert n to int if n is string

    cos_x = 0
    for i in range(n+1):
        cos_x += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) 
    print(cos_x)

# Calculate value for function sinh
def approx_sinh(x, n):
    
    assert is_number(x) == True and is_number(n) == True, 'x and n must be numbers'
    assert n > 0, 'n must be larger than 0'

    x = float(x)  # Convert x to float if x is string
    n = int(n)    # Convert n to int if n is string

    sinh_x = 0
    for i in range(n+1):
        sinh_x += (x ** (2 * i + 1)) / factorial(2 * i + 1) 
    print(sinh_x)

# Calculate value for function cosh
def approx_cosh(x, n):
    
    assert is_number(x) and is_number(n), 'x and n must be numbers'
    assert n > 0, 'n must be larger than 0'

    x = float(x)  # Convert x to float if x is string
    n = int(n)    # Convert n to int if n is string

    cosh_x = 0
    for i in range(n+1):
        cosh_x += (x ** (2 * i)) / factorial(2 * i) 
    print(cosh_x)

# Main Function 
def main():

    x = float(input('Enter x: '))
    n = int(input('Enter n: '))
    if (n <= 0):
        print('n must be larger than 0')
        return None
    approx_sin(x, n)
    approx_cos(x, n)
    approx_cos(x, n)
    approx_cosh(x, n)

if __name__ == '__main__': 

    approx_sin(x='3.14', n = 10)
    approx_cos(x=3.14, n = 10)
    approx_sinh(x=3.14, n = 10)
    approx_cosh(x=3.14, n = 10)