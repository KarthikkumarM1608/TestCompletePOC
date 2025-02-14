class CheckOutTwo:
  
  def __init__(self):
    self.page = Aliases.browser.CheckOutTwo
    self.page.Wait()
    
  def click_finish(self):
    self.page.linkFinish.click()