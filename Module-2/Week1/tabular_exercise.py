import pandas as pd
import numpy as np

def max_vales_index_sales(df):
    max_val = df['Sales'].max()
    idx = df[df['Sales'] == max_val].index.values
    print(f'Max: {max_val} - Index: {idx[0]}')

def average_tv(df):
    avg_val = df['TV'].mean() 
    print(f'Average value of tv: {avg_val}')

def count_sales(df):
    sales_record_count = df[df['Sales'] >= 20].count()[0]
    print(f'Number of record in sales being larger than 20: {sales_record_count}')

def average_radio_constraint_sales(df):
    avg_radio_records = df[df['Sales'] >= 15]['Radio'].mean()
    print(f'Average radio record with sales >= 15: {avg_radio_records}')

def average_sales_constraint_newspaper(df):
    avg_newspaper = df['Newspaper'].mean()
    sum_sales = df[df['Newspaper'] > avg_newspaper].sum()['Sales']
    print(f'Sum of sales record with newspaper value being larger than its average: {sum_sales}')

def scord_sales_average(df):
    avg_sales = df['Sales'].mean()
    scores = ['Good' if score > avg_sales else ('Average' if score == avg_sales else 'Bad') for score in df['Sales']]
    print(scores[7: 10])

def score_sales_average(df):
    avg_sales = df['Sales'].mean()
    scores = ['Good' if score > avg_sales else ('Average' if score == avg_sales else 'Bad') for score in df['Sales']]
    print(scores[7: 10])

def score_sales_approximate_average(df):
    avg_sales = df['Sales'].mean()
    approximate_avg = 0
    min_diff = avg_sales
    for i in df['Sales']:
        if abs(i - avg_sales) < min_diff:
            approximate_avg = i
            min_diff = abs(i - avg_sales)
    scores = ['Good' if score > approximate_avg else ('Average' if score == approximate_avg else 'Bad') for score in df['Sales']]
    print(scores[7: 10])

if __name__ == '__main__':
    df = pd.read_csv('Module-2/Week1/advertising.csv')
    max_vales_index_sales(df)
    average_tv(df)
    count_sales(df)
    average_radio_constraint_sales(df)
    average_sales_constraint_newspaper(df)
    score_sales_average(df)
    score_sales_approximate_average(df)