## 📖 Problem

A biker starts a road trip at altitude `0`.

Given an integer array `gain`, where `gain[i]` represents the net gain (or loss) in altitude between points `i` and `i + 1`, return the **highest altitude** reached during the trip.

---

## 💡 Intuition

Since each value in the `gain` array represents a change in altitude, we can continuously update the biker's current altitude as we traverse the array.

Instead of storing every altitude in a separate array, we only need:

* `currAlt` → Current altitude after processing each gain.
* `highAlt` → Highest altitude encountered so far.

This reduces the space complexity from **O(n)** to **O(1)**.

---

## 🚀 Approach

1. Initialize:

   * `currAlt = 0`
   * `highAlt = 0`

2. Traverse the `gain` array:

   * Add the current gain to `currAlt`.
   * Update `highAlt` if `currAlt` becomes larger.

3. Return `highAlt`.

---

## ✅ Example

**Input**

```text
gain = [-5,1,5,0,-7]
```

**Altitude Progression**

```text
0 → -5 → -4 → 1 → 1 → -6
```

**Highest Altitude**

```text
1
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```text
O(n)
```

We iterate through the array exactly once.

### Space Complexity

```text
O(1)
```

Only two integer variables are used.

---

## 💻 Code

```cpp
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int currAlt = 0;
        int highAlt = 0;

        for (int i = 0; i < gain.size(); i++) {
            currAlt += gain[i];
            highAlt = max(highAlt, currAlt);
        }

        return highAlt;
    }
};
```

---

### 🏷️ Tags

`Array` `Prefix Sum` `Simulation` `LeetCode Easy` `C++` `O(1) Space`
