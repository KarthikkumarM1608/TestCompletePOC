import AppHandler
import MainScreen
import OrderCreation


def test_one_open_existing_orders():
   
  #Clicking Open button in the Toolbar
  toolbar = Aliases.ToolBar
  toolbar.ClickItem(1, False)
  
  Aliases.OpenDialog.OpenFile(Project.Variables.open_order_table)
  
  
  # validating the orders table with checkpoint
  Tables.OpenOrderOrdersView.Check()
  