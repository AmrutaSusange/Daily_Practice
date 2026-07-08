arr = [8, 3, 6, 1]
n = len(arr)
for pas in range(n-1):
    for i in range(n-pas-1):
        arr[i] = min(arr[i:])
    print(arr)