def string_compare(P, T, i = None, j = None):
    if i is None and j is None:
        i = len(P) - 1
        j = len(T) - 1
    if i == 0:
        return j
    if j == 0:
        return i
    swaps = string_compare(P,T,i-1,j-1) + (P[i] != T[j])
    inserts = string_compare(P,T,i,j-1) + 1
    deletes = string_compare(P,T,i-1,j) + 1
 
    min_cost = min([swaps, inserts, deletes])
   
    return min_cost

def string_compare_PD(P, T):
    D = []
    operations = []
    for i in range(len(P)):
        if i == 0:
            D.append([k for k in range(len(T))])
            operations.append(['X'] + ['I' for k in range(len(T) - 1)])
        else:
            D.append([i] + [0] * (len(T) - 1))
            operations.append(['D'] + ['X'] * (len(T) - 1))     

    for i in range(1,len(P)):
        for j in range(1,len(T)):
            swaps = D[i-1][j-1] + (P[i] != T[j])
            inserts = D[i][j-1] + 1
            deletes = D[i-1][j] + 1
            min_cost = min([swaps, inserts, deletes])
            D[i][j] = min_cost
            if min_cost == swaps:
                if P[i] != T[j]:
                    operations[i][j] = 'S'
                else:
                    operations[i][j] = 'M'
            elif min_cost == inserts:
                operations[i][j] = 'I'
            else:
                operations[i][j] = 'D'

    i = len(P) - 1
    j = len(T) - 1
    path = []
    while operations[i][j] != 'X':
        path.append(operations[i][j])
        if operations[i][j] == 'M' or operations[i][j] == 'S':
            i -= 1
            j -= 1
        elif operations[i][j] == 'I':
            j -= 1
        elif operations[i][j] == 'D':
            i -= 1
    path.reverse()

    return D[len(P) - 1][len(T) - 1], ''.join(path)

def string_compare_PD2(P, T):
    D = []
    for i in range(len(P)):
        if i == 0:
            D.append([0 for k in range(len(T))])
        else:
            D.append([i] + [0] * (len(T) - 1))   

    for i in range(1,len(P)):
        for j in range(1,len(T)):
            swaps = D[i-1][j-1] + (P[i] != T[j])
            inserts = D[i][j-1] + 1
            deletes = D[i-1][j] + 1
            min_cost = min([swaps, inserts, deletes])
            D[i][j] = min_cost

    min_value = float('inf')
    j = 0
    for i in range(len(T)):
        if D[len(P) - 1][i] < min_value:
            min_value = D[len(P) - 1][i]
            j = i

    return j - len(P) + 2
            
def string_compare_PD3(T, P = None):
    if P is None:
        P = ''.join(sorted(T))
    D = []
    operations = []
    for i in range(len(P)):
        if i == 0:
            D.append([k for k in range(len(T))])
            operations.append(['X'] + ['I' for k in range(len(T) - 1)])
        else:
            D.append([i] + [0] * (len(T) - 1))
            operations.append(['D'] + ['X'] * (len(T) - 1))     

    for i in range(1,len(P)):
        for j in range(1,len(T)):
            if P[i] != T[j]:
                swaps = D[i-1][j-1] + float('inf')
            else:
                swaps = D[i-1][j-1]
            inserts = D[i][j-1] + 1
            deletes = D[i-1][j] + 1
            min_cost = min([swaps, inserts, deletes])
            D[i][j] = min_cost
            if min_cost == swaps:
                if P[i] != T[j]:
                    operations[i][j] = 'S'
                else:
                    operations[i][j] = 'M'
            elif min_cost == inserts:
                operations[i][j] = 'I'
            else:
                operations[i][j] = 'D'

    i = len(P) - 1
    j = len(T) - 1
    result = ''
    while operations[i][j] != 'X':
        if operations[i][j] == 'M':
            result += T[j]
            i -= 1
            j -= 1
        elif operations[i][j] == 'S':
            i -= 1
            j -= 1
        elif operations[i][j] == 'I':
            j -= 1
        elif operations[i][j] == 'D':
            i -= 1

    return result[::-1]


print(string_compare(' kot',' pies'))

print(string_compare_PD(' biały autobus',' czarny autokar')[0])

print(string_compare_PD(' thou shalt not',' you should not')[1])

print(string_compare_PD2(' ban',' mokeyssbanana'))

print(string_compare_PD3(' republican',' democrat'))

print(string_compare_PD3(' 243517698'))