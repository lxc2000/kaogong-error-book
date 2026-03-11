#!/bin/bash
# 考公错题本 - 一键推送到 GitHub

echo "🦐 考公错题本 - GitHub 推送脚本"
echo "══════════════════════════════════"
echo ""

# 检查是否输入了 GitHub 用户名
if [ -z "$1" ]; then
    echo "❌ 请提供 GitHub 用户名"
    echo ""
    echo "用法：$0 <GitHub 用户名> [Token]"
    echo ""
    echo "例如:"
    echo "  $0 liuxicheng"
    echo "  $0 liuxicheng ghp_xxxxxxxxxxxx"
    echo ""
    exit 1
fi

USERNAME=$1
TOKEN=$2
REPO="kaogong-error-book"

echo "📤 准备推送到 GitHub"
echo "   用户名：$USERNAME"
echo "   仓库名：$REPO"
echo ""

# 切换到项目目录
cd "$(dirname "$0")"

# 重命名分支为 main
git branch -M main 2>/dev/null || true

# 检查是否已有远程仓库
if git remote | grep -q "origin"; then
    echo "⚠️  已存在 origin 远程仓库"
    read -p "是否删除并重新添加？(y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote remove origin
    else
        echo "❌ 已取消"
        exit 1
    fi
fi

# 添加远程仓库
if [ -n "$TOKEN" ]; then
    echo "🔐 使用 Token 认证"
    git remote add origin https://${TOKEN}@github.com/${USERNAME}/${REPO}.git
else
    echo "🔐 使用 HTTPS (需要手动输入密码或 Token)"
    git remote add origin https://github.com/${USERNAME}/${REPO}.git
fi

# 推送
echo ""
echo "🚀 开始推送..."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "══════════════════════════════════"
    echo "✅ 推送成功!"
    echo ""
    echo "📱 访问仓库:"
    echo "   https://github.com/${USERNAME}/${REPO}"
    echo ""
    echo "📦 安装 (发布后):"
    echo "   pip install kaogong-error-book"
    echo ""
    echo "📱 小程序:"
    echo "   用开发者工具打开 miniprogram/ 目录"
    echo ""
else
    echo ""
    echo "══════════════════════════════════"
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因:"
    echo "1. 仓库不存在 - 请先在 GitHub 创建仓库"
    echo "2. 认证失败 - 请使用 Token"
    echo "3. 网络问题 - 请检查连接"
    echo ""
    echo "手动创建仓库:"
    echo "   https://github.com/new"
    echo "   仓库名：kaogong-error-book"
    echo ""
fi
