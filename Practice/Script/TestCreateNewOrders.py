import OrderForm
import AppHandler
import EventHandler
import MainScreen

def test_one_create_orders():
  mainform = MainScreen.MainForm()
  mainform.click_main_menu_new_order()
  
  # Implementing DDT approach
  DDT.CSVDriver(Project.Variables.csv_file_path)
  
  
  while not DDT.CurrentDriver.EOF():
    data = DDT.CurrentDriver.Value
    Log.AppendFolder(data["name"])
    order_form = OrderForm.OrderForm()
    order_form.WaitProperty("Exists", True, 5000)
    order_form.create_order(data)
      
    orderForm.ButtonOK.ClickButton()
    Log.PopLogFolder()
    DDT.CurrentDriver.Next()