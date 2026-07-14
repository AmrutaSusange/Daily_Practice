# smallest distance between two given numbers


def smallDist(arr,x,y):
    x_index = -1
    y_index = -1
    ans = float('inf')
    for i in range(len(arr)):
        if arr[i] == x:
            x_index = i
        elif arr[i] == y:
            y_index = i
        else:
            continue

        if x_index > -1 and y_index > -1:
            return min(ans, abs(x_index - y_index))
        else:
            -1


print(smallDist([10,20,30,40,50], 10, 50))




# Input: arrl = [1, 4, 45, 6, 10, S), target = 16
# Output: true
# Explanation: arr[3] + arr[4] = 6 + 10 = 16.


def tarketSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if target == arr[i]+arr[j]:
                return True
    return False
        



print(tarketSum([1, 4, 45, 6, 10, 5], 16))
        