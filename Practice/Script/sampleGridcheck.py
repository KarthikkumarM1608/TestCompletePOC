def Test1():
  mainForm = Aliases.Orders.MainForm
  mainForm.ToolBar.ClickItem(1, False)
  dlgOpen = Aliases.OpenDialog
  dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.CtrlNotifySink.ScrollBar.wPosition = 68
  dlgOpen.OpenFile("C:\\Users\\Public\\Documents\\TestComplete 15 Samples\\Desktop\\Orders\\MyTable.tbl", "Table (*.tbl)")
  #mainForm.OrdersView.ClickItem("Charles Dodgeson", 0)
  #Tables.OrdersView_gridrow.Check()
    
  # Access the Items property of the grid
  items = mainForm.OrdersView.Items
  customer_name = "Charles Dodgeson"
  found = False
    
  # Iterate through the rows in the Items collection
  for i in range(items.Count):  # Assuming Items.Count gives the total number of rows
      row = items.Item[i]  # Access the ith row
      Log.Message(row)
      '''
      cell_value = row.CustomerName  # Adjust as needed to access the specific cell
      if cell_value == customer_name:
          Log.Message(f"Row found at index: {i}")
          found = True
          break
    
  if not found:
      Log.Message("Row not found")

  # Perform additional validation on the found row
  if found:
      second_column_value = row.AnotherColumn  # Adjust as needed to access another cell
      Log.Message(f"Value in another column of the found row: {second_column_value}")
'''
# Call the function
Test1()