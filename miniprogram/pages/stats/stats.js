Page({
  data: {
    totalQuestions: 0,
    wrongCount: 0,
    accuracy: 0,
    subjects: []
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
    
    // 计算知识点分布
    const subjectCount = {}
    questions.forEach(q => {
      subjectCount[q.subject] = (subjectCount[q.subject] || 0) + 1
    })
    
    const subjects = Object.keys(subjectCount).map(name => ({
      name,
      count: subjectCount[name]
    }))
    
    // 计算正确率
    const accuracy = questions.length > 0 
      ? Math.round((questions.length - wrongBook.length) / questions.length * 100)
      : 0
    
    this.setData({
      totalQuestions: questions.length,
      wrongCount: wrongBook.length,
      accuracy,
      subjects
    })
  }
})
