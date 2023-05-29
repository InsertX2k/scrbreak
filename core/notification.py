"""
core module for showing a windows 10 action center toaster showing that you need to take a break.
"""
from win10toast import ToastNotifier

# initializing toaster service
toasterService = ToastNotifier()

# declaring a function for showing toaster messages.
def showWinToast(title: str, content: str, toastDuration: int=2, 
                 iconPath=None, isThreaded: bool=True):
    """
    Shows a message in Windows 10's Action Center.

    This function takes 6 parameters (2 required, 4 optional)

    Parameters are: title: str, content: str, toastDuration: int, iconPath, isThreaded: bool
    """
    toasterService.show_toast(title, content, duration=toastDuration, icon_path=iconPath, threaded=isThreaded)
    return None


if __name__ == '__main__':
    # showWinToast("test", "hello world", toastDuration=40)
    # raise SystemExit(0) # for testing only
    pass