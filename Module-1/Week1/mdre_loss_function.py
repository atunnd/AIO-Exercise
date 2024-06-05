# Calculate the MDRE function
def md_nre_single_sample(y, y_hat, n, p):
    
    loss = (y**(1/n) - y_hat**(1/n)) ** p
    print(loss)

# Main function
def main():
    
    y = float(input('Enter y: '))
    y_hat = float(input('Enter y hat: '))
    n = int(input('Enter n: '))
    p = int(input('Enter p: '))
    md_nre_single_sample(y, y_hat, n, p)
 
if __name__ == '__main__':
    md_nre_single_sample ( y =100 , y_hat =99.5 , n =2 , p =1)
    md_nre_single_sample ( y =50 , y_hat =49.5 , n =2 , p =1)
    md_nre_single_sample ( y =20 , y_hat =19.5 , n =2 , p =1) 
    md_nre_single_sample ( y =0.6 , y_hat =0.1 , n =2 , p =1)