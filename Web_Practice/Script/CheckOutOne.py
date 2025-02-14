class CheckOutOne:
  
  def __init__(self):
    self.page = Aliases.browser.CheckOutOne
    self.page.Wait()
  
  def enter_firstname(self, firstname):
    self.page.FirstName.setText(firstname)
  
  def enter_lastname(self, lastname):
      self.page.LastName.setText(lastname)
      
  def enter_zipcode(self, zipcode):
      self.page.PostalCode.setText(zipcode)
  
  def fill_your_info(self, firstname, lastname, zipcode):
    self.enter_firstname(firstname)
    self.enter_lastname(lastname)
    self.enter_zipcode(zipcode)
  
  def click_continue(self):
    self.page.ContinueButton.click()
  