# 15. 3Sum

Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.

Notice that the solution set must not contain duplicate triplets.

## Example 1

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

## Example 2

    Input: num = []
    Output: []

## Example 3

    Input: num = [0]
    Output: []

## Constraints

- <code> 0 <= nums.length <= 3000 </code>
- <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>
