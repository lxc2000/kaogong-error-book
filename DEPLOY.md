# 🦐 考公错题本 - GitHub 发布指南

## ✅ 已完成

- [x] 代码已提交到本地 git 仓库
- [x] README.md 已优化
- [x] .gitignore 已配置
- [x] setup.py 已准备

## 📤 上传到 GitHub

### 方式 1: 使用 GitHub CLI (推荐)

```bash
# 安装 gh (如果还没安装)
# 或者访问 https://cli.github.com/

# 登录 GitHub
gh auth login

# 创建仓库并推送
cd /home/admin/.openclaw/workspace/skills/exam-error-db
gh repo create kaogong-error-book --public --source=. --push
```

### 方式 2: 手动创建仓库

1. **访问 GitHub** https://github.com/new

2. **创建仓库**
   - 仓库名：`kaogong-error-book`
   - 描述：`轻量级考公错题管理工具 🦐`
   - 公开仓库 ✅
   - 不要初始化 README

3. **推送代码**
```bash
cd /home/admin/.openclaw/workspace/skills/exam-error-db
git remote add origin https://github.com/养虾哥/kaogong-error-book.git
git branch -M main
git push -u origin main
```

### 方式 3: 使用 Token

```bash
# 设置 token (替换 YOUR_TOKEN)
export GITHUB_TOKEN=your_personal_access_token

# 推送
git remote add origin https://${GITHUB_TOKEN}@github.com/养虾哥/kaogong-error-book.git
git push -u origin main
```

## 📱 微信小程序部署指南

### 准备工作

1. **注册小程序账号**
   - 访问 https://mp.weixin.qq.com/
   - 注册小程序
   - 获取 AppID

2. **下载微信开发者工具**
   - https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

### 小程序架构

```
考公错题本小程序
├── pages/
│   ├── index/        # 首页 - 随机抽题
│   ├── add/          # 添加错题
│   ├── paper/        # 生成试卷
│   ├── wrong/        # 错题本
│   └── stats/        # 统计
├── utils/
│   └── api.js        # 数据接口
├── app.js
├── app.json
└── project.config.json
```

### 开发步骤

1. **创建小程序项目**
   - 打开微信开发者工具
   - 导入项目
   - 填入 AppID

2. **配置域名**
   - 登录小程序后台
   - 开发管理 → 开发设置 → 服务器域名
   - 添加 API 域名

3. **数据同步方案**

   **方案 A: 云开发 (推荐)**
   ```javascript
   // 使用微信云数据库
   const db = wx.cloud.database()
   db.collection('questions').add({...})
   ```

   **方案 B: 自建后端**
   ```javascript
   // 调用 Python 后端 API
   wx.request({
     url: 'https://your-api.com/questions',
     method: 'POST',
     data: {...}
   })
   ```

   **方案 C: 本地存储**
   ```javascript
   // 使用小程序本地存储
   wx.setStorageSync('questions', [...])
   ```

### 快速模板

小虾可以帮你创建小程序基础模板，需要的话告诉我！

### 发布流程

1. 开发完成
2. 上传代码
3. 提交审核
4. 审核通过后发布

## 🎯 下一步

1. **创建 GitHub 仓库** - 选择上述方式之一
2. **推送代码** - `git push`
3. **发布 PyPI** (可选) - `pip install twine && twine upload dist/*`
4. **开发小程序** - 小虾可以帮忙！

---

需要小虾帮忙哪一步？🦐
