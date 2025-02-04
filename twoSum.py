
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]

        index = 0
        for i in nums:
            for j,v in enumerate(nums):
                if nums[index] + v == target and index!=j:
                    output.append(index)
                    output.append(j)
                    return output
                else:
                    pass
            index += 1
        

ret = Solution().twoSum([2,7,11,15], 9)

print(ret)

# arr = input('nums = ')
# arr = arr.strip("[]").split(",")
# if arr:
#     arr = list(map(int, arr))
# else:
#     arr = []

# target = int(input('target = '))

# output = []

# # def myStrip(string):
# #     for i in str

# def twosum():
#     if len(arr) <= 2: 
#         print('Array length must be greater than 2')
#     else:
#         index = 0
#         for i in arr:
#             for j,v in enumerate(arr):
#                 if arr[index] + v == target and index!=j:
#                     # print(arr[index] + v)
#                     # print(arr[index])
#                     # print(v)
#                     output.append(arr[index])
#                     output.append(v)
#                     print(output)
#                     return
#                 else:
#                     pass
#             index += 1

# twosum()