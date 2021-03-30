# MergeSort

- 写法一

```java
import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {
        int[] nums = {3, 1, 5, 9, 7, 6, 2};
        mergeSort(nums);
        System.out.println(Arrays.toString(nums));
    }

    static void mergeSort(int[] nums) {
        int[] workspace = new int[nums.length];
        mergeSort(nums, workspace, 0, nums.length-1);
    }

    private static void mergeSort(int[] nums, int[] workspace, int low, int high) {
        if (low >= high) return;

        int mid = (low + high) / 2;
        mergeSort(nums, workspace, low, mid);
        mergeSort(nums, workspace, mid+1, high);
        merge(nums, workspace, low, mid, high);
    }

    private static void merge(int[] nums, int[] workspace, int low, int mid, int high) {
        int index = low;        // workspace index
        int i = low;
        int j = mid+1;

        while (i <= mid && j <= high) {
            workspace[index++] = (nums[i] <= nums[j])? nums[i++] : nums[j++];
        }
        while (i <= mid) workspace[index++] = nums[i++];
        while (j <= high) workspace[index++] = nums[j++];

        // copy back
        for (int k=low; k<=high; k++) {
            nums[k] = workspace[k];
        }
    }
}
```

- 写法二

```java
import java.util.Arrays;

public class MergeSort2 {

    public static void main(String[] args) {
        int[] nums = {3, 1, 5, 9, 7, 6, 2};
        mergeSort(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }

    static void mergeSort(int[] nums, int low, int high) {
        if (low >= high) return;

        int mid = (low + high) / 2;
        mergeSort(nums, low, mid);
        mergeSort(nums, mid+1, high);
        merge(nums, low, mid, high);
    }

    private static void merge(int[] nums, int low, int mid, int high) {
        int[] tmp = new int[high-low+1];
        int i=low, j=mid+1, index=0;

        while (i <= mid || j <= high) {
            // 只有在这些情况下才有可能取j指向的数
            if (i > mid || (j <= high && nums[j] < nums[i])) {
                tmp[index++] = nums[j++];
            } else {
                tmp[index++] = nums[i++];
            }
        }

        // copy back
        index = 0;
        for (i=low; i<=high; i++) {
            nums[i] = tmp[index++];
        }
    }
}
```

