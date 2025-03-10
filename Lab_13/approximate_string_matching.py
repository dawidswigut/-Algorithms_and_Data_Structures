# SKOŃCZONE
import numpy as np
#import time

def string_compare(P: str, T: str, i = None, j = None):
    if i is None and j is None:
        i, j = len(P) - 1, len(T) - 1
    if i == 0:
        return j
    if j == 0:
        return i
    changes = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    insertion = string_compare(P, T, i, j - 1) + 1
    deletion = string_compare(P, T, i - 1, j) + 1
    return min(changes, insertion, deletion)

def string_compare_pd(P: str, T: str):
    m, n = len(P), len(T)
    D = np.zeros((m, n), dtype = int)
    parent = np.full((m, n), 'X', dtype = str)

    for i in range(1, m):
        D[i][0] = i
        parent[i][0] = 'D'
    for j in range(1, n):
        D[0][j] = j
        parent[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            choices = [(D[i - 1][j - 1] + (P[i] != T[j]), 'S' if P[i] != T[j] else 'M'),  # match/substitute
                       (D[i][j - 1] + 1, 'I'),  # insertion
                       (D[i - 1][j] + 1, 'D')]  # deletion
            D[i][j], parent[i][j] = min(choices, key = lambda x: x[0])

    return D, parent

def reconstruct_path(parent):
    i, j = parent.shape[0] - 1, parent.shape[1] - 1
    path = []
    while parent[i][j] != 'X':
        path.append(parent[i][j])
        if parent[i][j] == 'M' or parent[i][j] == 'S':
            i -= 1
            j -= 1
        elif parent[i][j] == 'I':
            j -= 1
        elif parent[i][j] == 'D':
            i -= 1
    return ''.join(path[::-1])

def string_compare_subsequence(P: str, T: str):
    m, n = len(P), len(T)
    D = np.zeros((m, n), dtype = int)
    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = 0

    parent = np.full((m, n), 'X', dtype = str)
    for j in range(1, n):
        parent[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            choices = [(D[i - 1][j - 1] + (P[i] != T[j]), 'S' if P[i] != T[j] else 'M'),  # match/substitute
                       (D[i][j - 1] + 1, 'I'),  # insertion
                       (D[i - 1][j] + 1, 'D')]  # deletion
            D[i][j], parent[i][j] = min(choices, key = lambda x: x[0])

    min_value = np.inf
    end_index = 0
    for i in range(n):
        if D[m - 1][i] < min_value:
            min_value = D[m - 1][i]
            end_index = i

    return end_index - m + 2, D, parent

def find_best_match_subsequence(P: str, T: str):
    end_index, _, _ = string_compare_subsequence(P, T)
    return end_index

def longest_common_subsequence(P: str, T: str):
    m, n = len(P), len(T)
    D = np.zeros((m, n), dtype=int)
    parent = np.full((m, n), 'X', dtype=str)

    for i in range(1, m):
        D[i][0] = i
        parent[i][0] = 'D'
    for j in range(1, n):
        D[0][j] = j
        parent[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            if P[i] == T[j]:
                choices = [(D[i - 1][j - 1], 'M'),  # match
                           (D[i][j - 1] + 1, 'I'),  # insertion
                           (D[i - 1][j] + 1, 'D')]  # deletion
            else:
                choices = [(D[i - 1][j - 1] + np.inf, 'S'),  # substitute (very high cost)
                           (D[i][j - 1] + 1, 'I'),  # insertion
                           (D[i - 1][j] + 1, 'D')]  # deletion
            D[i][j], parent[i][j] = min(choices, key = lambda x: x[0])

    return D, parent

def reconstruct_lcs(parent, P):
    i, j = parent.shape[0] - 1, parent.shape[1] - 1
    lcs = []
    while parent[i][j] != 'X':
        if parent[i][j] == 'M':
            lcs.append(P[i])
            i -= 1
            j -= 1
        elif parent[i][j] == 'S':
            i -= 1
            j -= 1
        elif parent[i][j] == 'I':
            j -= 1
        elif parent[i][j] == 'D':
            i -= 1
    return ''.join(lcs[::-1])

def longest_increasing_subsequence(T: str):
    P = ''.join(sorted(set(T)))
    _, parent = longest_common_subsequence(P, T)
    lcs = reconstruct_lcs(parent, P)
    return lcs

def main():

    P = ' kot'
    T = ' pies'
    #t_start = time.perf_counter()
    print(string_compare(P, T))
    #t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    P = ' biały autobus'
    T = ' czarny autokar'
    #t_start = time.perf_counter()
    D, _ = string_compare_pd(P, T)
    #t_stop = time.perf_counter()
    print(D[-1, -1])
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    P = ' thou shalt not'
    T = ' you should not'
    #t_start = time.perf_counter()
    _, parent = string_compare_pd(P, T)
    path = reconstruct_path(parent)
    #t_stop = time.perf_counter()
    print(path)
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    P = ' ban'
    T = ' mokeyssbanana'
    #t_start = time.perf_counter()
    end= find_best_match_subsequence(P, T)
    #t_stop = time.perf_counter()
    print(end)
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    P = ' democrat'
    T = ' republican'
    #t_start = time.perf_counter()
    _, parent = longest_common_subsequence(P, T)
    lcs = reconstruct_lcs(parent, P)
    #t_stop = time.perf_counter()
    print(lcs)
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    T = ' 243517698'
    #t_start = time.perf_counter()
    lis = longest_increasing_subsequence(T)
    #t_stop = time.perf_counter()
    print(lis)
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

if __name__ == '__main__':
    main()