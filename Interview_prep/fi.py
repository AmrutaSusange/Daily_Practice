def productExceptSelf( nums: List[int]) -> List[int]:
    res = []
    lef = []
    rig = []
    prod = 1
    val = 1
    for i in range(len(nums)):
        lef.append(prod)    # store product so far
        prod *= nums[i] 
        rig.append(val)

    for i in range(len(nums)-1, -1, -1):
        rig.append(val)
        val *= nums[i]
    rig.reverse()
    return rig

print(productExceptSelf([1,2,3,4]))