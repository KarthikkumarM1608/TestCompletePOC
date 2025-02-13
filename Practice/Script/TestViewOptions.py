import AppHandler
import EventHandler
import MainScreen
import OrderForm
import TestOpenExistingOrders

def test_view_options():
  
  TestOpenExistingOrders.test_one_open_existing_orders()
  
  toolBar = Aliases.Orders.MainForm.ToolBar
  
  toolBar.ClickItem(8, False)
  Tables.OrdersViewLargeIcons.Check()
  toolBar.ClickItem(9, False)
  Tables.OrdersViewSmallIcons.Check()
  toolBar.ClickItem(10, False)
  Tables.OrdersViewList.Check()
  toolBar.ClickItem(11, False)
  Tables.OrdersView.Check()