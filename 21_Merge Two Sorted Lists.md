# 21. Merge Two Sorted Lists

## Problem

Given the heads of two sorted linked lists `list1` and `list2`, merge them into a single sorted linked list and return its head.

---

## Intuition

Since both linked lists are already sorted, we can merge them similarly to the merge step of Merge Sort.

We maintain two pointers, one for each list, and repeatedly select the smaller node. Instead of creating new nodes, we reuse the existing nodes and update their `next` pointers.

A dummy node is used to simplify the implementation by avoiding special handling for the head of the merged list.

---

## Approach

1. Create a dummy node and a `tail` pointer.
2. Traverse both lists using two pointers.
3. Compare the current nodes:

   * Attach the smaller node to `tail->next`.
   * Move the corresponding pointer forward.
4. Move `tail` forward after each attachment.
5. Once one list is exhausted, connect the remaining nodes of the other list.
6. Return `dummy.next` as the head of the merged list.

---

## Dry Run

### Input

```text
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4
```

### Steps

```text
Compare 1 and 1 → take 1 from list1
Merged: 1

Compare 2 and 1 → take 1 from list2
Merged: 1 -> 1

Compare 2 and 3 → take 2
Merged: 1 -> 1 -> 2

Compare 4 and 3 → take 3
Merged: 1 -> 1 -> 2 -> 3

Compare 4 and 4 → take 4 from list1
Merged: 1 -> 1 -> 2 -> 3 -> 4

list1 exhausted
Attach remaining nodes from list2

Final: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

---

## Complexity Analysis

### Time Complexity

```text
O(n + m)
```

where:

* `n` = length of `list1`
* `m` = length of `list2`

Each node is processed exactly once.

### Space Complexity

```text
O(1)
```

No additional linked list is created. We only use a few pointers and a dummy node.

---

## C++ Solution

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (list1 && list2){

            if (list1->val <= list2->val){
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }

            tail = tail->next;
        }

        tail->next = list1 ? list1 : list2;

        return dummy.next;
    }
};
```

---

## Key Learning

* Linked lists can often be manipulated by changing pointers instead of creating new nodes.
* A dummy node simplifies linked list construction.
* This solution achieves optimal **O(n + m)** time and **O(1)** extra space complexity.
