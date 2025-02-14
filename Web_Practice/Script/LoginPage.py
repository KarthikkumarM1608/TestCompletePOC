class Login:
  def __init__(self):
    self.page = Aliases.browser.LoginPage
    self.page.Wait()
    
  def enter_username(self, username):
    username_field = self.page.UserName
    username_field.SetText(username)
  
  def enter_password(self,password):
    password_field = self.page.Password
    password_field.SetText(password)
  
  def click_login(self):
   self.page.LoginButton.ClickButton()
   
  def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()
    