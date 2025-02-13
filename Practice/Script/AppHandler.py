import os

class ApplicationManager:
  
  def open_application(self):
    TestedApps.Orders.Run()
  
  
  def close_application(self):
    TestedApps.Orders.Close()
    
  def force_shutdown(self):
    os.system("taskkill /f /im Orders.exe")
    