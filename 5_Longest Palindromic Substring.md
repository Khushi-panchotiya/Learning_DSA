# 5. Longest Palindromic Substring

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

### Example 1

```text
Input: s = "babad"
Output: "bab"

Explanation: "aba" is also a valid answer.
```

### Example 2

```text
Input: s = "cbbd"
Output: "bb"
```

---

## Intuition

A palindrome reads the same forwards and backwards. Every palindrome has a center:

* Odd-length palindrome: `"aba"` → center is `'b'`
* Even-length palindrome: `"abba"` → center is between the two `'b'`s

Instead of checking every possible substring, we can expand outward from each possible center and find the longest palindrome centered there.

---

## Approach: Expand Around Center

For each index `i` in the string:

1. Treat `i` as the center of an odd-length palindrome.
2. Treat the gap between `i` and `i + 1` as the center of an even-length palindrome.
3. Expand outward while the characters match.
4. Keep track of the longest palindrome found.

### Example

For `s = "babad"`:

```text
b a b a d
    ^
```

Expanding around index `2`:

```text
b
aba
```

Length = 3

The algorithm repeats this process for every possible center and returns the longest palindrome found.

---

## Algorithm

1. Initialize `start` and `end` to store the boundaries of the current longest palindrome.
2. Iterate through each character in the string.
3. Find:

   * The longest odd-length palindrome centered at `i`.
   * The longest even-length palindrome centered between `i` and `i + 1`.
4. Take the maximum length from both cases.
5. If a longer palindrome is found, update `start` and `end`.
6. Return the substring from `start` to `end`.

---

## Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n²) |
| Space Complexity | O(1)  |

---

## C++ Solution

```cpp
class Solution {
public:
    int expand(string& s, int left, int right) {
        while (left >= 0 &&
               right < s.size() &&
               s[left] == s[right]) {
            left--;
            right++;
        }

        return right - left - 1;
    }

    string longestPalindrome(string s) {
        int start = 0;
        int end = 0;

        for (int i = 0; i < s.size(); i++) {

            int len1 = expand(s, i, i);       // Odd-length palindrome
            int len2 = expand(s, i, i + 1);   // Even-length palindrome

            int len = max(len1, len2);

            if (len > end - start + 1) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substr(start, end - start + 1);
    }
};
```

---

## Key Learning

The key observation is that every palindrome can be expanded from its center. By leveraging this property, we avoid checking all possible substrings and improve the brute-force solution from **O(n³)** to **O(n²)** while using only **O(1)** extra space.
