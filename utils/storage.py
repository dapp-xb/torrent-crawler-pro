#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据存储模块
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
from config.settings import Config


class StorageManager:
    """管理爬虫数据存储"""
    
    @staticmethod
    def save_json(data: List[Dict], filename: Optional[str] = None) -> str:
        """保存为 JSON 文件"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"torrents_{timestamp}.json"
        
        filepath = Path(Config.OUTPUT_DIR) / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return str(filepath)
    
    @staticmethod
    def save_csv(data: List[Dict], filename: Optional[str] = None) -> str:
        """保存为 CSV 文件"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"torrents_{timestamp}.csv"
        
        if not data:
            return ""
        
        filepath = Path(Config.OUTPUT_DIR) / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        keys = data[0].keys()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        return str(filepath)
    
    @staticmethod
    def save(data: List[Dict], filename: Optional[str] = None, fmt: str = "json") -> str:
        """自动选择格式保存"""
        if fmt == "csv":
            return StorageManager.save_csv(data, filename)
        else:
            return StorageManager.save_json(data, filename)
    
    @staticmethod
    def load_json(filepath: str) -> List[Dict]:
        """加载 JSON 文件"""
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    
    @staticmethod
    def append_json(data: List[Dict], filepath: str):
        """追加到 JSON 文件"""
        existing = []
        if Path(filepath).exists():
            existing = StorageManager.load_json(filepath)
        
        existing.extend(data)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
