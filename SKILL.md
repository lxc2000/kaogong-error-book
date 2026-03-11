# exam-error-db - 考公错题本 🦐

轻量级考公错题管理工具 - 简单、好用、可打包

## 特点

- ✅ **极简** - 单文件 Python，无依赖
- ✅ **轻量** - 秒启动，不占资源
- ✅ **可打包** - 支持 pip 安装/独立 executable
- ✅ **离线** - 数据本地存储
- ✅ **对话式** - 集成 OpenClaw，自然语言交互

## 安装

### 方式 1: 直接使用
```bash
python3 exam_book.py
```

### 方式 2: 本地安装
```bash
chmod +x install.sh
./install.sh
exam-book stats  # 使用
```

### 方式 3: pip 安装
```bash
pip install -e .
exam-book stats
```

### 方式 4: 打包成可执行文件
```bash
pip install pyinstaller
pyinstaller -F exam_book.py
# 生成 dist/exam_book
```

## 使用

### 命令行
```bash
# 添加错题
exam-book add "题目内容" "答案" -s 言语理解 -e "解析"

# 生成试卷
exam-book paper -c 10          # 10 题
exam-book paper -c 10 -a       # 带答案

# 随机抽题
exam-book random -c 5

# 错题本
exam-book wrong

# 统计
exam-book stats
```

### OpenClaw 对话
```
"记录错题：题目是...，答案是 C，知识点是言语理解"
"来一道题"
"生成 10 道题的试卷"
"查看我的错题"
```

## 功能

| 功能 | 说明 |
|------|------|
| 📝 记录错题 | 题目、答案、知识点、解析 |
| 🎲 随机抽题 | 按知识点筛选 |
| 📄 生成试卷 | 自定义题量，可选答案 |
| 📖 错题本 | 自动收集错题 |
| 📊 统计 | 题量、知识点分布 |

## 数据存储

```
~/.openclaw/workspace/exam-errors/book.json
```

JSON 格式，简单透明：
```json
{
  "questions": [...],
  "wrong_book": [...],
  "stats": {"total": 0}
}
```

## 文件结构

```
exam-error-db/
├── exam_book.py      # 主程序 (单文件)
├── setup.py          # pip 安装配置
├── install.sh        # 本地安装脚本
├── README.md         # 详细说明
└── SKILL.md          # 技能文档
```

## 与 xzs 对比

| | xzs | 考公错题本 |
|---|-----|-----------|
| 定位 | 企业考试系统 | 个人错题工具 |
| 代码量 | 10 万 + 行 | 200 行 |
| 依赖 | Java/Spring/Vue | 无 |
| 数据库 | PostgreSQL | JSON 文件 |
| 启动 | 分钟级 | 秒级 |
| 学习成本 | 高 | 零 |

## 开发

```bash
# 运行
python3 exam_book.py

# 测试
python3 exam_book.py stats

# 打包
pyinstaller -F exam_book.py
```
