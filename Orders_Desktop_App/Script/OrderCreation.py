import datetime

class CreateOrders:
  def __init__(self):
    self.group_box = Aliases.OrderForm_GroupData
    
  def order_creation(self, data):
    group_box = Aliases.OrderForm_GroupData
    
    # Entering Customer Name, Street, City, State, Zip and Credit card details in Order Creation pop-up
    group_box.ProductNames.ClickItem(data["product"])
    group_box.Quantity.setText(data["quantity"])
    group_box.Priceperunit.setText(data["priceperunit"])
    group_box.Discount.setText(data["discount"])
    group_box.Total.setText(data["total"])
    
    card_type = data["card"]
    if card_type == "Visa":
      group_box.Visa.ClickButton()
    elif card_type == "MasterCard":
      group_box.MasterCard.ClickButton()
    elif card_type == "AmericanExpress":
      group_box.AmericanExpress.ClickButton()
    else:
      Log.Error("Invalid card type")
      
    group_box.Customer.SetText(data["name"])
    group_box.Street.SetText(data["street"])
    group_box.City.SetText(data["city"])
    group_box.State.SetText(data["state"])
    group_box.Zip.SetText(data["zip"])
    group_box.CardNo.SetText(data["creditcard"])
    
    # Entering today's date in Date field
    today = datetime.datetime.now()
    formatted = today.strftime("%m/%d/%y")

    date_picker = group_box.Date
    date_picker.wDate = formatted
    date_picker.Keys("[Tab]")
    
    # Entering Expiration Date, 
    exp_date_picker = group_box.ExpDate
    exp_date_picker.wDate = data["expirationdate"]
    exp_date_picker.Keys("[Tab]")

  def change_card_type(self, card_type):
    
    if card_type == "Visa":
      self.group_box.Visa.ClickButton()
    elif card_type == "MasterCard":
      self.group_box.MasterCard.ClickButton()
    elif card_type == "AmericanExpress":
      self.group_box.AmericanExpress.ClickButton()
  
  