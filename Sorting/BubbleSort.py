name = "BubbleSort"

def swap(list,i,j):
    t = list[i]
    list[i] = list[j]
    list[j] = t

def sort(list):
    top = len(list)-1
    while True:
        sorted = True
        for i in range(0,top):
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                sorted = False
        if sorted:
            break
