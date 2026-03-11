#!/usr/bin/env python3
"""
考公错题本 - 轻量级错题管理工具
🦐 养虾哥专属

用法:
    python exam_book.py add "题目" "答案" --subject 知识点 --explain 解析
    python exam_book.py paper --count 10
    python exam_book.py random --count 5
    python exam_book.py wrong
    python exam_book.py stats
"""

import json
import os
import random
import uuid
import argparse
from datetime import datetime

# 数据文件路径
DATA_FILE = os.path.expanduser("~/.openclaw/workspace/exam-errors/book.json")


def load():
    """加载数据"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        return {"questions": [], "wrong_book": [], "stats": {"total": 0}}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(data):
    """保存数据"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_question(question, answer, subject="未分类", explain=""):
    """添加错题"""
    data = load()
    q = {
        "id": str(uuid.uuid4())[:8],
        "question": question,
        "answer": answer,
        "subject": subject,
        "explain": explain,
        "created": datetime.now().strftime("%Y-%m-%d"),
    }
    data["questions"].append(q)
    data["stats"]["total"] = len(data["questions"])
    save(data)
    return q


def random_questions(count=5, subject=None):
    """随机抽题"""
    data = load()
    qs = data["questions"]
    if subject:
        qs = [q for q in qs if subject in q["subject"]]
    if not qs:
        return []
    return random.sample(qs, min(count, len(qs)))


def generate_paper(count=10, subject=None):
    """生成试卷"""
    qs = random_questions(count, subject)
    return {
        "title": "考公错题练习卷",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": len(qs),
        "questions": qs,
    }


def add_to_wrong(q_id):
    """加入错题本"""
    data = load()
    if q_id not in data["wrong_book"]:
        data["wrong_book"].append(q_id)
        save(data)


def get_wrong_book():
    """获取错题本"""
    data = load()
    return [q for q in data["questions"] if q["id"] in data["wrong_book"]]


def stats():
    """统计"""
    data = load()
    by_subject = {}
    for q in data["questions"]:
        subj = q["subject"]
        by_subject[subj] = by_subject.get(subj, 0) + 1
    return {
        "total": len(data["questions"]),
        "wrong": len(data["wrong_book"]),
        "by_subject": by_subject,
    }


def format_paper(paper, answers=False):
    """格式化试卷"""
    lines = [
        f"📄 {paper['title']} ({paper['date']}) - {paper['count']}题",
        "═" * 50,
    ]
    for i, q in enumerate(paper["questions"], 1):
        lines.append(f"{i}. {q['question']} [{q['subject']}]")
    if answers:
        lines.append("═" * 50)
        lines.append("答案:")
        for i, q in enumerate(paper["questions"], 1):
            lines.append(f"  {i}. {q['answer']}")
    return "\n".join(lines)


def format_questions(qs):
    """格式化题目列表"""
    lines = []
    for q in qs:
        lines.append(f"📝 {q['question']} [{q['subject']}]")
        lines.append(f"   答案：{q['answer']}")
        if q.get("explain"):
            lines.append(f"   解析：{q['explain']}")
        lines.append("")
    return "\n".join(lines)


# 命令行
def main():
    parser = argparse.ArgumentParser(description="考公错题本")
    sub = parser.add_subparsers(dest="cmd")

    # add
    p_add = sub.add_parser("add", help="添加错题")
    p_add.add_argument("question", help="题目内容")
    p_add.add_argument("answer", help="答案")
    p_add.add_argument("--subject", "-s", default="未分类", help="知识点")
    p_add.add_argument("--explain", "-e", default="", help="解析")

    # paper
    p_paper = sub.add_parser("paper", help="生成试卷")
    p_paper.add_argument("--count", "-c", type=int, default=10, help="题量")
    p_paper.add_argument("--subject", "-s", help="知识点")
    p_paper.add_argument("--answers", "-a", action="store_true", help="显示答案")

    # random
    p_random = sub.add_parser("random", help="随机抽题")
    p_random.add_argument("--count", "-c", type=int, default=5, help="题量")
    p_random.add_argument("--subject", "-s", help="知识点")

    # wrong
    sub.add_parser("wrong", help="查看错题本")

    # stats
    sub.add_parser("stats", help="统计")

    args = parser.parse_args()

    if args.cmd == "add":
        q = add_question(args.question, args.answer, args.subject, args.explain)
        print(f"✅ 已保存 (ID: {q['id']})")

    elif args.cmd == "paper":
        paper = generate_paper(args.count, args.subject)
        if not paper["questions"]:
            print("❌ 暂无题目")
        else:
            print(format_paper(paper, args.answers))

    elif args.cmd == "random":
        qs = random_questions(args.count, args.subject)
        if not qs:
            print("❌ 暂无题目")
        else:
            print(format_questions(qs))

    elif args.cmd == "wrong":
        wrong = get_wrong_book()
        if not wrong:
            print("📖 错题本为空")
        else:
            print(f"📖 错题本 ({len(wrong)}题):")
            print(format_questions(wrong))

    elif args.cmd == "stats":
        s = stats()
        print(f"📊 总题数：{s['total']}")
        print(f"📖 错题数：{s['wrong']}")
        print("📚 知识点分布:")
        for subj, cnt in s["by_subject"].items():
            print(f"   {subj}: {cnt}题")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
