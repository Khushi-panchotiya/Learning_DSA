# 128. Longest Consecutive Sequence

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

The algorithm must run in **O(n)** time.

### Example

```text
Input: [100, 4, 200, 1, 3, 2]
Output: 4

Explanation:
The longest consecutive sequence is [1, 2, 3, 4].
```

---

## Approach

A straightforward solution would be to sort the array and then count consecutive numbers. However, sorting takes **O(n log n)** time, which does not satisfy the problem requirement.

To achieve **O(n)** time complexity, we use a hash set (`unordered_set`) for constant-time lookups.

### Key Observation

A number can be the start of a sequence only if its predecessor does not exist.

For example:

```text
100, 101, 102, 103
```

* 100 is the start because 99 does not exist.
* 101 is not the start because 100 exists.
* 102 is not the start because 101 exists.
* 103 is not the start because 102 exists.

For every valid starting number, we keep checking whether the next consecutive number exists in the set and count the sequence length.

This ensures that every number is processed at most once.

---

## Algorithm

1. Insert all numbers into an `unordered_set`.
2. Iterate through each number in the set.
3. If `x - 1` does not exist, then `x` is the start of a sequence.
4. Expand the sequence by checking `x + 1`, `x + 2`, and so on.
5. Track the maximum sequence length found.
6. Return the maximum length.

---

## Code

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> numSet(nums.begin(), nums.end());

        int long_length = 0;

        for (int x : numSet) {

            // Start only if x is the beginning of a sequence
            if (!numSet.contains(x - 1)) {

                int count = 1;

                while (numSet.contains(x + 1)) {
                    count++;
                    x++;
                }

                long_length = max(long_length, count);
            }
        }

        return long_length;
    }
};
```

---

## Complexity Analysis

### Time Complexity: O(n)

* Building the hash set takes O(n).
* Each number is visited at most once while expanding sequences.
* Total complexity remains O(n).

### Space Complexity: O(n)

* The hash set stores all unique elements from the input array.
