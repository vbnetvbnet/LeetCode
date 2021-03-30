# Merge Two Sorted Arrays

- 写法一

```java
private int[] merge(int[] nums1, int[] nums2) {
    int m = nums1.length;
    int n = nums2.length;

    int[] result = new int[m+n];
    int i=0, j=0, index=0;

    while (true) {
        // 如果nums1已用完，则直接把nums2剩下的元素全部复制到result即可
        if (i == m) {
            while (j < n) result[index++] = nums2[j++];
            break;
        }
        // 如果nums2已用完，直接把nums1剩下的元素全部复制到result
        if (j == n) {
            while (i < m) result[index++] = nums1[i++];
            break;
        }
        // 否则，复制较小的元素
        result[index++] = (nums1[i] <= nums2[j])? nums1[i++] : nums2[j++];
    }
    // Note: 执行完之后`index`的值恰好是结果数组的大小
    return result;
}
```

- 写法二（推荐）

```java
private int[] merge2(int[] nums1, int[] nums2) {
    int m = nums1.length;
    int n = nums2.length;

    int[] nums = new int[m+n];
    int i=0, j=0, index=0;

    while (i<m && j<n) {
        nums[index++] = (nums1[i] <= nums2[j])? nums1[i++] : nums2[j++];
    }
    while (i<m) nums[index++] = nums1[i++];
    while (j<n) nums[index++] = nums2[j++];

    return nums;
}
```

- 写法三

```java
private int[] merge3(int[] nums1, int[] nums2) {
    int m = nums1.length;
    int n = nums2.length;

    int[] nums = new int[m+n];
    int i=0, j=0, index=0;

    while (i<m || j<n) {
        // 只有在这些情况下才有可能取j指向的数
        if (i==m || (j<n && nums2[j] < nums1[i])) {
            nums[index++] = nums2[j++];
        } else {
            nums[index++] = nums1[i++];
        }
    }

    return nums;
}
```

