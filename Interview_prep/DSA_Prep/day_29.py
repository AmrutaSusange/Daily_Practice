## Binary search

def zeroCount(arr):

    start = 0
    end = len(arr) -1
    ans = -1

    while start < end:
        mid = (end + start) //2
        if arr[mid] ==1:
            start = mid+1
        else:
            ans = mid
            end = mid
    return len(arr) - ans



print(zeroCount([1,1,1,1,1,1,1,1,1,0,0,0]))




## first and last occurance of element using binary search

def valueIndex(arr,x):
    start = 0
    end = len(arr) -1
    first_index = -1
    last_index = -1

    while start < end:
        mid = (start + end) //2
        if arr[mid] == x:
            first_index = mid
            end = mid
        elif arr[mid] < x:
            start = mid + 1  
        else:
            end = mid - 1 

    start = 0
    end = len(arr) -1

    while start < end:
        mid = (start + end) //2
        if arr[mid] == x:
            start = mid +1
            last_index = mid +1
        elif arr[mid] < x:
            start = mid + 1 
        else:
            end = mid -1

    return [first_index, last_index]

print(valueIndex([1,3,5,5,5,5,67,123,125],5))