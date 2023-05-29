"""
core module for spawning a notification window indicating that user has been looking at screen for so long
"""
# imports
from tkinter import *
from tkinter import scrolledtext, messagebox
from customtkinter import *
from awesometkinter import DEFAULT_COLOR
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


class RestWindow(Tk):
    def __init__(self, sessionMinutes):
        self.sessionMinutes = sessionMinutes
        super().__init__()
        # customtkinter related configuration.
        deactivate_automatic_dpi_awareness() # for hidpi displays
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        # ------------------------------------

        self.title("ScreenBreak")
        # declaring the geometry of the windows in separate variables.
        wWidth = 638
        wHeight = 300
        self.geometry(f'{wWidth}x{wHeight}')
        self.minsize(wWidth, wHeight)
        self.maxsize(wWidth, wHeight)
        self.resizable(False, False)
        self.configure(bg=DEFAULT_COLOR)
        try:
            self.iconbitmap(f"{application_path}\\core\\icon0.ico")
        except Exception as errorLoadingIconBitmap:
            messagebox.showerror("Error in mainloop", f"Couldn't load iconbitmap for this window due to this error\n{errorLoadingIconBitmap}\n\nPress OK to continue")
            pass

        # defining a function to insert text into the scrolledtext widget.
        def insertInformation():
            """
            A function for inserting text into the scrolledtext widget that will show information to the user.
            """
            self.moreinfo_widget.configure(state='normal')
            self.moreinfo_widget.delete(1.0, END)
            self.moreinfo_widget.insert(END, f"""You have been looking at the computer's screen for {self.sessionMinutes} minute(s) 
continuously, it is strongly recommended that you take a break for 5 
minutes or more to save your eyesight and help you get better sleep at night.

Please take a break for 5 minutes or more then press the 'OK' button 
below to close this window and notify you again after {self.sessionMinutes} minute(s) from the 
pressing time.
""")
            self.moreinfo_widget.configure(state='disabled')
            return None


        # defining the function for the OK button
        def okBtn_Function():
            """
            OK btn function
            """
            self.destroy()
            return None
        # declaring widgets in this window.
        self.lbl0 = Label(self, bg=DEFAULT_COLOR, foreground='white', font=("Arial Bold",14), text="You need to take a break.")
        self.lbl0.place(x=15, y=7)
        self.moreinfo_widget = scrolledtext.ScrolledText(self, cursor='arrow', font=("Consolas", 11), background=DEFAULT_COLOR, foreground='white', state='disabled')
        self.moreinfo_widget.place(x=15, y=40, relwidth=0.96, relheight=0.73)
        self.ok_btn = CTkButton(self, text="OK", command=okBtn_Function)
        self.ok_btn.place(x=250, y=265)
        # let's display information to the user.
        insertInformation()





if __name__ == '__main__':
    pass