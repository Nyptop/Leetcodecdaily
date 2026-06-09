class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        smallest = 999999999
        largest = 0
        for l in range(0, len(nums)):
            if nums[l] < smallest:
                smallest = nums[l]
            if nums[l] > largest:
                largest = nums[l]
        if len(nums) == 1:
            return 0
        return (largest - smallest) * k
