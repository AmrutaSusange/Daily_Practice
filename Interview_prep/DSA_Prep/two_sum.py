def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
        


def twoSum(nums: List[int], target: int) -> List[int]:
        out = {}
        for i in nums:
            if i in out:
                out[i] +=1
            else:
                 out[i] =1


             