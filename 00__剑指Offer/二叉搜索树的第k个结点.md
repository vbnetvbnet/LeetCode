# 二叉搜索树的第k个结点

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

## Solution

二叉搜索树中根遍历的结果刚好就是排序好的序列。

```java
import java.util.ArrayList;

public class Solution {
    public TreeNode KthNode(TreeNode root, int k) {
        ArrayList<TreeNode> list = new ArrayList<>();
        inorder(root, list);
        
        if (k < 1 || k > list.size()) return null;
        else return list.get(k-1);
    }
    
    private void inorder(TreeNode root, ArrayList<TreeNode> list) {
        if (root == null) return;

        inorder(root.left, list);
        list.add(root);
        inorder(root.right, list);
    }
}
```

实际上并不需要把整个数都遍历完，只需要遍历到第k个数就得到结果了。

```java
public class Solution {
    
    private int count = 0;
    public TreeNode KthNode(TreeNode root, int k) {
        if (root == null) return null;
        
        // check if kth node is in the left subtree
        TreeNode node = KthNode(root.left, k);
        if (node != null) return node;
        // o.w, check if kth node is the root node
        count++;
        if (count == k) return root;
        // o.w, check if kth node is in the right subtree
        node = KthNode(root.right, k);
        if (node != null) return node;
        
        return null;
    }
}
```

