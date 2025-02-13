import os

class ApplicationManager:
  def open_application(self):
        TestedApps.Orders.Run()
    
  def close_application(self, option = "No"):
    Aliases.Orders.Close()
    
    confirm_dialog = Aliases.CloseDlgConfirmation
    
    # based on the options(Yes/No/Cancel buttons) in the Close Confirmation pop-up being parsed,
    if option == "Yes" and confirm_dialog.Exists:
      confirm_dialog.btnYes.ClickButton()
    elif option == "No" and confirm_dialog.Exists:
      confirm_dialog.btnNo.ClickButton()
    elif option == "Cancel"and confirm_dialog.Exists:
      confirm_dialog.btnCancel.ClickButton()
    
  def force_shutdown(self):
    # Use the os module to forcefully kill the application
    os.system("taskkill /f /im Orders.exe")
