# 微信小程序开发指南

## 📱 快速开始

### 1. 下载微信开发者工具

访问官网下载并安装微信开发者工具：
https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

### 2. 导入项目

打开微信开发者工具，选择"导入项目"，填写以下信息：

- **项目目录**：`C:\Users\admin\WorkBuddy\20260311210646\kaogong-error-book\miniprogram`
- **AppID**：
  - 如果有小程序 AppID，直接填写
  - 如果没有，选择"测试号"（可以测试基本功能）
- **项目名称**：考公错题本

### 3. 修改 AppID

打开 `project.config.json` 文件，将 `appid` 字段修改为你的真实 AppID：

```json
{
  "appid": "你的真实AppID",
  "projectname": "考公错题本"
}
```

## 🚀 项目结构

```
miniprogram/
├── app.js              # 小程序主文件
├── app.json            # 小程序配置
├── app.wxss            # 全局样式
├── project.config.json # 项目配置
├── sitemap.json        # 搜索配置
└── pages/              # 页面目录
    ├── index/          # 首页
    ├── add/            # 添加错题
    ├── random/         # 随机抽题
    ├── paper/          # 生成试卷
    └── wrong/          # 错题本
```

## 📋 功能说明

### 首页
- 显示题目统计信息
- 快速导航到各个功能

### 添加错题
- 记录题目内容
- 记录答案
- 记录知识点
- 记录解析

### 随机抽题
- 从题库中随机抽取题目
- 支持按知识点筛选

### 生成试卷
- 自定义题目数量
- 选择是否包含答案
- 生成可打印的试卷

### 错题本
- 查看所有错题
- 复习错题
- 移除已掌握的错题

## 🔧 开发注意事项

### 1. 数据存储

小程序使用本地存储保存数据：

```javascript
// 保存题目
wx.setStorageSync('questions', questionList)

// 读取题目
const questions = wx.getStorageSync('questions') || []

// 保存错题本
wx.setStorageSync('wrongBook', wrongBookList)

// 读取错题本
const wrongBook = wx.getStorageSync('wrongBook') || []
```

### 2. 页面配置

每个页面需要四个文件：
- `.js` - 页面逻辑
- `.wxml` - 页面结构
- `.wxss` - 页面样式
- `.json` - 页面配置（可选）

### 3. 调试方法

使用微信开发者工具的调试功能：
- 点击右侧"调试器"按钮
- 在 Console 中查看日志
- 使用 `console.log()` 输出调试信息
- 在 Network 面板查看网络请求

## 📦 发布准备

### 1. 测试号 vs 正式号

- **测试号**：适合开发测试，功能有限
- **正式号**：需要注册小程序，功能完整

### 2. 注册小程序

如果需要发布正式版，请：
1. 访问 https://mp.weixin.qq.com/
2. 点击"立即注册"
3. 选择"小程序"
4. 按照指引完成注册
5. 获取正式 AppID

### 3. 上传代码

在微信开发者工具中：
1. 点击顶部"上传"按钮
2. 填写版本号和项目备注
3. 点击"上传"

### 4. 提交审核

在微信公众平台：
1. 进入"版本管理"
2. 选择开发版本
3. 点击"提交审核"
4. 填写审核信息
5. 等待审核通过

## 🐛 常见问题

### Q: project.config.json 中 AppID 填什么？
A: 如果有正式 AppID 就填写正式的，没有可以先填测试号，后续可以修改。

### Q: 本地数据会丢失吗？
A: 不会，除非用户清除小程序数据或卸载小程序。

### Q: 如何备份题目数据？
A: 可以在设置中添加"导出数据"功能，将数据导出为 JSON 文件。

### Q: 小程序能离线使用吗？
A: 可以，所有数据都存储在本地，无需网络连接。

## 📚 参考资源

- [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)
- [微信开发者工具使用指南](https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html)
- [小程序 API 文档](https://developers.weixin.qq.com/miniprogram/dev/api/)

## 💡 开发建议

1. **先在模拟器中测试**，确保功能正常
2. **真机调试**，在真机上测试实际效果
3. **测试不同机型**，确保兼容性
4. **性能优化**，注意小程序包大小限制（2MB）
5. **用户体验**，遵循微信小程序设计规范

---

**Happy Coding! 🎉**
