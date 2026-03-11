Page({
  data: {
    question: '',
    answer: '',
    explain: '',
    subjects: ['言语理解', '数量关系', '常识判断', '判断推理', '资料分析'],
    subjectIndex: 0
  },

  onQuestionInput: function (e) {
    this.setData({
      question: e.detail.value
    })
  },

  onAnswerInput: function (e) {
    this.setData({
      answer: e.detail.value
    })
  },

  onExplainInput: function (e) {
    this.setData({
      explain: e.detail.value
    })
  },

  onSubjectChange: function (e) {
    this.setData({
      subjectIndex: e.detail.value
    })
  },

  saveQuestion: function () {
    const { question, answer, explain, subjects, subjectIndex } = this.data

    if (!question.trim()) {
      wx.showToast({ title: '请输入题目', icon: 'none' })
      return
    }
    if (!answer.trim()) {
      wx.showToast({ title: '请输入答案', icon: 'none' })
      return
    }

    const questions = wx.getStorageSync('questions') || []
    const newQuestion = {
      id: Date.now().toString(),
      question: question.trim(),
      answer: answer.trim().toUpperCase(),
      subject: subjects[subjectIndex],
      explain: explain.trim(),
      created: new Date().toISOString().split('T')[0]
    }

    questions.push(newQuestion)
    wx.setStorageSync('questions', questions)

    wx.showToast({ title: '保存成功', icon: 'success' })
    
    // 清空表单
    this.setData({
      question: '',
      answer: '',
      explain: '',
      subjectIndex: 0
    })

    // 2 秒后返回
    setTimeout(() => {
      wx.navigateBack()
    }, 1500)
  }
})
