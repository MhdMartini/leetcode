# 581. Shortest Unsorted Continuous Subarray

Given an integer array <code>nums</code>, you need to find one **continuous subarray** that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Notice that the solution set must not contain duplicate triplets.

## Example 1

<pre>
<b>Input:</b> nums = [2,6,4,8,10,9,15]
<b>Output:</b> 5
<b>Explanation:</b> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

## Example 2

<pre>
<b>Input:</b> nums = [1,2,3,4]
<b>Output:</b> 0
</pre>

## Example 3

<pre>
<b>Input:</b> nums = [1]
<b>Output:</b> 0
</pre>

## Constraints

- <code> 0 <= nums.length <= 10<sup>4</sup> </code>
- <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>
