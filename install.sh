#!/bin/bash
# 考公错题本 - 安装脚本

echo "🦐 考公错题本 - 安装中..."

# 创建数据目录
mkdir -p ~/.openclaw/workspace/exam-errors

# 创建可执行目录
mkdir -p ~/.local/bin

# 复制脚本
cp exam_book.py ~/.local/bin/exam-book
chmod +x ~/.local/bin/exam-book

echo ""
echo "✅ 安装完成!"
echo ""
echo "使用方法:"
echo "  exam-book add \"题目\" \"答案\" -s 知识点 -e 解析"
echo "  exam-book paper -c 10"
echo "  exam-book random -c 5"
echo "  exam-book wrong"
echo "  exam-book stats"
echo ""
echo "或者使用 Python 直接运行:"
echo "  python3 exam_book.py ..."
echo ""
