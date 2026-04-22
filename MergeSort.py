from merge_lists import merge_lists

def merge_sort(arr: list) -> list:

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_lists(left, right)



test_arr = [90, 64, 34, 25, 12, 22, 11]
sorted_arr = merge_sort(test_arr.copy())

print(f"Sorted array is: {sorted_arr}")
print(f"Unsorted array is: {test_arr}")