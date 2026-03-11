# 🦐 考公错题本

> 轻量级考公错题管理工具 - 简单、好用、可打包

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## ✨ 特点

- 🍃 **极简** - 200 行代码，零依赖
- ⚡ **轻量** - 秒启动，不占资源
- 📦 **可打包** - pip / exe / 本地安装
- 💾 **离线** - 数据本地 JSON 存储
- 💬 **对话式** - 支持自然语言交互

## 🚀 快速开始

### 安装

**方式 1: 直接使用**
```bash
python3 exam_book.py stats
```

**方式 2: 本地安装**
```bash
chmod +x install.sh
./install.sh
exam-book stats
```

**方式 3: pip 安装**
```bash
pip install -e .
exam-book stats
```

**方式 4: 打包成可执行文件**
```bash
pip install pyinstaller
pyinstaller -F exam_book.py
# 生成 dist/exam_book
```

### 使用

```bash
# 添加错题
exam-book add "题目内容" "答案" -s 言语理解 -e "解析"

# 生成试卷
exam-book paper -c 10          # 10 题
exam-book paper -c 10 -a       # 带答案

# 随机抽题
exam-book random -c 5

# 查看错题本
exam-book wrong

# 统计
exam-book stats
```

## 📊 功能

| 功能 | 说明 |
|------|------|
| 📝 记录错题 | 题目、答案、知识点、解析 |
| 🎲 随机抽题 | 按知识点筛选 |
| 📄 生成试卷 | 自定义题量，可选答案 |
| 📖 错题本 | 自动收集错题 |
| 📊 统计 | 题量、知识点分布 |

## 📁 文件结构

```
exam-error-db/
├── exam_book.py      # 主程序 (200 行)
├── setup.py          # pip 安装配置
├── install.sh        # 本地安装脚本
├── README.md         # 说明文档
├── SKILL.md          # 技能文档
└── .gitignore        # Git 忽略文件
```

## 💾 数据存储

数据存储在 `~/.openclaw/workspace/exam-errors/book.json`

```json
{
  "questions": [
    {
      "id": "abc123",
      "question": "题目内容",
      "answer": "A",
      "subject": "言语理解",
      "explain": "解析",
      "created": "2026-03-11"
    }
  ],
  "wrong_book": ["abc123"],
  "stats": {"total": 1}
}
```

## 📱 微信小程序

小程序版本开发中...

## 🆚 对比其他考试系统

| | xzs | 考公错题本 |
|---|-----|-----------|
| 代码量 | 10 万 + 行 | 200 行 |
| 依赖 | Java/Spring/Vue | 无 |
| 数据库 | PostgreSQL | JSON |
| 启动 | 分钟级 | 秒级 |

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 License

MIT License

## 👤 作者

养虾哥 🦐

---

Made with ❤️ for 考公人
