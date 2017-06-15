class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return false
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[target - nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

    self = 0
    nums = {1,2,3,4}
    target =6
    print(twoSum(self, nums, target))