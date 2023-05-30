class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_nums = sorted(nums)

        output = [sorted_nums.index(num) for num in nums]

        return output