# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    left = start
    right = end
    
    middle = (left + right) // 2

    if len(arr) < 1:
        return -1

    if left == right and arr[middle] != target:
        return -1
    

    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
        # target is at the left side of the array
        left = start
        right = middle -1
        return binary_search(arr, target, left , right)
    else:
        # target is at the right of the array
        left = middle +1
        right = end
        return binary_search(arr, target, left, right)





arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr1, 12, 0, len(arr1)-1))
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here





## works but does not return the index, returns the found number 
# def binary_search(arr, target, start, end):

#     left = start
#     right = end
    
#     middle = (left + right) // 2

#     # if len(arr) == 1:
#     #     print('last item')

#     if arr[middle] == target:
#         return middle
#     elif arr[middle] > target:
#         # target is at the right side of the array
#         arr = arr[:middle]
#         return binary_search(arr, target, start, middle)
#     else:
#         # target is at the left of the array
#         arr = arr[middle:]
#         return binary_search(arr, target, start, middle)