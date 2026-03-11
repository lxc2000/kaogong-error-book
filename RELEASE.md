# 🦐 考公错题本 - 发布清单

## ✅ 已完成

- [x] Python 命令行工具 (exam_book.py)
- [x] pip 安装配置 (setup.py)
- [x] 本地安装脚本 (install.sh)
- [x] 微信小程序模板 (miniprogram/)
- [x] README 文档
- [x] 部署指南
- [x] Git 仓库初始化
- [x] 代码提交 (2 commits)

## 📤 上传到 GitHub

### 步骤 1: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写：
   - **仓库名**: `kaogong-error-book`
   - **描述**: `轻量级考公错题管理工具 🦐`
   - **公开仓库** ✅
   - **不要**初始化 README

3. 点击 "Create repository"

### 步骤 2: 推送代码

```bash
cd /home/admin/.openclaw/workspace/skills/exam-error-db

# 重命名分支为 main
git branch -M main

# 添加远程仓库 (替换为你的 GitHub 用户名)
git remote add origin https://github.com/YOUR_USERNAME/kaogong-error-book.git

# 推送
git push -u origin main
```

### 步骤 3: 验证

访问 `https://github.com/YOUR_USERNAME/kaogong-error-book` 确认代码已上传

---

## 📱 微信小程序部署

### 准备工作

1. **注册小程序账号**
   - 访问 https://mp.weixin.qq.com/
   - 注册小程序
   - 获取 **AppID**

2. **下载微信开发者工具**
   - https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

### 步骤 1: 导入项目

1. 打开微信开发者工具
2. 选择 "导入项目"
3. 项目目录：`/home/admin/.openclaw/workspace/skills/exam-error-db/miniprogram`
4. AppID: 填入你的 AppID (或选测试号)
5. 点击 "导入"

### 步骤 2: 配置项目

1. 打开 `project.config.json`
2. 修改 `appid` 为你的真实 AppID

### 步骤 3: 开发调试

1. 编译预览
2. 测试各功能：
   - ✅ 首页抽题
   - ✅ 添加错题
   - ✅ 生成试卷
   - ✅ 错题本
   - ✅ 统计

### 步骤 4: 上传发布

1. 点击右上角 "上传"
2. 填写版本号和备注
3. 登录小程序后台
4. 提交审核
5. 审核通过后发布

---

## 🎯 数据存储方案

### 当前：本地存储
```javascript
wx.setStorageSync('questions', [...])
```
**优点**: 简单、离线可用  
**缺点**: 数据不跨设备同步

### 进阶：云开发 (推荐)
```javascript
// 1. 开通云开发
wx.cloud.init({ env: 'your-env-id' })

// 2. 存储数据
const db = wx.cloud.database()
db.collection('questions').add({...})

// 3. 查询数据
db.collection('questions').where({...}).get()
```

### 进阶：自建后端
```python
# Flask API 示例
@app.route('/api/questions', methods=['POST'])
def add_question():
    data = request.json
    # 保存到数据库
    return {'ok': True}
```

---

## 📦 PyPI 发布 (可选)

```bash
# 安装工具
pip install build twine

# 构建
python -m build

# 上传到 TestPyPI (测试)
twine upload --repository testpypi dist/*

# 上传到 PyPI (正式)
twine upload dist/*
```

---

## 📊 项目结构

```
kaogong-error-book/
├── exam_book.py          # Python 主程序
├── setup.py              # pip 配置
├── install.sh            # 安装脚本
├── README.md             # 项目说明
├── SKILL.md              # 技能文档
├── DEPLOY.md             # 部署指南
├── .gitignore            # Git 忽略
│
└── miniprogram/          # 微信小程序
    ├── app.js
    ├── app.json
    ├── app.wxss
    ├── project.config.json
    ├── sitemap.json
    └── pages/
        ├── index/        # 首页
        ├── add/          # 添加
        ├── paper/        # 试卷
        ├── wrong/        # 错题本
        └── stats/        # 统计
```

---

## 🔧 后续优化

### Python 端
- [ ] 支持图片题目
- [ ] 支持数学公式
- [ ] 导出 PDF 试卷
- [ ] 导入 Excel 题库

### 小程序端
- [ ] 云开发集成
- [ ] 用户登录
- [ ] 数据同步
- [ ] 分享功能
- [ ] 答题模式
- [ ] 错题收藏

### 后端 (可选)
- [ ] RESTful API
- [ ] 用户系统
- [ ] 题库管理后台
- [ ] 数据分析

---

## 📞 需要帮助？

1. **GitHub 上传问题**: 检查网络连接，或使用 Gitee 镜像
2. **小程序审核**: 确保功能完整，无违规内容
3. **云开发**: 参考微信官方文档

---

Made with ❤️ by 小虾 🦐
