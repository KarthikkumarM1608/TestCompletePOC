import OrderCreation
import MainScreen
import AppHandler

def test_one_create_orders_mainmenu():
  # Data Driven Testing Approach - Create New orders in the Application Main menu Orders > New Orders... based on the supplied csv file
  
  # Reading the CSV file path from Variables  
  DDT.CSVDriver(Project.Variables.csv_file_path)
  
  # TS - Instance created for MainForm (Main Window) class
  main_form = MainScreen.MainForm()
  
  while not DDT.CurrentDriver.EOF():
    # clicking on File > Orders > New Order... option
    main_form.new_order_mainmenu()
    
    # waiting for Order Form pop-up and creating warning if missing
    order_form = Aliases.OrderForm
    if not order_form.WaitProperty("Exists", True, 5000):
      Log.Error("Order Form pop-up is not displayed")
  
    #order_form.waitConfirm(5000)
      
    data = DDT.CurrentDriver.Value
    Log.AppendFolder(data["name"])
    
    # Calling Create Orders class for creating the Orders
    create = OrderCreation.CreateOrders()
    create.order_creation(data)
  
    # clicking OK button in the Order Creation pop-up
    order_form.ButtonOK.ClickButton()
    
    date_format_warning = Aliases.DatedlgWarning
    if date_format_warning.Exists:
      date_format_warning.btnOK.ClickButton()

    Log.PopLogFolder()
  
    # Incrementing the Data-driven test to next set,
    DDT.CurrentDriver.Next()
  