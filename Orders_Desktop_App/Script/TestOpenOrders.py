import AppHandler
import MainScreen
import OrderCreation


def test_one_open_existing_orders():
  
  # Open the Existing Orders from csv file
  main_form = MainScreen.MainForm()
  main_form.toolbar_open_existing_order(Project.Variables.open_order_table)
  
  # validating the orders table with checkpoint
  Tables.OpenOrderOrdersView.Check()
  
def test_edit_existing_order():
  
  # Open the Existing Orders from csv file
  main_form = MainScreen.MainForm()
  main_form.toolbar_open_existing_order(Project.Variables.open_order_table)
  
  # click on the First row
  Aliases.MainForm.OrdersView.DblClickItem(0)
  
  # Edit the Order and change the card type to Visa
  edit_order = OrderCreation.CreateOrders()
  edit_order.change_card_type("Visa")