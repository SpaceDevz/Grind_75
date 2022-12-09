class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Sliding Window Technique
        """

        if len(nums) <= 2:
            return nums

        for item, idx in enumerate(nums):
            if sum([nums[idx], nums[idx-1]]) == target:
                return [idx, idx+1]
            

print(Solution().twoSum([2, 7, 11, 15], 9))