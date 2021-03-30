# 和为S的两个数字

输入一个**递增排序**的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

## Example

```
Input: nums = [1, 3, 4, 6, 7, 8]	S = 10
Output: [3, 7]
```

## Idea

注意到这是一个已排序的数组，可以使用夹逼法。对于多解的情况，外层的乘积比内层的要小。比如：3x7 要小于 4x6. 因此可以设置两个指针分别指向数组的开始和结尾，然后不断向中间夹逼。

## Solution

```java
import java.util.ArrayList;

public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int[] nums, int sum) {
        int n = nums.length;
        ArrayList<Integer> result = new ArrayList<>();
        if (n < 2) return result;
        
        int i=0, j=n-1;
        while (i < j) {
            int s = nums[i] + nums[j];
            if (s == sum) {
                result.add(nums[i]);
                result.add(nums[j]);
                return result;
            } else if (s < sum) {
                i++;
            } else {
                j--;
            }
        }
        return result;
    }
}
```

