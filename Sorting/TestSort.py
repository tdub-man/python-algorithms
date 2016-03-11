from random import shuffle
import BubbleSort
import InsertionSort
import ShellSort
import Quicksort

x = [1,2,3,4,5,6,7,8,9]
methods = [BubbleSort,InsertionSort,ShellSort,Quicksort]
for m in methods:
    shuffle(x)
    print("Unsorted: {0} == {1}".format(x,m.name))
    m.sort(x)
    print("  Sorted: {0} == {1}".format(x,m.name))
