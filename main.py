from core.windows import *
from core.notification import *
from time import sleep
# imports necessary to get the path where the files are extracted in
import os
import sys

# initializing a variable containing the path where application files are stored.
application_path = ''

# attempting to get where the program files are stored
if getattr(sys, 'frozen', False): 
    # if program was frozen (compiled) using pyinstaller, the pyinstaller bootloader creates a sys attribute
    # frozen=True to indicate that the script file was compiled using pyinstaller, then it creates a
    # constant in sys that points to the directory where program executable is (where program files are extracted in).
    application_path = sys._MEIPASS
else: 
    # if program is not frozen (compiled) using pyinstaller and is running normally like a Python 3.x.x file.
    application_path = os.path.dirname(os.path.abspath(__file__))

# changing the current working directory to the path where one-file mode source files are extracted in.
os.chdir(application_path)


def main(SessionMinutes: int):
    minutesToSleep = (SessionMinutes * 60)
    while True:
        sleep(minutesToSleep)
        showWinToast("Take a break", f"You've been looking at the screen continuously for {SessionMinutes} minutes, Please take a break for 5 minutes or more", toastDuration=25, isThreaded=True, iconPath=f"{application_path}\\core\\icon0.ico")
        RestWindow(SessionMinutes).mainloop()
        



if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            main(30)
            raise SystemExit(0)
        except KeyboardInterrupt:
            pass
    elif len(sys.argv) == 2:
        try:
            minutesForSession = int(sys.argv[1])
            main(minutesForSession)
            raise SystemExit(0)
        except TypeError:
            print(f"error: {sys.argv[1]} couldn't be converted to data type: int")
            print("command line usage is: minutesForSession: int - Show the notification every x minutes")
            raise SystemExit(5)
        except KeyboardInterrupt:
            pass
    else:
        print("command line usage is: minutesForSession: int - Show the notification every x minutes")
        raise SystemExit(6)
        
