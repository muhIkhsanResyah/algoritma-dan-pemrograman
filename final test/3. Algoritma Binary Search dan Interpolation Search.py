
# Binary Search
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Interpolation Search
def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1


arr = [10, 20, 30, 40, 50]
print("Binary Search 30:", binary_search(arr, 30))
print("Interpolation Search 40:", interpolation_search(arr, 40))
