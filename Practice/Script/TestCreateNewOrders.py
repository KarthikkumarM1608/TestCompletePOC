import OrderForm
import AppHandler
import EventHandler
import MainScreen

def test_one_create_orders():
  mainform = MainScreen.MainForm()
  mainform.click_main_menu_new_order()
  
  # Implementing DDT approach
  DDT.CSVDriver(Project.Variables.csv_file_path)
  
  data = DDT.CurrentDriver.Value
  
  order_form = OrderForm.OrderForm()
  order_form.create_order(data)
  
  orderForm = orders.OrderForm
  groupBox = orderForm.Group
  textBox = groupBox.Customer
  textBox.Click(39, 9)
  textBox.SetText("test")
  textBox.Keys("[Tab]")
  textBox = groupBox.Street
  textBox.SetText("test")
  textBox.Keys("[Tab]")
  textBox = groupBox.City
  textBox.SetText("test")
  textBox.Keys("[Tab]")
  textBox = groupBox.State
  textBox.SetText("test")
  textBox.Keys("[Tab]")
  textBox = groupBox.Zip
  textBox.SetText("tet")
  textBox.Keys("[Tab]")
  groupBox.Visa.Keys("[Tab]")
  textBox = groupBox.CardNo
  textBox.SetText("testw")
  textBox.Keys("[Enter]")
  orderForm.Click(370, 468)
  orderForm.ButtonOK.ClickButton()
