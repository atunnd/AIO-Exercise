
# Calculate the precistion, recall and f1-score
def model_evaluation(
        tp, fp, fn):
    
    if (type(tp) != int):          # Check for correct type of tp
        print('tp must be int')
        return None
    
    if (type(fp) != int):          # Check for correct type of fp
        print('fp must be int')
        return None
    
    if (type(fn) != int):          # Check for correct type of fn
        print('fn must be int')
        return None
    
    if (tp <= 0 or fp <= 0 or fn <= 0):
        print('tp and fp and fn must be greater than zero')   # Check for positive values
        return None
    
    precision = tp / (tp + fp)   # Calculate precision
    recall = tp / (tp + fn)      # Calculate recall
    f1_score = 2 * (precision * recall) / (precision + recall)   # Calculate f1-score

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')

    return f1_score

# Main function
def main():
    tp = int(input('Enter value for tp: '))
    fp = int(input('Enter value for fp: '))
    fn = int(input('Enter value for fn: '))

    model_evaluation(tp, fp, fn)

if __name__ == "__main__":
    main()