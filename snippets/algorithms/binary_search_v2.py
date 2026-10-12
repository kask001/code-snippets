#!/usr/bin/env python3
"""
二分查找 - 左边界查找

查找目标值第一次出现的位置（左边界），
适用于数组中有重复元素的场景。
"""

from typing import List


def binary_search_left(arr: List[int], target: int) -> int:
    """
    查找目标值第一次出现的索引。

    Args:
        arr: 已排序的数组（升序，可含重复）
        target: 目标值

    Returns:
        第一次出现的索引，未找到返回 -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(arr) and arr[left] == target:
        return left
    return -1


if __name__ == "__main__":
    data = [1, 2, 2, 2, 3, 4, 5, 5, 6]
    print(f"数组: {data}")
    print(f"查找 2 的左边界: {binary_search_left(data, 2)}")
    print(f"查找 5 的左边界: {binary_search_left(data, 5)}")
    print(f"查找 7: {binary_search_left(data, 7)}")
