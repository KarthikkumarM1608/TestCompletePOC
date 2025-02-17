class ProductsPage:
  
  def __init__(self):
    self.page = Aliases.browser.ProductsPage
    self.page.Wait()
  
  def find_product(self, product_name):
    products = self.page.findElements("//div[@class='inventory_item_name']")
        
    for product in products:

      if product.innerText == product_name:
      
        product.findElement("../../../div[3]/button").ClickButton()
        break
    
  def click_cart_icon(self):
    self.page.CartIcon.click()  
  