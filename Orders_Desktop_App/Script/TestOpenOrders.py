﻿import AppHandler
import MainScreen
import OrderCreation


def test_one_open_existing_orders():
  
  # TS - Instance created for ApplicationManager class
  #app_manager = AppHandler.ApplicationManager()
  
  # Force close any running instances at the start
  #app_manager.force_shutdown()  

  # Opening the Application
  #app_manager.open_application()

    
  #Clicking Open button in the Toolbar
  toolbar = Aliases.ToolBar
  toolbar.ClickItem(1, False)
  
  Aliases.OpenDialog.OpenFile(Project.Variables.open_order_table)
  
  
  # validating the orders table with checkpoint
  Tables.OpenOrderOrdersView.Check()
  
  #app_manager.close_application()