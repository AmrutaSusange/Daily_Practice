nums = [1,1,1,3,3,4,3,2,4,2]
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                else:
                    continue
        return False

ans = Solution()
print(ans.containsDuplicate(nums))

# But this solution is having o(n^2) time complexity

def containsDuplicate(self, nums: List[int]) -> bool:
        track = {}
        for i in range(len(nums)):
            if nums[i] in track:
                track[nums[i]] +=1
            else:
                track[nums[i]] =1
        
        for key, val in track.items():
            if val > 1:
                return True
            else:
                continue
        return False

# This one is better with o(n) time complexity but we have to trade space complexity here which is o(n)

def containsDuplicate(self, nums: List[int]) -> bool:
    track = {}
    for i in range(len(nums)):
        if nums[i] in track:
            return True
        else:
            track[nums[i]] =1
    return False

# fastest

def containsDuplicate(self, nums: List[int]) -> bool:
    track = set()
    for i in range(len(nums)):
        if nums[i] in track:
            return True
        else:
            track.add(nums[i])
    return False