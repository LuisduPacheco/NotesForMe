class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    result = 0
    for i in range(len(nums) - 1):
      for j in range(i+1,len(nums)):
        result = nums[i] + nums[j]
        if result == target:
          print(result)
          return [i, j]
    return []
two_sum = Solution()
two_sum.twoSum([1,4,5,6], 9)