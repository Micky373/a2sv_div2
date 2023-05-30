class CustomSort(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]

        sorted_nums = sorted(nums,key=CustomSort)

        final = ''.join(sorted_nums)

        final = final.lstrip("0")

        if final == "":
            final = "0"

        return final


