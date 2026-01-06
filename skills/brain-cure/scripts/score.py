#!/usr/bin/env python3
"""
BrainCure - Score Calculator

점수 체계:
    base 1점 + pillars (0-9) = 최대 10점
    Butler Mode면 base 0점 → 최대 9점

사용법:
    python score.py evaluate --type request --p1 2 --p2 3 --p3 1
    python score.py evaluate --type request --p1 3 --p2 3 --p3 3 --butler
    python score.py average /path/to/prompt_scores.json
    python score.py add /path/to/prompt_scores.json 7
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

# 점수별 별명
SCORE_TITLES = {
    0: ("🙏", "Hail Mary"),
    1: ("🎰", "Slot Machine"),
    2: ("😶‍🌫️", "Foggy"),
    3: ("🚶", "Wandering"),
    4: ("🤔", "Getting There"),
    5: ("🧭", "On Track"),
    6: ("🎯", "Focused"),
    7: ("🧠", "Sharp"),
    8: ("🦾", "Commander"),
    9: ("💎", "Flawless"),
    10: ("🦸", "Tony Stark"),
}

# Hail Mary 패턴별 점수 상한
PATTERN_CAPS = {
    "hail_mary": 2,
    "just_do_it": 1,
    "why_no_context": 1,
    "copy_paste_loop": 1,
    "none": 10
}

def calculate_score(p1: int, p2: int, p3: int, pattern: str = "none", butler: bool = False) -> dict:
    """
    점수 계산.
    
    base 1점 + pillars (0-9) = 최대 10점
    Butler Mode면 base 0점
    """
    # base 점수
    base = 0 if butler else 1
    
    # pillars 합산
    pillars = p1 + p2 + p3
    
    # 총점
    score = base + pillars
    
    # 패턴 상한 적용
    cap = PATTERN_CAPS.get(pattern, 10)
    score = min(score, cap)
    
    return {
        "base": base,
        "pillars": pillars,
        "total": score
    }

def get_title(score: int) -> tuple[str, str]:
    """점수에 해당하는 별명 반환."""
    return SCORE_TITLES.get(score, ("❓", "Unknown"))

def get_weakest_pillar(pillars: dict, prompt_type: str) -> tuple[str, str, int]:
    """가장 약한 pillar 반환."""
    if prompt_type == "request":
        names = ["origin", "destination", "boundary"]
        labels = ["출발점", "목적지", "경계"]
    else:
        names = ["hypothesis", "scope", "context"]
        labels = ["가설", "범위", "맥락"]
    
    scores = [pillars.get("p1", 0), pillars.get("p2", 0), pillars.get("p3", 0)]
    min_idx = scores.index(min(scores))
    
    return names[min_idx], labels[min_idx], scores[min_idx]

def load_scores(filepath: str) -> dict:
    """점수 파일 로드."""
    path = Path(filepath)
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"scores": [], "average": 0.0}

def save_scores(filepath: str, data: dict):
    """점수 파일 저장."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_score(filepath: str, score: int) -> dict:
    """새 점수 추가하고 평균 재계산."""
    data = load_scores(filepath)
    data["scores"].append({
        "value": score,
        "timestamp": datetime.now().isoformat()
    })
    
    values = [s["value"] for s in data["scores"]]
    data["average"] = round(sum(values) / len(values), 1)
    
    if len(values) >= 3:
        recent = values[-5:]
        if len(recent) >= 2:
            if recent[-1] > recent[0]:
                data["trend"] = "improving"
            elif recent[-1] < recent[0]:
                data["trend"] = "declining"
            else:
                data["trend"] = "stable"
    
    save_scores(filepath, data)
    return data

def main():
    parser = argparse.ArgumentParser(description="BrainCure Score Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # evaluate 커맨드
    eval_parser = subparsers.add_parser("evaluate", help="프롬프트 점수 계산")
    eval_parser.add_argument("--type", choices=["request", "question"], required=True)
    eval_parser.add_argument("--p1", type=int, required=True, help="Pillar 1 점수 (0-3)")
    eval_parser.add_argument("--p2", type=int, required=True, help="Pillar 2 점수 (0-3)")
    eval_parser.add_argument("--p3", type=int, required=True, help="Pillar 3 점수 (0-3)")
    eval_parser.add_argument("--pattern", default="none", help="감지된 안티패턴")
    eval_parser.add_argument("--butler", action="store_true", help="Butler Mode 감지")
    
    # average 커맨드
    avg_parser = subparsers.add_parser("average", help="세션 평균 조회")
    avg_parser.add_argument("filepath", help="점수 파일 경로")
    
    # add 커맨드
    add_parser = subparsers.add_parser("add", help="점수 추가")
    add_parser.add_argument("filepath", help="점수 파일 경로")
    add_parser.add_argument("score", type=int, help="추가할 점수")
    
    args = parser.parse_args()
    
    if args.command == "evaluate":
        result = calculate_score(args.p1, args.p2, args.p3, args.pattern, args.butler)
        pillars = {"p1": args.p1, "p2": args.p2, "p3": args.p3}
        weakest_key, weakest_label, weakest_score = get_weakest_pillar(pillars, args.type)
        emoji, title = get_title(result["total"])
        
        print(json.dumps({
            "score": result["total"],
            "max_score": 10,
            "breakdown": {
                "base": result["base"],
                "pillars": result["pillars"]
            },
            "emoji": emoji,
            "title": title,
            "pillar_scores": {
                "p1": args.p1,
                "p2": args.p2,
                "p3": args.p3
            },
            "weakest": {
                "key": weakest_key,
                "label": weakest_label,
                "score": weakest_score
            },
            "butler_mode": args.butler,
            "pattern": args.pattern if args.pattern != "none" else None
        }, ensure_ascii=False))
        
    elif args.command == "average":
        data = load_scores(args.filepath)
        print(json.dumps({
            "average": data.get("average", 0),
            "count": len(data.get("scores", [])),
            "trend": data.get("trend", "unknown")
        }, ensure_ascii=False))
        
    elif args.command == "add":
        data = add_score(args.filepath, args.score)
        print(json.dumps({
            "added": args.score,
            "new_average": data["average"],
            "total_count": len(data["scores"]),
            "trend": data.get("trend", "unknown")
        }, ensure_ascii=False))

if __name__ == "__main__":
    main()
