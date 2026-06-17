## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Intuition

To maximize profit, we need to buy at the lowest price before selling at a higher price in the future.

Instead of checking every possible buy-sell pair, we can keep track of the minimum stock price seen so far while traversing the array. For each day, we calculate the profit if we sell on that day and update the maximum profit accordingly.

---

## Approach

1. Initialize `minPrice` with the first stock price.
2. Traverse the array once.
3. For each price:

   * Update `minPrice` if a lower price is found.
   * Calculate the profit obtained by selling at the current price.
   * Update the maximum profit if this profit is greater than the current maximum.
4. Return the maximum profit.

---

## Dry Run

### Example

```text
prices = [7,1,5,3,6,4]
```

| Price | Min Price So Far | Profit | Max Profit |
| ----- | ---------------- | ------ | ---------- |
| 7     | 7                | 0      | 0          |
| 1     | 1                | 0      | 0          |
| 5     | 1                | 4      | 4          |
| 3     | 1                | 2      | 4          |
| 6     | 1                | 5      | 5          |
| 4     | 1                | 3      | 5          |

**Answer = 5**

---

## Complexity Analysis

### Time Complexity

**O(n)**

We traverse the array only once.

### Space Complexity

**O(1)**

Only a few variables are used regardless of the input size.

---

## C++ Solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minPrice = prices[0];

        for (int price : prices) {
            minPrice = min(minPrice, price);
            profit = max(profit, price - minPrice);
        }

        return profit;
    }
};
```

⭐ If you found this solution helpful, consider giving the repository a star.
