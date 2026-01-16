data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    tail = data[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(data))