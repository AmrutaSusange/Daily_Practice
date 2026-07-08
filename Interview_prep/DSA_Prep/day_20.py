
def sunstringOne(s):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '1' :
            for j in range(i+1, n):
                if s[j] == '1' :
                 count +=1
                else:
                   continue
        else:
           continue
    return count
            
                
print(sunstringOne('101011'))



# with permutation combination way

def binarySubstring(s):
   count = 0
   for ele in range(len(s)):
      if s[ele] == '1':
         count +=1
   return (count * (count-1)) // 2


print(binarySubstring('1111'))