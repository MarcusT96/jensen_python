def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Hitta minsta i osorterad del
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Byt till sorterad del
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test
nums = [64, 25, 12, 22, 11]

selection_sort(nums)

print(nums)  # [11, 12, 22, 25, 64]
