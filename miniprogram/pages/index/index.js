Page({
  data: {
    totalQuestions: 0,
    wrongCount: 0,
    currentQuestion: null,
    showAnswer: false
  },

  onLoad: function () {
    this.loadStats()
  },

  onShow: function () {
    this.loadStats()
  },

  loadStats: function () {
    const questions = wx.getStorageSync('questions') || []
    const wrongBook = wx.getStorageSync('wrongBook') || []
    
    this.setData({
      totalQuestions: questions.length,
      wrongCount: wrongBook.length
    })
  },

  nextQuestion: function () {
    const questions = wx.getStorageSync('questions') || []
    
    if (questions.length === 0) {
      wx.showToast({
        title: '暂无题目，先去添加吧',
        icon: 'none'
      })
      return
    }
    
    const randomIndex = Math.floor(Math.random() * questions.length)
    this.setData({
      currentQuestion: questions[randomIndex],
      showAnswer: false
    })
  },

  toggleAnswer: function () {
    this.setData({
      showAnswer: !this.data.showAnswer
    })
  },

  goToAdd: function () {
    wx.navigateTo({
      url: '/pages/add/add'
    })
  },

  gotoPaper: function () {
    wx.navigateTo({
      url: '/pages/paper/paper'
    })
  },

  gotoWrong: function () {
    wx.navigateTo({
      url: '/pages/wrong/wrong'
    })
  }
})
