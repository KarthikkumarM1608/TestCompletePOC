class ProductsPage:
  
  def __init__(self):
    self.page = Aliases.browser.ProductsPage
    self.page.Wait()
  
  def wait_for_page(self):
    self.page.Wait()
    
  def validate_page_loaded(self):
    return self.page.Exists
  
  def find_product(self, product_name):
    products = self.page.findElements("//div[@class='inventory_item_name']")
        
    for product in products:

      if product.innerText == product_name:
      
        product.findElement("../../../div[3]/button").ClickButton()
        break
    
    self.page.CartIcon.Click()

  def click_cart_icon(self):
    self.page.CartIcon.click()  
  