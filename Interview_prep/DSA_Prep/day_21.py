def missingNum(arr):
    for ele in range(len(arr)):
        if arr[ele] +1 in arr:
            continue
        else:
            return arr[ele] +1
    
print(missingNum([1,2,3,5]))



def checkElement(arr, num):
    n = len(arr)
    if num < arr[n//2]:
        for i in range(n//2):
            if num == arr[i]:
                return True
        return False
    else:
        for i in range(n//2, n):
            if num == arr[i]:
                return True
        return False
    


print(checkElement([1,2,3,4,5,6,],7))

        

