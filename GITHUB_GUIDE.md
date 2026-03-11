# 🦐 考公错题本 - GitHub 上传指南

## ⚠️ 需要 GitHub Token

由于安全原因，小虾无法直接访问你的 GitHub 账号。请按以下步骤操作：

---

## 方式一：使用推送脚本 (推荐)

### 步骤 1: 获取 GitHub Token

1. 访问 https://github.com/settings/tokens/new
2. 填写说明：`kaogong-error-book`
3. 勾选权限：`repo` (完整控制)
4. 点击 "Generate token"
5. **复制 Token** (只显示一次，保存好！)

### 步骤 2: 运行推送脚本

```bash
cd /home/admin/.openclaw/workspace/skills/exam-error-db

# 赋予执行权限
chmod +x push-to-github.sh

# 运行 (替换为你的 GitHub 用户名和 Token)
./push-to-github.sh 养虾哥 ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 方式二：手动操作

### 步骤 1: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写：
   - **Repository name**: `kaogong-error-book`
   - **Description**: `轻量级考公错题管理工具 🦐`
   - **Public** ✅
   - ❌ 不要勾选 "Add a README file"
   - ❌ 不要勾选 "Add .gitignore"
   - ❌ 不要勾选 "Choose a license"

3. 点击 "Create repository"

### 步骤 2: 推送代码

```bash
cd /home/admin/.openclaw/workspace/skills/exam-error-db

# 重命名分支为 main
git branch -M main

# 添加远程仓库 (替换为你的 GitHub 用户名)
git remote add origin https://github.com/你的用户名/kaogong-error-book.git

# 推送
git push -u origin main
```

如果提示认证，输入：
- 用户名：你的 GitHub 用户名
- 密码：使用上面生成的 Token (不是登录密码)

---

## 方式三：使用 GitHub Desktop

1. 下载 https://desktop.github.com/
2. 登录 GitHub 账号
3. File → Add Local Repository → 选择 `exam-error-db` 文件夹
4. Publish repository

---

## 验证上传

访问 `https://github.com/你的用户名/kaogong-error-book`

应该看到以下文件：
```
✅ exam_book.py
✅ setup.py
✅ install.sh
✅ README.md
✅ SKILL.md
✅ DEPLOY.md
✅ RELEASE.md
✅ miniprogram/
```

---

## 📱 微信小程序下一步

上传成功后：

1. 下载微信开发者工具
   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

2. 导入项目
   - 目录：`miniprogram/`
   - AppID：你的小程序 AppID (或测试号)

3. 修改 `project.config.json`
   ```json
   {
     "appid": "你的真实 AppID"
   }
   ```

4. 编译 → 上传 → 提交审核

---

## 🆘 遇到问题？

### 问题 1: 认证失败
```
remote: Authentication failed
```
**解决**: 使用 Token 而不是密码
```bash
git remote set-url origin https://ghp_xxx@github.com/用户名/kaogong-error-book.git
```

### 问题 2: 仓库已存在
```
remote: Repository already exists
```
**解决**: 删除远程仓库后重试，或换个仓库名

### 问题 3: 网络问题
```
fatal: unable to access
```
**解决**: 检查网络，或使用代理

---

## 📞 需要帮助？

告诉小虾：
- 你的 GitHub 用户名
- 遇到的具体错误信息

小虾帮你诊断！🦐
