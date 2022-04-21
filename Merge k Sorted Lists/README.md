# Merge k Sorted Lists

You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

## Example 1

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

## Example 2

    Input: lists = []
    Output: []

## Example 3

    Input: lists = [[]]
    Output: []

## Constraints

- <code> k == lists.length </code>

- <code> 0 <= k <= 10<sup>4</sup> </code>

- <code> 0 <= lists[i].length <= 500 </code>

- <code> -10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup> </code>

- <code> lists[i] </code>
is sorted in <strong>ascending order.</strong>

- The sum of
<code> lists[i].length </code>
will not exceed
<code> 10<sup>4</sup> </code>
