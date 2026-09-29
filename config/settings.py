#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理模块
"""

import os
import json
from pathlib import Path
from typing import Dict, Any

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 数据存储目录
DATA_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"
DB_DIR = BASE_DIR / "database"

# 创建必要目录
for dir_path in [DATA_DIR, LOG_DIR, DB_DIR]:
    dir_path.mkdir(exist_ok=True)

class Config:
    """爬虫基础配置"""
    
    # 网络配置
    REQUEST_TIMEOUT = 20
    REQUEST_RETRY = 3
    RETRY_DELAY = 2
    
    # 多线程配置
    MAX_WORKERS = 5  # 最大并发线程数
    TASK_QUEUE_SIZE = 100
    
    # 爬虫配置
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
    }
    
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15",
    ]
    
    # 代理配置（可选）
    USE_PROXY = False
    PROXY_URL = "http://127.0.0.1:7890"
    
    # 存储配置
    OUTPUT_FORMAT = "json"  # json 或 csv
    OUTPUT_DIR = str(DATA_DIR)
    
    # 定时任务配置
    SCHEDULER_ENABLED = True
    SCHEDULER_INTERVAL = 3600  # 秒（1小时）
    
    # 日志配置
    LOG_LEVEL = "INFO"
    LOG_DIR = str(LOG_DIR)
    
    # 搜索关键词（示例）
    DEFAULT_KEYWORDS = [
        "4K",
        "1080p",
        "720p",
    ]
    
    @classmethod
    def load_from_file(cls, config_file: str) -> "Config":
        """从文件加载配置"""
        if os.path.exists(config_file):
            with open(config_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    if hasattr(cls, key):
                        setattr(cls, key, value)
        return cls
    
    @classmethod
    def save_to_file(cls, config_file: str):
        """保存配置到文件"""
        config_data = {
            k: v for k, v in vars(cls).items()
            if not k.startswith("_") and isinstance(v, (str, int, bool, list, dict))
        }
        os.makedirs(os.path.dirname(config_file) or ".", exist_ok=True)
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print(f"Base Dir: {BASE_DIR}")
    print(f"Data Dir: {DATA_DIR}")
    print(f"Max Workers: {Config.MAX_WORKERS}")
