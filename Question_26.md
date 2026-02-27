# 26. Remove Duplicates from Sorted Array

## The first solution I think of
<pre>
  <code>
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
  </code>
</pre>

**Space complexity: O(n)** <br>
**Time complexity: O(n)** <br>

#### The problem: 
The input is already sorted, so I don't need to maintain a dictionary. I can simply use 2 pointers approach.
