# 1. BST

- you know the code.

The time complexity of the provided code can be analyzed as follows:

1. **`createBST(Node* root, Node* node)` function**: This function inserts a node into the binary search tree (BST). In the worst case (when the BST is a skewed tree), the time complexity of this function is
   
   O(n)
   
   , where
   
   n
   
   is the number of nodes in the BST.

2. **`inorderTraverse(Node* curNode)` function**: This function traverses the BST in an inorder manner. The time complexity of this function is
   
   O(n)
   
   , where
   
   n
   
   is the number of nodes in the BST.

3. **`main()` function**: In the main function, the `createBST` function is called for each element in the `store` vector. Therefore, the time complexity of the main function is
   
   O(n^2)
   
   in the worst case, where
   
   n
   
   is the number of elements in the `store` vector.

So, the overall time complexity of the code is

O(n^2)

in the worst case. However, if the BST is balanced, the time complexity of the `createBST` function would be

O(\log n)

, and the overall time complexity of the code would be

O(n \log n)

. But the provided `createBST` function does not ensure a balanced BST. Therefore, we consider the worst-case time complexity, which is

O(n^2)

.

Please note that this analysis assumes that the operations of inserting an element into the BST and traversing the BST are the most time-consuming tasks in this code. Other operations are considered to have negligible time complexity in comparison.

I hope this helps! Let me know if you have any other questions. 😊
