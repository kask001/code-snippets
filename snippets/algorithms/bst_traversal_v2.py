#!/usr/bin/env python3
"""
二叉搜索树 - 层序遍历 (BFS)

使用队列实现二叉树的逐层遍历（广度优先搜索），
输出结果按层级分组。
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    层序遍历二叉树，返回按层级分组的列表。

    Args:
        root: 二叉树根节点

    Returns:
        每层节点值组成的列表
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


if __name__ == "__main__":
    # 构建二叉树:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    for i, level in enumerate(level_order(root)):
        print(f"第 {i + 1} 层: {level}")
