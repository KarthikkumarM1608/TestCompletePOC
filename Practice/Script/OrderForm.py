class OrderForm:
  
  def create_order(self, data):
    orderform = Aliases.OrderForm
    group_box = orderform.Group
    
    # Entering ProductName
    group_box.ProductNames.ClickItem(data["product"])
    
    Delay(10000)
    