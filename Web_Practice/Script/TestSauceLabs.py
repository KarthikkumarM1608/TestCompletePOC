def test_orders():
  DDT.CSVDriver(Project.Variables.csv_file_path)
  
  while not DDT.CurrentDriver.EOF():
    
    data = DDT.CurrentDriver.Value
  
    Log.AppendFolder(data["firstname"])
    Browsers.Item[btEdge].Navigate("https://www.saucedemo.com/v1/index.html")
    browser = Aliases.browser
    browser.BrowserWindow.Maximize()
    page = browser.LoginPage
    textbox = page.UserName
    textbox.SetText(Project.Variables.Username)
    passwordBox = page.Password
    passwordBox.SetText(Project.Variables.Password)
    page.LoginButton.ClickButton()
  
  
    page = browser.ProductsPage
    page.Wait()
    
    products = page.findElements("//div[@class='inventory_item_name']")
        
    for product in products:
      item = data["itemname"]
      
      Log.Message(item)
      
      if product.innerText == item:
      
        product.findElement("../../../div[3]/button").ClickButton()
        break
    
    page.CartIcon.Click()
      
    page = browser.ShoppingCartPage
    page.Wait()
    
    page.linkCheckout.Click()
    
    page = browser.CheckOutOne
    page.Wait()
    
    textbox = page.textboxFirstName
    textbox.SetText(data["firstname"])
    textbox = page.textboxLastName
    textbox.SetText(data["lastname"])
    textbox = page.textboxPostalCode
    textbox.SetText(data["zip"])
    page.submitbuttonContinue.ClickButton()
    
    page = browser.CheckOutTwo
    page.Wait()
    page.linkFinish.Click()
    
    page = browser.OrderConfirmationPage
    page.Wait()
    aqObject.CheckProperty(Aliases.browser.OrderConfirmationPage.FindElement("//h2[.='THANK YOU FOR YOUR ORDER']"), "contentText", cmpEqual, "THANK YOU FOR YOUR ORDER")
    Log.PopLogFolder()
    
    DDT.CurrentDriver.Next()
    