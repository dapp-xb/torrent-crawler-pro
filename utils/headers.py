#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTTP 请求头管理
"""

import random
from typing import Dict
from config.settings import Config


class HeaderManager:
    """管理 HTTP 请求头"""
    
    @staticmethod
    def get_random_headers() -> Dict[str, str]:
        """获取随机 User-Agent 的请求头"""
        headers = Config.HEADERS.copy()
        headers["User-Agent"] = random.choice(Config.USER_AGENTS)
        return headers
    
    @staticmethod
    def get_mobile_headers() -> Dict[str, str]:
        """获取移动端请求头"""
        headers = Config.HEADERS.copy()
        headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15"
        return headers
    
    @staticmethod
    def get_desktop_headers() -> Dict[str, str]:
        """获取桌面端请求头"""
        headers = Config.HEADERS.copy()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        return headers
