from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        maxSmall = 0
        if target in nums:
            return nums.index(target)
        else:
            for i,v in enumerate(nums):
                if target>v:
                    maxSmall=v  
            if maxSmall == 0:
                return 0
            else:
                return nums.index(maxSmall) + 1 




ref = Solution().searchInsert([1001], 5)

print(ref)