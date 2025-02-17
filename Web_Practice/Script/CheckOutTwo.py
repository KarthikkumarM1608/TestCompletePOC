class CheckOutTwo:
  
  def __init__(self):
    self.page = Aliases.browser.CheckOutTwo
    self.page.Wait()
    
  def click_finish(self):
    self.page.linkFinish.click()
  
  def extract_payment_info(self):
    payment_info = self.page.findElement("//div[text()='Payment Information:']/../div[2]").textContent
    return payment_info
    
  def extract_shipping_info(self):
    shipping_info = self.page.findElement("//div[text()='Shipping Information:']/../div[4]").textContent
    return shipping_info
  
    