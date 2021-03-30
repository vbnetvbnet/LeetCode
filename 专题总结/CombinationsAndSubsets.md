# Combinations and Subsets
`组合(combine(nums, k))`是从`nums`里选`k`个数

而`subsets(nums)`是输出`nums`的所有子集，因此有

```
subsets(nums) = combine(nums, 0) + combine(nums, 1) + ... + combine(nums, n)
```

## 问题1: combine(nums, k)
- Input: a set of **distinct** integers, `nums` and an integer `k`
- Output: All the combinations of length `k` choosing from `nums`

Example:

```
Input: nums = [1, 2, 3]
Output: [[1, 2], [1, 3], [2, 3]]
```

## Solution

```java
    // M(i): Get all combinations of length `k` starting from index `i`
    // Base case: k==0 (Should NOT use "prefix.size()==k" because the value of `k` keeps changing at every iteration)
    // Solution: M(0)
    static List<List<Integer>> combine(int[] nums, int k) {
        List<List<Integer>> result = new ArrayList<>();
        combine(nums, k, 0, new ArrayList<>(), result);
        return result;
    }

    private static void combine(int[] nums, int k, int i, List<Integer> prefix, List<List<Integer>> result) {
        if (k==0) {
            result.add(new ArrayList<>(prefix));
            return;
        }

        if (i == nums.length) return;
        // 包含当前元素
        prefix.add(nums[i]);
        combine(nums, k-1, i+1, prefix, result);
        prefix.remove(prefix.size()-1);             // clean up - 恢复prefix的值

        // 不包含当前元素
        combine(nums, k, i+1, prefix, result);
    }
```

当然也可以这样写：

```java
    private static void combine2(int[] nums, int k, int i, List<Integer> prefix, List<List<Integer>> result) {
        if (k==0) {
            result.add(new ArrayList<>(prefix));
            return;
        }

        for (int j=i; j<nums.length; j++) {
            prefix.add(nums[j]);
            combine2(nums, k-1, j+1, prefix, result);
            prefix.remove(prefix.size()-1);             // clean up - restore the value of `prefix`
        }
    }
```

## 问题2: subsets(nums)
Example:

```
Input: nums = [1,2,3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

Note that the order of subsets in the output does not matter.

## Solution

```java
    // 方法一：Backtracking
    // M(i): Get all possible subsets starting from index `i`
    // Corner case: prefix=[], i=0; prefix=nums, i=n
    // Solution: M(0)
    static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        subsets(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void subsets(int[] nums, int i, List<Integer> prefix, List<List<Integer>> result) {
        if (i == nums.length) {
            result.add(new ArrayList<>(prefix));
            return;
        }

        // 包含当前元素
        prefix.add(nums[i]);
        subsets(nums, i+1, prefix, result);
        prefix.remove(prefix.size()-1);     // clean up - 恢复prefix的值

        // 不包含当前元素
        subsets(nums, i+1, prefix, result);
    }

    // 方法二：Backtracking (输出是有序的)
    // subsets(nums) = combine(nums, 0) + combine(nums, 1) + ... + combine(nums, n)
    static List<List<Integer>> subsets2(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i=0; i<=nums.length; i++) {
            subsets2(nums, i, 0, new ArrayList<>(), result);
        }
        return result;
    }

    private static void subsets2(int[] nums, int k, int i, List<Integer> prefix, List<List<Integer>> result) {
        if (k == 0) {
            result.add(new ArrayList<>(prefix));
            return;
        }

        for (int j=i; j<nums.length; j++) {
            // subsets(prefix=prefix+nums[i]
            prefix.add(nums[j]);
            subsets2(nums, k-1, j+1, prefix, result);
            // clean up - restore value of prefix
            prefix.remove(prefix.size()-1);
        }
    }

    // 方法三：Bit Operation
    static List<List<Integer>> subsets3(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        final int MAX_VALUE = 1 << nums.length;   // 2^n
        for (int i=0; i<MAX_VALUE; i++) {
            int mask = i;
            List<Integer> list = new ArrayList<>();
            int ndx = 0;
            while (mask > 0) {
                // 每次都判断mask最后一位是否为1
                int lastDigit = mask & 1;
                if (lastDigit == 1) list.add(nums[ndx]);
                ndx++;
                mask = mask >> 1;
            }
            result.add(list);
        }
        return result;
    }
```

Take [1,2,3] for example, the masks are

| Binary | Decimal |
| ------- | ---------- |
| 000 | 0 |
| 001 | 1 |
| 010 | 2 |
| 011 | 3 |
| 100 | 4 |
| 101 | 5 |
| 110 | 6 |
| 111 | 7 |

So, we can use decimal values of 0 ~ 2^n-1 as masks and for each bit in a mask include the corresponding number in our list if that bit is `1`.
