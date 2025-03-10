    m, n = len(P), len(T)
    D = np.zeros((m, n), dtype=int)
    parent = np.full((m, n), 'X', dtype=str)

    for j in range(1, n):
        parent[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            choices = [(D[i - 1][j - 1] + (P[i] != T[j]), 'S' if P[i] != T[j] else 'M'),  # match/substitute
                       (D[i][j - 1] + 1, 'I'),  # insertion
                       (D[i - 1][j] + 1, 'D')]  # deletion
            D[i][j], parent[i][j] = min(choices, key=lambda x: x[0])
