# SKOŃCZONE

import time
import random

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return f"{self.key} : {self.value}"
    
class Sort:
    @staticmethod
    def shift_sort(arr):
        n = len(arr)
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if arr[index] > arr[j]:
                    index = j
            arr.insert(i, arr.pop(index))
        return arr
    
    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        h = n // 2
        while h > 0:
            for i in range(h, n):
                temp = arr[i]
                j = i
                while j >= h and arr[j - h] > temp:
                    arr[j] = arr[j - h]
                    j -= h
                arr[j] = temp
            h //= 2
        return arr

def main():

    input_data = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    elements1 = [Element(key, value) for key, value in input_data]
    Sort.shift_sort(elements1)
    print(elements1)
    print("Algorytm jest stabilny.\n")
    
    random_numbers1 = [random.randint(0, 99) for _ in range(10000)]

    t_start1 = time.perf_counter()
    Sort.shift_sort(random_numbers1)
    t_stop1 = time.perf_counter()

    print("Czas obliczeń:", "{:.7f}".format(t_stop1 - t_start1),"\n")


    elements2 = [Element(key, value) for key, value in input_data]
    Sort.shell_sort(elements2)
    print(elements2)
    print("Algorytm jest niestabilny.\n")

    random_numbers2 = [random.randint(0, 99) for _ in range(10000)]

    t_start2 = time.perf_counter()
    Sort.shell_sort(random_numbers2)
    t_stop2 = time.perf_counter()

    print("Czas obliczeń:", "{:.7f}".format(t_stop2 - t_start2),"\n")

    print("Shell sort jest najszybszym z algorytmów, porównując również do heapsorta.")


if __name__ == '__main__':
    main()