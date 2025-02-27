from typing import List


class Solution:

    def largestToN(self, arr: List[int],n) -> int:
        arr.sort(reverse=True)
        return arr[:n]
    
    def maxArea(self, height: List[int]) -> int:
        index = self.largestToN(height, 2)
        
        return index
    

inst = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(inst)
        

        