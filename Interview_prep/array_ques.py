arr = [5, 7, 2, 7, 5, 2, 5] 

count = {}
def count_num(arr):

    for num in arr:
            if num in count:
                count[num] +=1
            else:
                count[num] =1

    for nums, counts in count.items():
            if counts %2 != 0:
                return nums
    
print(count_num(arr))