def Test1():
  Browsers.Item[btEdge].Navigate("https://practice.expandtesting.com/inputs")
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  page = browser.PracticeWebsite
  numberInput = page.Numberfield
  numberInput.SetText("12345")
  textbox = page.Textfield
  textbox.SetText("Test")
  passwordBox = page.Passwordfield
  passwordBox.SetText(Project.Variables.Password2)
  dateInput = page.DatePicker
  dateInput.Keys("12022025")
  page.DisplayInputsButton.ClickButton()
