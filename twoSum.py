class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements_to_index = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if nums[i] in complements_to_index.keys():
                return [complements_to_index[nums[i]], i]
            complements_to_index[complement] = i