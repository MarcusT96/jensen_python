def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1                

        # Flytta element större än key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1                

        # Sätt in key på rätt plats
        arr[j + 1] = key
        
    return arr

# Exempel
nums = [12, 11, 13, 5, 6]

insertion_sort(nums)

print(nums)  # [5, 6, 11, 12, 13]
