# 647. Palindromic Substrings

## Problem Statement

Given a string `s`, return the number of palindromic substrings in it.

A palindrome is a string that reads the same forward and backward. A substring is a contiguous sequence of characters within the string.

**Example 1:**

```text
Input: s = "abc"
Output: 3
```

**Explanation:** `"a"`, `"b"`, and `"c"` are palindromic substrings.

**Example 2:**

```text
Input: s = "aaa"
Output: 6
```

**Explanation:** `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, and `"aaa"`.

---

## Intuition

A palindrome expands symmetrically around its center.

Instead of generating every possible substring and checking whether it is a palindrome, we can directly find palindromes by expanding outward from their centers.

There are two possible types of centers:

1. **Odd-length palindromes** → centered at a character.
   - Example: `"aba"`

2. **Even-length palindromes** → centered between two characters.
   - Example: `"abba"`

By expanding from every possible center, we can count all palindromic substrings efficiently.

---

## Approach

For each index `i` in the string:

1. Count all odd-length palindromes centered at `i`.
2. Count all even-length palindromes centered between `i` and `i + 1`.
3. Expand outward while:
   - indices remain within bounds
   - characters at both ends are equal

Each successful expansion represents a valid palindrome, so increment the count.

Finally, return the total count.

---

## Dry Run

Consider:

```text
s = "aaa"
```

### Center at index 0

```text
"a"
```

Count = 1

### Center between 0 and 1

```text
"aa"
```

Count = 1

### Center at index 1

```text
"a"
"aaa"
```

Count = 2

### Center between 1 and 2

```text
"aa"
```

Count = 1

### Center at index 2

```text
"a"
```

Count = 1

Total = 6

---

## Complexity Analysis

### Time Complexity

**O(n²)**

For each position, we expand around the center. In the worst case (`"aaaa..."`), each expansion can traverse the entire string.

### Space Complexity

**O(1)**

Only a few variables are used; no extra data structures are required.

---

## C++ Solution

```cpp
class Solution {
public:
    
    int expand(string& s, int left, int right) {
        int count = 0;

        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }

        return count;
    }

    int countSubstrings(string s) {
        int ans = 0;

        for (int i = 0; i < s.size(); i++) {
            // Odd length palindromes
            ans += expand(s, i, i);

            // Even length palindromes
            ans += expand(s, i, i + 1);
        }

        return ans;
    }
};
```

## Key Takeaway

The crucial observation is that every palindrome has a center. Expanding around each possible center allows us to count all palindromic substrings in **O(n²)** time while using **O(1)** extra space.
