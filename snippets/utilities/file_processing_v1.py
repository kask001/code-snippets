#!/usr/bin/env python3
"""
文件处理工具函数

常用的文件操作封装：读写、搜索、批量重命名等。
"""

import os
from pathlib import Path
from typing import List, Optional


def read_file_safe(filepath: str, encoding: str = "utf-8") -> Optional[str]:
    """
    安全读取文件内容。

    Args:
        filepath: 文件路径
        encoding: 文件编码

    Returns:
        文件内容字符串，失败返回 None
    """
    try:
        with open(filepath, "r", encoding=encoding) as f:
            return f.read()
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"读取文件失败 [{filepath}]: {e}")
        return None


def write_file_safe(filepath: str, content: str, encoding: str = "utf-8") -> bool:
    """
    安全写入文件，自动创建目录。

    Args:
        filepath: 文件路径
        content: 写入内容
        encoding: 文件编码

    Returns:
        是否成功
    """
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding=encoding) as f:
            f.write(content)
        return True
    except (PermissionError, OSError) as e:
        print(f"写入文件失败 [{filepath}]: {e}")
        return False


def search_files(directory: str, extension: str = ".py") -> List[str]:
    """
    递归搜索指定扩展名的文件。

    Args:
        directory: 搜索目录
        extension: 文件扩展名（如 ".py"、".txt"）

    Returns:
        匹配的文件路径列表
    """
    result = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                result.append(os.path.join(root, filename))
    return result


def count_lines(filepath: str) -> Dict[str, int]:
    """
    统计文件的行数（总行、代码行、空行、注释行）。

    Args:
        filepath: 文件路径

    Returns:
        包含各类行数统计的字典
    """
    content = read_file_safe(filepath)
    if content is None:
        return {"total": 0, "code": 0, "blank": 0, "comment": 0}

    lines = content.splitlines()
    total = len(lines)
    blank = sum(1 for line in lines if not line.strip())
    comment = sum(1 for line in lines if line.strip().startswith("#"))
    code = total - blank - comment

    return {"total": total, "code": code, "blank": blank, "comment": comment}


if __name__ == "__main__":
    import tempfile

    # 测试文件写入和读取
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w") as f:
        temp_path = f.name
        f.write("# 示例文件\n")
        f.write("\n")
        f.write("print('hello world')\n")
        f.write("# 这是注释\n")

    content = read_file_safe(temp_path)
    print(f"文件内容:\n{content}")

    stats = count_lines(temp_path)
    print(f"行数统计: {stats}")

    os.unlink(temp_path)
