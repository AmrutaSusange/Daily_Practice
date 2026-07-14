def sumZero(arr):
	e_set = set()
	i = 0
	j = len(arr) -1
	lst = []
	while i < j:
		arr = sorted(arr)
		if arr[i] + arr[j] ==0:
			if (arr[i], arr[j]) in e_set:
				i +=1
				j -=1
				continue
			else:
				e_set.add((arr[i], arr[j]))
				lst.append ([arr[i], arr[j]])
			i+=1
			j-=1   
		elif arr[i] + arr[j] < 0: 
				i+=1
		else:
				j-=1
	return lst

print(sumZero([6, 1, 8, 0, 4, -9, - 1, -10, -6, -5]))



#------------------------------------------------duplicate numbers fron list

def dupNum(arr):
	ls = []
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] == arr[j]:
				ls.append(arr[i])
			else:
				continue
	return  ls

print(dupNum([12, 3, 1, 2, 3]))
               

def dupNum(arr):
	ls = []
	i = 1
	j = len(arr) -1

	while i< j:
		if arr[i] - arr[j] ==0:
			ls.append(arr[i])
			i+=1
			j-=1
			continue
		else:
			i+=1
			j-=1
	return ls

print(dupNum([2, 3, 1, 2, 3]))


def dupDic(arr):
    dic = {}
    ls = []
    for char in arr:
        if char in dic:
            dic[char] +=1
        else:
            dic[char] =1
        
    for key, val in dic.items():
        if val >1:
             ls.append(key)
        else:
             continue
    return ls



print(dupDic([2, 3, 1, 2, 3]))

# Dictionary mein in check O(1) hota hai — hashmap ki wajah se direct access milta hai, loop nahi chalta.
# List mein in check O(n) hota hai


