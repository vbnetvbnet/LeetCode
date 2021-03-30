# 链表中倒数第k个结点

输入一个链表，输出该链表中倒数第k个结点。

## Idea

Two-Pointers. First move fast pointer k steps, then move two pointers together, until fast pointer reach the end (when `fast == null`).

## Solution

```java
/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
        
        ListNode fast = head, slow = head;
        // fast pointer move k steps
        for (int i=0; i<k; i++) {
            if (fast == null) return null;
            fast = fast.next;
        }
        // two pointers move together
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}
```

