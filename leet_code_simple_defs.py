def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

def pivotIndex(nums):
        Sum_left = 0
        Sum_right = sum(nums)
        print(Sum_right)
        for i in range(len(nums)):
            Sum_right -= nums[i]
            print(Sum_right,Sum_left)
            if Sum_left == Sum_right:
                return i
            Sum_left += nums[i]
        return -1

thing = pivotIndex([1,7,3,6,5,6])
print(thing)


