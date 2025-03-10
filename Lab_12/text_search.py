# SKOŃCZONE
import time

def naive_method(S, W):
    m = 0
    i = 0
    found = 0
    comparisons = 0
    length_S = len(S)
    length_W = len(W)

    while m <= length_S - length_W:
        comparisons += 1
        if S[m + i] == W[i]:
            i += 1
            if i == length_W:
                found += 1
                m += 1
                i = 0
        else:
            m += 1
            i = 0
    return found, comparisons

def rabin_karp_search(S, W, d = 256, q = 101):
    length_S = len(S)
    length_W = len(W)
    hW = 0
    hS = 0
    h = 1
    found = 0
    comparisons = 0
    collisions = 0

    for i in range(length_W - 1):
        h = (h * d) % q

    for i in range(length_W):
        hW = (hW * d + ord(W[i])) % q
        hS = (hS * d + ord(S[i])) % q

    for m in range(length_S - length_W + 1):
        comparisons += 1
        if hW == hS:
            if S[m:m + length_W] == W:
                found += 1
            else:
                collisions += 1
        if m < length_S - length_W:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + length_W])) % q
            if hS < 0:
                hS = hS + q
    return found, comparisons, collisions

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'

    # Metoda naiwna
    t_start = time.perf_counter()
    found, comparisons = naive_method(S, W)
    t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(f"{found};{comparisons}")

    # Metoda Rabina - Karpa
    t_start = time.perf_counter()
    found, comparisons, collisions = rabin_karp_search(S, W)
    t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(f"{found};{comparisons};{collisions}")

if __name__ == "__main__":
    main()