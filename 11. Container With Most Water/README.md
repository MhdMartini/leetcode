# 11. Container With Most Water

You are given an integer array height of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.

## Example 1

![](question_11.jpg)

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

## Example 2

    Input: height = [1,1]
    Output: 1

## Constraints

- <code> n == height.length </code>
- <code> 2 <= n <= 10<sup>5</sup> </code>
- <code> 0 <= height[i] <= 10<sup>4</sup> </code>
