# 和为S的连续正数序列

输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序。例如：18,19,20,21,22是和为100的一组连续正整数。

## Solution

- 方法一：Bruteforce ($O(n^2)$)

```java
import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        // try all possible [i, j]
        for (int i=1; i<sum; i++) {
            for (int j=i+1; j<sum; j++) {
                int s = (j-i+1)*(i+j)/2;
                if (s == sum) {
                    ArrayList<Integer> list = new ArrayList<>();
                    for (int k=i; k<=j; k++) {
                        list.add(k);
                    }
                    result.add(list);
                }
            }
        }
        return result;
    }
}
```

- 方法二：Sliding Window ($O(n)$)

```java
import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        
        // Allowed operations:
        // * i move right (shrink the window)
        // * j move right (extend the window)
        int i=1, j=2;
        while (i < j) {
            int s = (j-i+1)*(i+j)/2;
            if (s == sum) {
                ArrayList<Integer> list = new ArrayList<>();
                for (int k=i; k<=j; k++) {
                    list.add(k);
                }
                result.add(list);
                i++;
            } else if (s < sum) {
                j++;
            } else {
                i++;
            }
        }
        
        return result;
    }
}
```

> ⚠️注意当 s==sum 时，记得i++