# Create dictionary for word occurences
def word_count(path_to_text):
    words = []
    with open(path_to_text) as file:
        for line in file:
            line = line.rstrip('\n')
            word_in_line = line.split(' ')
            for word in word_in_line:
                words.append(word)
    
    words.sort(key=str.swapcase)
    my_dict = dict.fromkeys(words, 0)
    for word in words:
        my_dict[word] += 1
    
    return my_dict

if __name__ == '__main__':
    word_count('Module-1/Week2/P1_data.txt')