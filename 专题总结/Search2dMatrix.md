# 1. LeetCode 74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

**Example 2:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

## Idea

If we "serialize" this 2-D matrix (`m` rows and `n` columns) into an 1-D array, then the array is still sorted. And the $i^{th}$ element in the 1-D array corresponding to `matrix[i/n][i%n]`. Then we can use binary search as usual.

## Solution

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;
        if (n == 0) return false;
        
        int low=0, high=m*n-1;
        while (low <= high) {
            int mid = (low + high) / 2;
            int midVal = matrix[mid/n][mid%n];
            
            if (midVal == target) return true;
            if (midVal < target) low = mid+1;
            else high = mid-1;
        }
        return false;
    }
}
```

# 2. LeetCode 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example:**

Consider the following matrix:

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given target = `5`, return `true`.

Given target = `20`, return `false`.

## Idea

One way of doing this is to run binary search for each row, and the running time is $O(m*logn)$.

A better way is to start from bottom-left (or top-right) corner, and for each step when we compare current number to the target, we can make two choices: 1⃣️move to a smaller number, 2⃣️move to a larger number. When running the binary search algorithm, we should always move toward target, of course.

> The reason why we can start from top-left corner or bottom-right corner is because that way we can only make one choice. Starting from top-left corner can only move to larger numbers and bottom-right corner smaller numbers.

## Solution

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;
        if (n == 0) return false;
        
        // start from top-right
        int i=0, j=n-1;
        while (i<m && j>=0) {
            if (matrix[i][j] == target) return true;
            if (matrix[i][j] < target) i++;
            else j--;
        }
        return false;
    }
}
```

