from timeit import timeit
from typing import List, Optional
from numpy import inf
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.__repr__()


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        ret = True
        for l in lists:
            if l is not None:
                ret = False
                break
        if ret:
            return None

        head = ListNode(0)
        curr_node = head

        while True:
            min_ = inf
            min_idx = 0
            for idx, l in enumerate(lists):
                if l is None:
                    continue
                if l.val < min_:
                    min_ = l.val
                    min_idx = idx
                    pass
            if min_ == inf:
                return head.next

            curr_node.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            curr_node = curr_node.next

    def mergeKLists_v2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists(lists)


def print_list(l: Optional[ListNode]):
    while l:
        print(l.val, end=" ")
        l = l.next
    print()


def main():
    ln = [ListNode(1, ListNode(4,  ListNode(5))), ListNode(
        1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    t1 = timeit(lambda: Solution().mergeKLists(
        copy.deepcopy(ln)), number=10000)
    t2 = timeit(lambda: Solution().mergeKLists_v2(
        copy.deepcopy(ln)), number=10000)
    print("v1:", t1)
    print("v2:", t2)

    sln = Solution().mergeKLists(ln.copy())
    print_list(sln)


if __name__ == "__main__":
    main()
