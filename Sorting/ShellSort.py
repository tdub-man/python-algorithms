import math

name = "ShellSort"

def sort(list):
    inc = len(list) // 2
    while inc:
        for i, el in enumerate(list):
            while i >= inc and list[i - inc] > el:
                list[i] = list[i - inc]
                i -= inc
            list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
