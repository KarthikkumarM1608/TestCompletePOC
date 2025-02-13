import AppHandler

def OrdersAppEvents_OnStartTestCase(Sender, StartTestCaseParams):
    try:
        Log.Message(f"Starting test case: {StartTestCaseParams.Name}")
        # Create an instance of the ApplicationManager
        app_manager = AppHandler.ApplicationManager()
        
        # Force close any running instances to start fresh
        #if Aliases.Orders.Exists:
        app_manager.force_shutdown()
        
        # Launch the application
        app_manager.open_application()
        Log.Message("Application launched successfully.")
    except Exception as e:
        Log.Warning(f"Failed to launch application at start of test case: {str(e)}")
        #raise

def OrdersAppEvents_OnStopTestCase(Sender, StopTestCaseParams):
    try:
        Log.Message(f"Stopping test case: {StopTestCaseParams.Name}")
        # Create an instance of the ApplicationManager
        app_manager = AppHandler.ApplicationManager()
        
        # Close the application
        app_manager.close_application()
        Log.Message("Application closed successfully.")
    except Exception as e:
        Log.Warning(f"Failed to close application at end of test case: {str(e)}")
        #raise
