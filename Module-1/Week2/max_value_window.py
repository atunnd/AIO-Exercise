## Find max number
def find_max(window):
    max_value = window[0]
    for i in window:
        if i > max_value:
            max_value = i
    return max_value

# Find max number for each window
def max_window(list_of_number, window):
    len_of_list = len(list_of_number)
    res = []
    for i in range(0, len_of_list - window + 1):
        max_value = find_max(list_of_number[i:i+window:])
        res.append(max_value)
    
    return res

if __name__ == '__main__':
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k=3
    res = max_window(num_list, k)
    print(res)