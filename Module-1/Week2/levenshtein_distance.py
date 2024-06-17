import numpy as np

# Find the min among 3 numbers


def find_min_of_three(a, b, c):
    min_value = a
    if a > b:
        min_value = b
    if b > c:
        min_value = c

    return min_value


def levenshtein_distance(string_s, string_t):
    len_of_s = len(string_s)
    len_of_t = len(string_t)
    list_of_s = list(string_s)
    list_of_t = list(string_t)
    mat = np.zeros((len_of_s+1, len_of_t+1), dtype=int)

    for i in range(0, len_of_s+1):
        mat[i, 0] = i
    for j in range(0, len_of_t+1):
        mat[0, j] = j

    for i in range(1, len_of_s+1):
        for j in range(1, len_of_t+1):
            min_val = find_min_of_three(
                mat[i-1, j-1], mat[i-1, j], mat[i, j - 1])
            if list_of_s[i-1] != list_of_t[j-1]:
                min_val += 1
            mat[i, j] = min_val

    return mat[len_of_s, len_of_t]


if __name__ == '__main__':
    S = "yu"
    T = "you"
    dis = levenshtein_distance(S, T)
    print(dis)
