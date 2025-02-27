from typing import List


class Solution:

    def largestToN(self, arr: List[int],n) -> int:
        arr.sort(reverse=True)
        return arr[:n]        
        


instance = Solution().secondLargest([1,8,6,2,5,4,8,3,7])
print(instance)