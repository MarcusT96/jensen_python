def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
           
        # Sista i element redan på plats därför n - i - 1
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Byt plats
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True                

            # Om inga byten: klar!
        if not swapped:
          break        

    return arr

nums = [64, 34, 25, 12, 22]
bubble_sort(nums)

print(nums)  # [12, 22, 25, 34, 64]
