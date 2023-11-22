def twoSum(nums, target) :
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

print(twoSum([1,2,3,4,5,6,7,8],11))