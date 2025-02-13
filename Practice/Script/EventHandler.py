import AppHandler

def AppEventsPractice_OnStartTestCase(Sender, StartTestCaseParams):
  try:
    Log.Message(f"Opening Application: {StartTestCaseParams.Name}")
    
    # Opening the Application
    app_manager = AppHandler.ApplicationManager()
    # clean-up the previously opened Application instances if any
    app_manager.force_shutdown()
    
    app_manager.open_application()
  
  except Exception as e:
    Log.Warning("Application launch Failed: {str(e)}")
    
def AppEventsPractice_OnStopTestCase(Sender, StopTestCaseParams):
  try:
    Log.Message(f"Closing Application: {StopTestCaseParams.Name}")
    
    # Closing the Application
    app_manager = AppHandler.ApplicationManager()
    
    app_manager.close_application()
  
  except Exception as e:
    Log.Warning("Application closing Failed: {str(e)}")
  