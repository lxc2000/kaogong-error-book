App({
  onLaunch: function () {
    // 初始化云开发环境（如果使用云开发）
    // wx.cloud.init({ env: 'your-env-id' })
    
    // 从本地存储加载数据
    const questions = wx.getStorageSync('questions')
    const wrongBook = wx.getStorageSync('wrongBook')
    
    if (!questions) {
      wx.setStorageSync('questions', [])
    }
    if (!wrongBook) {
      wx.setStorageSync('wrongBook', [])
    }
  },
  
  globalData: {
    questions: [],
    wrongBook: []
  }
})
