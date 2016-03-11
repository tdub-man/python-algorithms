name = "Quicksort"

def sort(list):
    less = []
    pivotList = []
    more = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = sort(less)
        more = sort(more)
        return less + pivotList + more
