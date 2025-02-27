from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            if i==k:
                pass
            else:
                if nums.count(i) > nums.count(k):
                    k=i
        return k


instance = Solution().majorityElement([3,2,2,2,2,2,3])
print(instance)