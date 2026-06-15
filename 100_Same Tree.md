# 100. Same Tree - Recursive DFS Solution (C++)

## Intuition

Two binary trees are considered the same if they have the same structure and the corresponding nodes contain the same values.

Since each subtree is itself a binary tree, recursion is a natural fit. At every step, we compare the current nodes and recursively verify their left and right subtrees.

## Approach

1. If both nodes are `nullptr`, return `true`.
2. If one node is `nullptr` and the other is not, return `false`.
3. If the node values differ, return `false`.
4. Recursively compare:
   - Left subtree of both trees.
   - Right subtree of both trees.
5. Return `true` only if both recursive calls return `true`.

## Complexity Analysis

### Time Complexity
- **O(n)**

Each node is visited exactly once.

### Space Complexity
- **O(h)**

Where `h` is the height of the tree due to the recursion stack.

- Balanced tree: **O(log n)**
- Skewed tree: **O(n)**

## Code

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        if (p == nullptr && q == nullptr)
            return true;

        if (p == nullptr || q == nullptr)
            return false;

        if (p->val != q->val)
            return false;

        return isSameTree(p->left, q->left)
            && isSameTree(p->right, q->right);
    }
};
