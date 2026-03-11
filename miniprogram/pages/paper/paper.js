Page({
  data: {
    paperTitle: '考公错题练习卷',
    date: '',
    questions: [],
    answers: [],
    showAnswer: false
  },

  onLoad: function () {
    this.generatePaper()
  },

  generatePaper: function () {
    const questions = wx.getStorageSync('questions') || []
    
    if (questions.length === 0) {
      wx.showToast({ title: '暂无题目', icon: 'none' })
      return
    }
    
    // 随机抽取 10 题
    const count = Math.min(10, questions.length)
    const shuffled = [...questions].sort(() => Math.random() - 0.5)
    const selected = shuffled.slice(0, count)
    
    this.setData({
      date: new Date().toISOString().split('T')[0],
      questions: selected,
      answers: selected.map((q, i) => ({ num: i + 1, answer: q.answer })),
      showAnswer: false
    })
  },

  showAnswers: function () {
    this.setData({
      showAnswer: true
    })
  }
})
