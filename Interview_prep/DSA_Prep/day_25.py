#Repeat and missind element identification


def misIdentify(arr):
    emp_set = set()
    for i in range(len(arr)):
        if arr[i] in emp_set:
            repeat = arr[i]
        else:
            emp_set.add(arr[i])
    
    actual_sum = sum(arr)
    for mis in arr:
        total_sum = (len(arr) * (len(arr)+1)) // 2
        missing = total_sum - (actual_sum - repeat)

        return [repeat, missing]
    


print(misIdentify([4, 3, 6, 2, 1, 1]))


## leader elements prob

def leaders(arr):
    leader = arr[-1]
    ls = [leader]

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            ls.append(leader)
    return ls
        

print(leaders([16, 17, 4, 3, 5, 2]))

