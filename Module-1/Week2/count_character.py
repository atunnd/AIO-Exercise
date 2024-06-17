# Sort the list in alphabetic order
def sort_alphabet(target):
    for i in range(len(target)):
        for j in range(len(target)):
            if target[i] < target[j]:
                temp = target[i]
                target[i] = target[j]
                target[j] = temp
    
    return target

# Dictionay for occurences of character
def count_char(string):
    a = list(string)
    sort_alphabet(a)
    my_dict = dict.fromkeys(a, 0)

    for i in a:
        my_dict[i] += 1
    
    return my_dict


if __name__ == '__main__':

    string = "Happiness"
    res = count_char(string)
    print(res)