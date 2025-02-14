def WebEvents_OnStartTestCase(Sender, StartTestCaseParams):
    Browsers.Item[btEdge].Navigate(Project.Variables.URL)
    browser = Aliases.browser
    browser.BrowserWindow.Maximize()

def WebEvents_OnStopTestCase(Sender, StopTestCaseParams):
    browser = Aliases.browser
    browser.Close()
