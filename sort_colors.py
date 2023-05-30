import itertools

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        reds = []
        whites = []
        blues = []

        for num in nums:
            if num == 0:
                reds.append(num)
            
            elif num == 1:
                whites.append(num)

            else:
                blues.append(num)

        final_nums = list(itertools.chain(reds,whites,blues))
        
        for i in range(len(final_nums)):
            nums[i] = final_nums[i]

