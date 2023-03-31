class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1,len(nums)):
            if nums[k] == nums[i]:
                continue
            else:
                nums[k+1]=nums[i]
                k = k+1

        return k+1