def topKFrequent( nums: List[int], k: int) -> List[int]:
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] +=1
        else:
            dic[num] = 1
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    
    ls = list(sorted_dict.keys())
    return ls[0:k]

print(topKFrequent([1,1,1,2,2,3], k = 2))


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        d = {}
        for ele in strs:
            el = ''.join(sorted(ele))
            if el not in d:
                d[el] = []

            d[el].append(ele)
        return list(d.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] +=1
        else:
            dic[num] = 1
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    
    ls = list(sorted_dict.keys())
    return ls[0:k]

