# Input: arr[] = [10, 8, 30, 4, 5], × = 5
# Output: 4
# Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is
# at index 4. So, the output is 4.


arr = [10, 8, 30, 4, 5]
x = 5

for i in range(len(arr)):
    if arr[i] == x:
        print(i)


#so with this solution the complexity is O(n)

