name = "InsertionSort"

def sort(list):
    for i in range(1,len(list)):
        newVal = list[i]
        j = i
        while j > 0 and list[j-1] > newVal:
            list[j] = list[j-1]
            j -= 1
        list[j] = newVal
