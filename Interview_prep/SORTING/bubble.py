arr = [1,2,3,4]
n = len(arr)
for pas in range(n-1):
    for i in range(n-pas-1):
        if arr[i] > arr[i+1]:
            swaped =True
            if swaped == True:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                break
        else:
            continue
    print(arr)

