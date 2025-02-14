class ShoppingCart:
  def __init__(self):
    self.page = Aliases.browser.ShoppingCartPage
    self.page.Wait()
  
  def click_checkout_link(self):
    self.page.linkCheckout.click()
    