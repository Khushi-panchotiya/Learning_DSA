## Intuition

A cycle exists in a linked list if we can revisit a node by continuously following the `next` pointers.

There are two common approaches to detect a cycle:

### Approach 1: Hash Set

As we traverse the linked list, we store the address of each visited node in a hash set.

- If a node is encountered again, it means we have already visited it, so a cycle exists.
- If we reach `nullptr`, the list has no cycle.

### Approach 2: Floyd's Cycle Detection Algorithm (Fast & Slow Pointers)

To avoid using extra memory, we can use two pointers:

- `slow` moves one step at a time.
- `fast` moves two steps at a time.

If a cycle exists, the fast pointer will eventually catch up to the slow pointer inside the cycle.

If no cycle exists, the fast pointer will reach the end of the list.

---

## Approach 1: Hash Set

### Algorithm

1. Create an unordered set to store visited node addresses.
2. Traverse the linked list.
3. If the current node already exists in the set, return `true`.
4. Otherwise, insert the node into the set and continue.
5. If the traversal reaches `nullptr`, return `false`.

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Code

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> visited;

        while (head) {
            if (visited.count(head))
                return true;

            visited.insert(head);
            head = head->next;
        }

        return false;
    }
};
```

---

## Approach 2: Floyd's Fast & Slow Pointer Algorithm (Optimal)

### Algorithm

1. Initialize two pointers, `slow` and `fast`, at the head.
2. Move:
   - `slow` by one step.
   - `fast` by two steps.
3. If they ever point to the same node, a cycle exists.
4. If `fast` or `fast->next` becomes `nullptr`, no cycle exists.

### Why It Works

Inside a cycle, the fast pointer gains one node on the slow pointer during every iteration.

This is similar to two runners on a circular track:
- One runner moves twice as fast.
- Eventually, the faster runner catches up to the slower runner.

Therefore, if a cycle exists, the two pointers are guaranteed to meet.

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Code

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (fast == slow) {
                return true;
            }
        }

        return false;
    }
};
```

---

## Comparison

| Approach | Time | Space |
|-----------|---------|---------|
| Hash Set | O(n) | O(n) |
| Fast & Slow Pointers | O(n) | O(1) |

The Fast & Slow Pointer approach is preferred because it achieves the same time complexity while using constant extra space.

---

### Tags

`Linked List` `Two Pointers` `Fast and Slow Pointers` `Floyd's Cycle Detection` `Hash Set` `Cycle Detection` `O(1) Space` `Blind 75` `LeetCode`
