﻿class MainForm:
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
  
  def toolbar_open_existing_order(self, filepath):
    #Clicking Open button in the Toolbar
    toolbar = Aliases.ToolBar
    toolbar.ClickItem(1, False)
  
    Aliases.OpenDialog.OpenFile(filepath)
  
  def toolbar_edit_order(self):
    listView = Aliases.MainForm
    listView.OrdersView.ClickItem(1)
    #"Clare Jefferson", "FamilyAlbum")  
    toolbar = Aliases.ToolBar
    toolbar.ClickItem(5, False)
    