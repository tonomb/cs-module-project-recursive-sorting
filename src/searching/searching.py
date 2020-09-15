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




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    if arr[0] < arr[1]:
        left = 0
        right = len(arr) -1
        
        while left <= right:

            middle = (right + left) // 2

            if arr[middle] == target:
                return middle
            elif arr[middle] > target:
                # toss out the left side of the array 
                right = middle - 1 

            else:
                left = middle + 1
                
        return -1  # not found

    else:
        left = 0
        right = len(arr) -1
        while left <= right:
            middle = (right + left) // 2

            if arr[middle] == target:
                return middle
            elif arr[middle] > target:  # 45 < -17
                # toss out the left side of the array 
                left = middle + 1 
                
            else:
                right = middle - 1
                
                
        return -1  # not found





ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

print(agnostic_binary_search(ascending, 47))


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