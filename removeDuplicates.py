from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0 
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j  

instance = Solution().removeDuplicates([1,1,1,1])
print(instance)
