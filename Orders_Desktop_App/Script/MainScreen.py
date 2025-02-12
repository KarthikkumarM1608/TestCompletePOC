class MainForm:
  def new_order_mainmenu(self):

    # App - Instance created for Application
    main_form = Aliases.MainForm
    main_form.WaitProperty("Exists", True, 5000)
    if main_form.Exists:
      # clicking Orders > New Order... option from the Main Menu
      main_form.MainMenu.Click("Orders|New order...")
      #Aliases.MainForm.MainMenu.Click("Orders|New order...")
      order_form = Aliases.OrderForm
    
      return order_form
    else:
      Log.Error("Error in Mainform identification")
