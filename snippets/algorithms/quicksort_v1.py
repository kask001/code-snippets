#!/usr/bin/env python3
"""
快速排序 (Quick Sort)

分治法排序算法，选择一个基准值(pivot)将数组分为两部分，
分别对两部分递归排序。平均时间复杂度: O(n log n)。
"""

from typing import List


def quicksort(arr: List[int]) -> List[int]:
    """
    实现快速排序。

    Args:
        arr: 待排序的列表

    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr

    # 选择中间元素作为基准值
    pivot = arr[len(arr) // 2]

    # 三路划分
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    print(f"排序前: {data}")
    print(f"排序后: {quicksort(data)}")
    print(f"空列表: {quicksort([])}")
    print(f"单元素: {quicksort([42])}")
    print(f"逆序: {quicksort([5, 4, 3, 2, 1])}")
