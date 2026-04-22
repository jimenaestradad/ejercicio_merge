'''
Merge two sorted lists
'''
def merge_lists(arr1: list, arr2: list) -> list:
    i = 0
    j = 0
    merged = []

    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# Test
arr1 = [11, 25, 64, 90]
arr2 = [12, 22, 34]

merged_arr = merge_lists(arr1, arr2)

print(f"Merged array is: {merged_arr}")