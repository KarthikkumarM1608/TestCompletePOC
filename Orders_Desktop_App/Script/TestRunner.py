﻿import TestOpenOrders
import TestOrdersCreation
import AppHandler


def test_runner():
  test_cases = [TestOrdersCreation.test_one_create_orders_mainmenu, TestOpenOrders.open_existing_orders]
  
  app_handler = AppHandler.ApplicationManager()
  for test in test_cases:
    try:
      test()
    except Exception as e:
      Log.Error(f"Error occurred + str{e}")
      app_handler.force_shutdown()
      Delay(2000)
      app_handler.open_application()
