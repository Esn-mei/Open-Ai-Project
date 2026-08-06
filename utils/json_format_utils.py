# utils/json_format_utils.py

"""
JSON 格式化工具模块

提供统一的 JSON 序列化和格式化功能，确保项目中 JSON 输出的一致性
"""

import json
from typing import Any, Dict
from bson import ObjectId

class CustomJSONEncoder(json.JSONEncoder):
    """
    自定义 JSON 编码器，支持 MongoDB ObjectId 等特殊类型
    """
    def default(self, obj: Any) -> Any:
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

def format_json(data: Any, indent: int = 4, ensure_ascii: bool = False) -> str:
    return json.dumps(data, indent=indent, ensure_ascii=ensure_ascii, cls=CustomJSONEncoder)