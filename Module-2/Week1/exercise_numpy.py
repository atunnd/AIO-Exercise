import numpy as np

def create_array():
    arr = np.arange(0, 10, 1)
    print(arr)

def create_boolean_array():
    arr = np.ones((3,3), dtype=bool)
    print(arr)
    arr2 = np.ones((3,3)) > 0
    print(arr2)
    arr3 = np.full((3, 3), fill_value=True, dtype=bool)
    print(arr3)

def select_odd_number():
    arr = np.arange(0, 10)
    print(arr[arr % 2 == 1])
    arr[arr % 2 == 1] = -1
    print(arr)

def reshape_array():
    arr = np.arange(10)
    arr_2d = arr.reshape(2, -1)
    print(arr_2d)

def reshape_concatenate_array():
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=0)
    print('Result: \n', c)
    c2 = np.concatenate([arr1, arr2], axis=1)
    print('Result: \n', c2)

def repeat_array():
    arr = np.array([1, 2, 3])
    print(np.repeat(arr, 3)) # repeat each element
    print(np.tile(arr, 3)) #repeat the whole array

def query_array():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    index = np.where((a >= 5) & (a <= 10))
    print('result', a[index])

def vectorize_array():

    def maxx(x, y):
        if x >= y:
            return x
        else:
            return y
    
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    pair_max = np.vectorize(maxx, otypes=[float])
    print(pair_max(a, b))

def max_value_array():

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    print('Result: ', np.where(a < b, b, a))

if __name__ == '__main__':
    create_array()
    create_boolean_array()
    select_odd_number()
    reshape_array()
    reshape_concatenate_array()
    repeat_array()
    query_array()
    vectorize_array()
    max_value_array()