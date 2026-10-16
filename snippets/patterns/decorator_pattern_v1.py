#!/usr/bin/env python3
"""
装饰器模式 (Decorator Pattern)

动态地给对象添加额外的职责，比生成子类更加灵活。

示例：为文本处理添加各种装饰功能（加密、压缩、日志）。
"""

from abc import ABC, abstractmethod


# 组件接口
class TextProcessor(ABC):
    """文本处理器接口。"""

    @abstractmethod
    def process(self, text: str) -> str:
        pass


# 具体组件
class PlainTextProcessor(TextProcessor):
    """纯文本处理器。"""

    def process(self, text: str) -> str:
        return text


# 装饰器基类
class TextDecorator(TextProcessor):
    """文本装饰器基类。"""

    def __init__(self, wrapped: TextProcessor):
        self._wrapped = wrapped

    def process(self, text: str) -> str:
        return self._wrapped.process(text)


# 具体装饰器
class UpperCaseDecorator(TextDecorator):
    """转大写装饰器。"""

    def process(self, text: str) -> str:
        return super().process(text).upper()


class ReverseDecorator(TextDecorator):
    """反转文本装饰器。"""

    def process(self, text: str) -> str:
        return super().process(text)[::-1]


class TrimDecorator(TextDecorator):
    """去除多余空格装饰器。"""

    def process(self, text: str) -> str:
        return " ".join(super().process(text).split())


if __name__ == "__main__":
    # 基础处理器
    processor = PlainTextProcessor()
    print(f"原始: '{processor.process('  hello  world  ')}'")

    # 添加装饰器（可以任意组合）
    processor = UpperCaseDecorator(processor)
    print(f"大写: '{processor.process('  hello  world  ')}'")

    processor = TrimDecorator(processor)
    print(f"大写+去空格: '{processor.process('  hello  world  ')}'")

    processor = ReverseDecorator(processor)
    print(f"大写+去空格+反转: '{processor.process('  hello  world  ')}'")
