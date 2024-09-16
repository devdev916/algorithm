'''
# 링크
https://leetcode.com/problems/merge-sorted-array/description/

# 문제
88. Merge Sorted Array
두 개의 정수 배열 nums1과 nums2가 주어집니다. 두 배열은 오름차순으로 정렬되어 있으며 두 개의 정수 m(nums1의 원소 개수)과 n(nums2의 원소 개수)도 주어집니다.
이 때 배열 nums1과 nums2를 오름차순인 하나의 배열로 합치세요.
두 개의 배열을 합친 최종 결과는 함수의 리턴값이 아니라 nums1에 정렬된 상태로 저장되어 있어야 합니다. 따라서 입력으로 들어오는 nums1 배열은 m + n의 길이를 가지고, nums1 배열에서 m개의 원소 이후에는 기본값인 0으로 채워져있습니다. nums2는 n의 길이를 가진 배열이 입력으로 들어옵니다.
(문제를 풀 때 다른 배열 혹은 Collections의 자료구조를 추가로 선언하지 말고 입력으로 주어진 배열만 가지고 푸세요. 변수 선언은 상관없습니다.)
'''

### using 내장함수 ###
class Solution(object):
    def merge(self, nums1, m, nums2, n):
      for j in range(n):
          nums1[m+j] = nums2[j]
      nums1.sort()

### 이해필요 ###
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :return
        len1 = len(nums1)
        end_idx = len1-1
        while n > 0 and m > 0 :
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n-=1
            else:
                nums1[end_idx] = nums1[m-1]
                m-=1
            end_idx-=1
        while n > 0:
            nums1[end_idx] = nums2[n-1]
            n-=1
            end_idx-=1