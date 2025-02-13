class MainForm:
  
  def click_toolbar(self, option):
    mainform = Aliases.Orders.MainForm
    
    if option == "Open":
      index = 1
    elif option == "Save":
      index = 2
    
    # clicking the option based on the param received  
    mainform.Toolbar.ClickItem(index, False)
    
  def click_main_menu_new_order(self):
    mainform = Aliases.Orders.MainForm
    mainform.MainMenu.Click("Orders|New order...")
  