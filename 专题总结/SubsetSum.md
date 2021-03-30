# SubsetSum系列总结

## 问题1: 判断一个集合是否存在一个子集使得该子集的和等于sum
- Problem: Subset Sum
- Input: An `array` with n integers and `sum`
- Return: whether there is a subset of integers that adds up to `sum`

## Solution:
M(sum, i) = 从index `i` 到数组末尾（index `n-1`)，是否有一个subset of integers that adds up `sum`.

Then our solution would be: M(sum, 0)

```java
    static boolean subsetSum(int[] nums, int sum) {
        return sumsetSum(nums, sum, 0);
    }
    
    static boolean sumsetSum(int[] nums, int sum, int i) {
        if (i == nums.length) {
            return sum == 0;
        }
        return sumsetSum(nums, sum-nums[i], i+1) ||    // 包含当前元素
                sumsetSum(nums, sum, i+1);             // 不包含当前元素
    }
```

对于Base case，可能写成下面这样会更intuitive，但是这样不能处理输入是空数组的特殊情况。

```java
    if (i == nums.length-1) {
        return nums[i] == sum;
    }
```

Running Time: 每一个数都有2个状态：包含或不包含，所以是O(2^n)

## 问题2: 如果我们希望输出这些子集呢？
```java
    static void subsetSum(int[] nums, int sum) {
        boolean[] included = new boolean[nums.length];
        subsetSum(nums, sum, 0, included);
    }

    static void subsetSum(int[] nums, int sum, int i, boolean[] included) {
        if (i == nums.length) {
            if (sum == 0) {
                for (int j = 0; j < nums.length; j++) {
                    if (included[j]) System.out.print(" " + nums[j]);
                }
                System.out.println();
            }
            return;
        }

        included[i] = true;     // 包含当前元素
        subsetSum(nums, sum - nums[i], i+1, included);

        included[i] = false;    // 不包含当前元素
        subsetSum(nums, sum, i+1, included);
    }
```

这种方式较为低效，因为每次输出时都遍历所有的数去判断是否included = true。可以使用一个ArrayList `prefix`来保存已选的数。

```java
    static void subsetSum(int[] nums, int sum) {
        subsetSum(nums, sum, 0, new ArrayList<>());
    }

    static void subsetSum(int[] nums, int sum, int i, ArrayList<Integer> prefix) {
        if (i == nums.length) {
            if (sum == 0) {
                System.out.println(prefix);
            }
            return;
        }

        // 包含当前元素
        prefix.add(nums[i]);
        subsetSum(nums, sum - nums[i], i+1, prefix);
        prefix.remove(prefix.size()-1);     // 恢复prefix的值

        // 不包含当前元素
        subsetSum(nums, sum, i+1, prefix);
    }
```

## 问题3：如果只需要输出满足条件的子集的个数呢？

```java
    // return the count of subsets whose sum equal to `sum`
    static int subsetSum(int[] nums, int sum) {
        return subsetSum(nums, sum, 0);
    }

    static int subsetSum(int[] nums, int sum, int i) {
        if (i == nums.length) {
            if (sum == 0) {
                return 1;
            }
            return 0;
        }

        int count = 0;
        count += subsetSum(nums, sum - nums[i], i+1);
        count += subsetSum(nums, sum, i+1);
        return count;
    }
```