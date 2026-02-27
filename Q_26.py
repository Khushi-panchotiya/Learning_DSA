# optimum soltion
class Solution:
  def removeDuplicates(self, nums):
    if not nums:
      return 0
    k = 1  # Initialise the count of unique elements to 1
    for i in range(1, len(nums)):
      if nums[i] != nums[i - 1]:
        nums[k] = nums[i]  # Overwrite the next unique element
          k += 1
    return k

# The solution I think of 
class Solution(object):
  def removeDuplicates(self, nums):
    unique = {}
    k = 0
    for i,value in enumerate(nums):
      if value not in unique:
        nums[i], nums[k] = nums[k], nums[i]
        k += 1
        unique[value] = i
      else:
        continue
    return k  
  
