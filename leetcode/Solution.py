class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums))[i+1:]:
                if nums[i]+nums[j] == target:
                    return[i,j]

s = Solution()
print(s.twoSum([3,2,4],6))
