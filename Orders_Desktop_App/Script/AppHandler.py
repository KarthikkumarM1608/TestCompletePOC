import os

class ApplicationManager:
  def open_application(self):
        TestedApps.Orders.Run()
    
  def close_application(self, option = "No"):
    Aliases.Orders.Close()
    
    confirm_dialog = Aliases.CloseDlgConfirmation
    
    # based on the options(Yes/No/Cancel buttons) in the Close Confirmation pop-up being parsed,
    if confirm_dialog.Exists:
      if option == "Yes":
        confirm_dialog.btnYes.ClickButton()
      elif option == "No":
        confirm_dialog.btnNo.ClickButton()
      elif option == "Cancel":
        confirm_dialog.btnCancel.ClickButton()
    
  def force_shutdown(self):
    # Use the os module to forcefully kill the application
    os.system("taskkill /f /im Orders.exe")
