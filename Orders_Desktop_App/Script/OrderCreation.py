﻿import datetime

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

  
      
  def get_productName(self, data):
    self.group_box.ProductNames.ClickItem(data["product"])
  
  def get_qty(self, data):
    qty = self.group_box.Quantity
    qty.setText(data["quantity"])
  
  def get_priceperunit(self, data):
    ppu = self.group_box.Priceperunit
    ppu.setText(data["priceperunit"])
    
  def get_discount(self, data):
    discnt = self.group_box.Discount
    discnt.setText(data["discount"])
  
  def get_total(self, data):
    total = self.group_box.Total
    total.setText(data["total"])
  
  def change_card_type(self, card_type):
      
      if card_type == "Visa":
        self.group_box.Visa.ClickButton()
      elif card_type == "MasterCard":
        self.group_box.MasterCard.ClickButton()
      elif card_type == "AmericanExpress":
        self.group_box.AmericanExpress.ClickButton()
  
  def get_card(self, data):
    try:
      if data["card"] == "Visa":
        self.group_box.Visa.ClickButton()
      elif data["card"] == "MasterCard":
        self.group_box.MasterCard.ClickButton()
      elif data["card"] == "AmericanExpress":
        self.group_box.AmericanExpress.ClickButton()
        
    except Exception as e:
      Log.Error("Card Selection Failed {e}")
      
  def get_customer(self, data):
    cust = self.group_box.Customer
    cust.SetText(data["name"])
    
  def get_street(self, data):
    street = self.group_box.Street
    street.SetText(data["street"])
  
  def get_city(self, data):
    city = self.group_box.City
    city.SetText(data["city"])

  def get_state(self, data):    
    state = self.group_box.State
    state.SetText(data["state"])
    
  def get_zip(self, data):
    zip = self.group_box.Zip
    zip.SetText(data["zip"])
    
  def get_card_number(self, data):
    card = self.group_box.CardNo
    card.SetText(data["creditcard"])
    
  def get_currentdate(self):
    # Entering today's date in Date field
    today = datetime.datetime.now()
    formatted = today.strftime("%m/%d/%y")

    date_picker = self.group_box.Date
    date_picker.wDate = formatted
    date_picker.Keys("[Tab]")
    
  def get_expirationdate(self, data):
    # Entering Expiration Date, 
    exp_date_picker = self.group_box.ExpDate
    exp_date_picker.wDate = data["expirationdate"]
    exp_date_picker.Keys("[Tab]")
