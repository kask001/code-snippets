#!/usr/bin/env python3
"""
列表推导式与生成器表达式 (List Comprehension & Generator Expression)

Python 中简洁而强大的数据转换语法，
用于从已有数据创建新的列表、字典、集合。
"""

from typing import List, Dict


def flat_matrix(matrix: List[List[int]]) -> List[int]:
    """使用列表推导式展平二维列表。"""
    return [item for row in matrix for item in row]


def dict_invert(d: Dict[str, int]) -> Dict[int, str]:
    """字典键值反转。"""
    return {v: k for k, v in d.items()}


def sieve_of_eratosthenes(n: int) -> List[int]:
    """埃拉托斯特尼筛法，找出 n 以内的所有素数。"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def word_frequency(text: str) -> Dict[str, int]:
    """统计文本中每个单词的出现频率。"""
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"展平矩阵: {flat_matrix(matrix)}")

    original = {"a": 1, "b": 2, "c": 3}
    print(f"字典反转: {dict_invert(original)}")

    print(f"20以内素数: {sieve_of_eratosthenes(20)}")

    text = "the quick brown fox jumps over the lazy dog"
    print(f"词频统计: {word_frequency(text)}")
