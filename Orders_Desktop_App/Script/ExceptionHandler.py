import functools
import AppHandler

def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            Log.Error(f"Error occurred in {func.__name__}: {str(e)}")
            app_handler = AppHandler.ApplicationManager()
            app_handler.force_shutdown()
            Delay(3000)
            app_handler.open_application()
            raise
    return wrapper