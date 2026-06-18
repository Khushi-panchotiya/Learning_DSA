# 125. Valid Palindrome

## Problem

Given a string `s`, determine whether it is a palindrome after:

* Converting all uppercase letters to lowercase.
* Removing all non-alphanumeric characters.

A palindrome reads the same forward and backward.

## Example

```text
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric characters and converting to lowercase:
"amanaplanacanalpanama"
which is a palindrome.
```

---

## Approach: Two Pointers

Instead of creating a new filtered string, we use two pointers:

* `l` starts from the beginning.
* `r` starts from the end.

### Steps

1. Skip non-alphanumeric characters from the left.
2. Skip non-alphanumeric characters from the right.
3. Compare the lowercase versions of both characters.
4. If they differ, return `false`.
5. Move both pointers inward and continue.

This approach avoids extra space and processes the string in a single pass.

---

## Complexity Analysis

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

* Each character is visited at most once.
* No additional string or data structure is used.

---

## C++ Solution

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {

            if (!isalnum(s[l])) {
                l++;
                continue;
            }

            if (!isalnum(s[r])) {
                r--;
                continue;
            }

            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};
```

---

## Key Takeaway

This is a classic **Two Pointers** problem where we compare characters from both ends while skipping invalid characters. The solution achieves **O(n)** time complexity with **O(1)** extra space.
