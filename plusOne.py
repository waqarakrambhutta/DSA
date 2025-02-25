from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempStr = ''
        for i in digits:
            tempStr += str(i)
        tempStr = str(int(tempStr) + 1)
        digits.clear()
        for i in range(len(tempStr)):
            digits.insert(i,int(tempStr[i]))
        
        return digits


instance = Solution().plusOne([4,3,2,1])

print(instance)