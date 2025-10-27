def merge_sort(arr):
    if len(arr) <= 1: 
        return arr  

    # Dela
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])

    # Kombinera (merge) 
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1

    result.extend(left[i:])
    result.extend(right[j:]) 

    return result

nums = [64, 34, 25, 12, 22]
sorted_nums = merge_sort(nums)

print(sorted_nums)  # [12, 22, 25, 34, 64]