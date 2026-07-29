#!/usr/bin/env python3
"""
Python dataclass (数据类)

dataclass 是 Python 3.7+ 引入的装饰器，自动生成
__init__、__repr__、__eq__ 等特殊方法，
减少样板代码，专注于数据建模。
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class Address:
    """地址数据类。"""
    city: str
    street: str
    zip_code: str

    def full_address(self) -> str:
        return f"{self.street}, {self.city} {self.zip_code}"


@dataclass(order=True)
class Student:
    """学生数据类，支持排序（按 gpa 降序）。"""
    gpa: float
    name: str
    age: int
    courses: List[str] = field(default_factory=list)
    address: Optional[Address] = None

    def add_course(self, course: str):
        self.courses.append(course)

    def summary(self) -> str:
        addr = self.address.full_address() if self.address else "未设置"
        return (
            f"{self.name} (GPA: {self.gpa})\n"
            f"年龄: {self.age}, 地址: {addr}\n"
            f"课程: {', '.join(self.courses)}"
        )


@dataclass
class BlogPost:
    """博客文章数据类，带默认值和验证。"""
    title: str
    content: str
    author: str = "匿名"
    tags: List[str] = field(default_factory=lambda: ["未分类"])
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

    def __post_init__(self):
        """初始化后的自动验证。"""
        if len(self.title) > 100:
            raise ValueError("标题不能超过100个字符")
        if not self.content.strip():
            raise ValueError("内容不能为空")

    def tag_string(self) -> str:
        return ", ".join(f"#{tag}" for tag in self.tags)


if __name__ == "__main__":
    addr = Address(city="北京", street="长安街1号", zip_code="100000")
    s1 = Student(gpa=3.8, name="Alice", age=20, address=addr)
    s1.add_course("Python")
    s1.add_course("数据结构")
    print(s1.summary())

    s2 = Student(gpa=3.9, name="Bob", age=21)
    s2.add_course("算法")
    print(f"\n按 GPA 排序: {sorted([s1, s2], reverse=True)}")

    post = BlogPost(title="学习 dataclass", content="dataclass 真好用!", tags=["Python", "学习"])
    print(f"\n{post.title} | {post.tag_string()} | {post.created_at}")
