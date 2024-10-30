'''
# 링크
https://leetcode.com/problems/two-sum

# 문제
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

# 예시
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

'''

### 무차별대입법 ###
# 시간복잡도 O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found


### 해시테이블 ###
# 시간복잡도 O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = {}  # 빈 딕셔너리 생성
        n = len(nums)

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            hashtable[num] = i

        return []  # No solution found
