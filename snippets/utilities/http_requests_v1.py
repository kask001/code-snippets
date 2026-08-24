#!/usr/bin/env python3
"""
HTTP 请求工具函数

封装常用的 HTTP 请求操作，包括 GET、POST、错误处理、重试机制。
使用 requests 库（需要安装: pip install requests）。
"""

import time
from typing import Optional, Dict, Any


class HttpClient:
    """简单的 HTTP 客户端封装。"""

    def __init__(self, base_url: str = "", timeout: int = 10, max_retries: int = 3):
        """
        初始化 HTTP 客户端。

        Args:
            base_url: 基础 URL
            timeout: 请求超时时间（秒）
            max_retries: 最大重试次数
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def get(self, path: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        发送 GET 请求。

        Args:
            path: 请求路径
            params: 查询参数

        Returns:
            包含 status、data、headers 的字典
        """
        import requests

        url = f"{self.base_url}/{path.lstrip('/')}" if self.base_url else path
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return {
                    "status": response.status_code,
                    "data": response.json(),
                    "headers": dict(response.headers),
                }
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries:
                    return {"status": 0, "error": str(e), "data": None}
                time.sleep(attempt)

        return {"status": 0, "error": "max retries exceeded", "data": None}


def fetch_json_placeholder() -> None:
    """示例：从 JSONPlaceholder API 获取数据。"""
    import requests

    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
        resp.raise_for_status()
        user = resp.json()
        print(f"用户: {user['name']} ({user['email']})")
        print(f"公司: {user['company']['name']}")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


if __name__ == "__main__":
    fetch_json_placeholder()

    client = HttpClient(base_url="https://jsonplaceholder.typicode.com")
    posts = client.get("/posts", params={"_limit": 3})
    if posts["data"]:
        for post in posts["data"]:
            print(f"\n标题: {post['title'][:50]}...")
    else:
        print(f"请求失败: {posts.get('error')}")
