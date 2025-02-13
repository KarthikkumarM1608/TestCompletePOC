def Test1():
  Browsers.Item[btEdge].Navigate("https://practice.expandtesting.com/tables")
  browser = Sys.Browser()
  first_name = browser.FindElements("//tbody/tr/td[2]")
  
  for i in first_name:
    if i.Text == "Frank":
      Log.Message(i.Text)
      break
  
  #.FindElement("//div//tr[2]/td/a[contains(@class, 'btn-primary')]").Keys("[Enter]")
  

