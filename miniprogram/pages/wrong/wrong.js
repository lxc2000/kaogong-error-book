Page({
  data: {
    wrongQuestions: []
  },

  onLoad: function () {
    this.loadWrongBook()
  },

  onShow: function () {
    this.loadWrongBook()
  },

  loadWrongBook: function () {
    const questions = wx.getStorageSync('questions') || []
    const wrongIds = wx.getStorageSync('wrongBook') || []
    
    const wrong = questions.filter(q => wrongIds.includes(q.id))
    
    this.setData({
      wrongQuestions: wrong
    })
  }
})
