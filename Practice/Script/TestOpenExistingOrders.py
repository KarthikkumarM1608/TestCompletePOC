import MainScreen

def test_one_open_existing_orders():
  Log.Message("Testing started")
  # click on the Toolbar to open the Existing Orders
  mainform = MainScreen.MainForm()
  mainform.click_toolbar("Open")
  
  Aliases.OpenDialog.OpenFile(Project.Variables.orders_file)
  
  # Grid validation checkpoint
  Tables.OrdersView.Check()
  
  # click on Save button in the Toolbar
  mainform.click_toolbar("Save") 
  
  