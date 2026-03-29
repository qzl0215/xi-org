#!/usr/bin/env python3
"""
溪系统 Token 统计脚本
自动从 OpenClaw session 日志中提取 token 使用量
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# 配置
SESSIONS_DIR = Path.home() / ".qclaw" / "agents" / "main" / "sessions"
OUTPUT_FILE = Path.home() / "srv" / "xi" / "shared" / "reports" / "token-usage.json"

def extract_tokens_from_session(session_file):
    """从单个 session 文件提取 token 信息"""
    tokens = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0, "totalTokens": 0, "turns": 0}
    
    try:
        with open(session_file, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                    # OpenClaw 的 token 记录格式
                    if "message" in entry and isinstance(entry["message"], dict):
                        msg = entry["message"]
                        if "usage" in msg:
                            u = msg["usage"]
                            tokens["input"] += u.get("input", 0)
                            tokens["output"] += u.get("output", 0)
                            tokens["cacheRead"] += u.get("cacheRead", 0)
                            tokens["cacheWrite"] += u.get("cacheWrite", 0)
                            tokens["totalTokens"] += u.get("totalTokens", 0)
                            tokens["turns"] += 1
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        pass
    
    return tokens

def get_all_sessions():
    """获取所有 session 文件"""
    sessions = []
    if SESSIONS_DIR.exists():
        for f in SESSIONS_DIR.iterdir():
            if f.suffix == ".jsonl":
                sessions.append(f)
    return sessions

def aggregate_by_date(sessions):
    """按日期聚合 token 使用量"""
    by_date = defaultdict(lambda: {
        "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0, 
        "totalTokens": 0, "turns": 0, "sessions": 0
    })
    
    for session_file in sessions:
        mtime = datetime.fromtimestamp(session_file.stat().st_mtime)
        date_str = mtime.strftime("%Y-%m-%d")
        
        tokens = extract_tokens_from_session(session_file)
        for key in ["input", "output", "cacheRead", "cacheWrite", "totalTokens", "turns"]:
            by_date[date_str][key] += tokens[key]
        by_date[date_str]["sessions"] += 1
    
    return dict(by_date)

def main():
    sessions = get_all_sessions()
    by_date = aggregate_by_date(sessions)
    
    # 计算总计
    total = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0, "totalTokens": 0, "turns": 0, "sessions": 0}
    for date_data in by_date.values():
        for key in ["input", "output", "cacheRead", "cacheWrite", "totalTokens", "turns", "sessions"]:
            total[key] += date_data.get(key, 0)
    
    result = {
        "generated_at": datetime.now().isoformat(),
        "total": total,
        "by_date": by_date
    }
    
    # 写入输出文件
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    # 打印摘要
    print(f"Token 统计完成:")
    print(f"  输入: {total['input']:,} tokens")
    print(f"  输出: {total['output']:,} tokens")
    print(f"  缓存读取: {total['cacheRead']:,} tokens")
    print(f"  缓存写入: {total['cacheWrite']:,} tokens")
    print(f"  总计: {total['totalTokens']:,} tokens")
    print(f"  对话轮次: {total['turns']}")
    print(f"  Sessions: {total['sessions']}")
    print(f"  输出文件: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()