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

## The optimum solution I found

<pre>
  <code>
    class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        
        return k
  </code>
</pre>

#### The one thing I noticed:

While finding the optimum solution for this question, I discovered some micro-factors that can influence your runtime results and code efficiency.

- Variable Proximity: Comparing adjacent indices (like nums[i] and nums[i-1]) is extremely fast because CPUs optimise for sequential memory access.
- Mathematical Overhead: Returning a raw counter (like k) is microseconds faster than returning a calculated value (like j + 1).
- Space-Time Trade-off: Using a Dictionary provides O(n) speed but costs O(n) memory; leveraging the Sorted property allows for the same speed with O(1) memory.
- In-Place Overwriting: Overwriting values (nums[k] = nums[i]) is generally more efficient than Swapping when you don't need to preserve the "junk" data at the end of the array.
