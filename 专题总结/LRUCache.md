# [146. LRU Cache](https://leetcode-cn.com/problems/lru-cache/)


Design and implement a data structure for . It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.  
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Follow up:**  
Could you do both operations in **O(1)** time complexity?

**Example:**

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```



## Idea

使用HashMap保存key-value pairs，使用双链表保存access order

## Solution

- 方法一：

```java
import java.util.HashMap;
import java.util.Map;

class LRUCache {

    private int capacity;

    private ListNode head = new ListNode(0, 0);
    private ListNode tail = new ListNode(0, 0);
    private Map<Integer, ListNode> map = new HashMap<>();


    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.pre = head;
    }

    public int get(int key) {
        ListNode node = map.get(key);
        if (node == null) return -1;

        moveToFirst(node);
        return node.value;
    }

    public void put(int key, int value) {
        // If already exists, update
        if (get(key) != -1) {       // order updated
            map.get(key).value = value;
            return;
        }

        // If size reaches capacity, remove last node, then insert newNode
        if (capacity <= 0) return;
        if (map.size() == capacity) {
            remove(tail.pre);
        }

        insertFront(new ListNode(key, value));
    }


    private void moveToFirst(ListNode node) {
        remove(node);
        insertFront(node);
    }

    private void remove(ListNode node) {
        map.remove(node.key);
        ListNode pre = node.pre;
        ListNode next = node.next;
        pre.next = next;
        next.pre = pre;
    }

    private void insertFront(ListNode node) {
        map.put(node.key, node);
        ListNode first = head.next;
        head.next = node;
        node.pre = head;
        node.next = first;
        first.pre = node;
    }


    private static class ListNode {
        int key;
        int value;
        ListNode pre;
        ListNode next;

        ListNode(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
```

- 方法二：继承LinkedHashMap

```java
class LRUCache extends LinkedHashMap<Integer, Integer> {
    private int capacity;
    
    public LRUCache(int capacity) {
        super(capacity, 0.75F, true);   // true: access-order, false: insertion-order
        this.capacity = capacity;
    }

    public int get(int key) {
        return super.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }
    
    // Returns true if this map should remove its eldest entry.
    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }
}
```

