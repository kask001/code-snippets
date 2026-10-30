#!/usr/bin/env python3
"""
动态规划 - 斐波那契数列与爬楼梯 (Dynamic Programming)

展示动态规划的核心思想：将大问题分解为子问题，
存储子问题的解以避免重复计算（记忆化）。
"""

from functools import lru_cache
from typing import Dict


# 方法 1: 记忆化递归
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """使用记忆化的斐波那契。"""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# 方法 2: 自底向上的动态规划
def fib_dp(n: int) -> int:
    """使用 DP 数组的斐波那契。"""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 方法 3: 空间优化的 DP
def fib_optimized(n: int) -> int:
    """空间优化为 O(1) 的斐波那契。"""
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# 经典问题: 爬楼梯
def climb_stairs(n: int) -> int:
    """
    爬楼梯问题：每次可以爬 1 或 2 级台阶，求到达第 n 级的方法数。
    本质就是斐波那契数列。
    """
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fib_memo(i)} (memo) | {fib_dp(i)} (dp) | {fib_optimized(i)} (opt)")

    print(f"\n爬楼梯 (5级): {climb_stairs(5)} 种方法")
    print(f"爬楼梯 (10级): {climb_stairs(10)} 种方法")
