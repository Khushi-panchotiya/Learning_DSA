# 3. Longest Substring Without Repeating Characters

* Pattern: Sliding Window + Hash Set

# Intuition

We need to find the longest substring that contains only unique characters.

A brute-force approach would generate all possible substrings and check whether each one contains duplicate characters, but this would be inefficient.

Instead, we can use the **Sliding Window** technique. The idea is to maintain a window that always contains unique characters. As we expand the window using the `right` pointer, we check whether the current character already exists in the window.

* If it does not exist, we simply add it to the window.
* If it already exists, we shrink the window from the left until the duplicate character is removed.

This guarantees that the window always represents a valid substring with no repeating characters.

# Approach

1. Use two pointers, `left` and `right`, to represent the current window.
2. Use an `unordered_set` to store the characters currently inside the window.
3. Iterate through the string using the `right` pointer:

   * If `s[right]` is already present in the set, repeatedly remove characters from the left side of the window and move `left` forward until the duplicate is removed.
   * Insert `s[right]` into the set.
   * Update the answer using the current window length: `right - left + 1`.
4. Return the maximum length found.

# Why It Works

At any point, the window contains only unique characters.

When a duplicate character is encountered, we remove characters from the left until the window becomes valid again. Since each character is inserted and removed at most once, the algorithm processes the string efficiently in linear time.

# Complexity Analysis

* Time Complexity: **O(n)**

* Code
class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int left = 0;
        unordered_set<char> window;
        int ans = 0;

        for (int right = 0; right < s.size(); right++) {

            while (window.contains(s[right])) {

                window.erase(s[left]);
                left++;

            }

            window.insert(s[right]);

            ans = max(ans, right - left + 1);

        }

        return ans;
    }
};

  * Each character is inserted into and removed from the set at most once.

* Space Complexity: **O(min(n, m))**

  * Where `m` is the size of the character set.
  * In the worst case, the set stores all unique characters in the current window.
