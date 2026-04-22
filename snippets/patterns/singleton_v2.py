#!/usr/bin/env python3
"""
单例模式 - 线程安全实现

展示在多线程环境下保证单例的正确实现。
"""

import threading
import time


class ThreadSafeSingleton:
    """线程安全的单例类，使用双重检查锁定。"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # 第一次检查（无锁，快速路径）
        if cls._instance is None:
            # 加锁
            with cls._lock:
                # 第二次检查（有锁，确保只创建一次）
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._value = 0
            self._initialized = True
            print("单例实例已创建")

    def increment(self):
        self._value += 1
        return self._value


def worker():
    """工作线程函数。"""
    singleton = ThreadSafeSingleton()
    value = singleton.increment()
    print(f"线程 {threading.current_thread().name}: value = {value}")


if __name__ == "__main__":
    # 验证多线程下的单例行为
    threads = [threading.Thread(target=worker, name=f"T{i}") for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    s1 = ThreadSafeSingleton()
    s2 = ThreadSafeSingleton()
    print(f"\n是否同一实例: {s1 is s2}")
    print(f"最终值: {s1._value}")
