##https://leetcode.com/problems/two-sum/
##Given an array of integers, return indices of the two numbers such that they add up to a specific target.
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
from collections import *
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##target is 9
        ##2 needs 7, check to see if 7 is in the list
        ##YMU because you didn't know how to initialize a default value for dict, use lambda
        ##YMU YOU KEEP TRYING TO ACCESS DEFAULT DICT AS IF THAT WERE THE NAME OF THE DICTIONARY
        visited = defaultdict(lambda: -1)
        for i in range(len(nums)):
            component = target - nums[i]
            ##YMU, you don't know how to search for a value in a dictionary
            if visited[component] >= 0:
                return [visited[component],i]
            ##YMU, the pointer was a bit off
            ##YMU before by putting the wrong index, keep in mind you have to store the value of the nums array as the key
            ##because that's what you're trying to match with component
            visited[nums[i]] = i

d = Solution().twoSum
print(d([2, 7, 11, 15],17))