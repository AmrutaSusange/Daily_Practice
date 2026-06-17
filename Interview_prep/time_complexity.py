import copy 
ar = [1,2,2,1]

ar2 = []

for i in range(len(ar)-1, -1, -1):
    ar2.append(ar[i])
if ar == ar2:
    print('True')
else:
    print('False')



ar1 = 'amruta'

ar3 = ''

for i in range(len(ar1)-1, -1, -1):
    ar3 = ar3+ar1[i]
if ar1 == ar3:
    print('Its a pallindrome')
else:
    print('not a pallindrom')


# With two pointer approach

ls = [1,2,3,2,1,7]
ls1 = copy.deepcopy(ls)

i = 0
j = len(ls) -1

while (i < j):
    ls1[i], ls1[j] = ls1[j], ls1[i]
    i+=1
    j-=1
if ls == ls1:
    print('True')
else:
    print('False')