class OrderConfirmationPage:
  def __init__(self):
    self.page = Aliases.browser.OrderConfirmationPage
    self.page.Wait()
  
  def validate_checkpoint(self):
    aqObject.CheckProperty(self.page.FindElement("//h2[.='THANK YOU FOR YOUR ORDER']"), "contentText", cmpEqual,
     "THANK YOU FOR YOUR ORDER")
  
  def navigate_products_page(self):
    self.page.ToUrl("https://www.saucedemo.com/v1/inventory.html")