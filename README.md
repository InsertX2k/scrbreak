# scrbreak
scrbreak (pronounced Screen Break) is a Windows tool that works as a Timer to remind you to take a break from your screen every 30 minutes or a predefined number of minutes
# Introduction
It is a no secret that no matter how many filters you have on your PC's screen or how many awards your monitor won in eye care, You will still need to take a break from your PC's display every predefined amount of minutes to help protect your eyes and prevent sleeplessness.

Since no piece of software can move you away from your PC, this tool does its job by reminding you to take frequent breaks every predefined number of minutes (usually 30 minutes).

# How does it really work?
It works as a Timer to remind you every 30 minutes (or a predefined number of minutes via command line usage) to take a break of your screen to save your eyesight and help you get better sleep at night. 

# Command Line usage
```bat
scrbreak.exe <Session Minutes>
```
`<Session Minutes>` - Is the number of minutes this program will show you a reminder every. (default value is **30**)

# Downloading scrbreak
[Downloads are available here](https://github.com/InsertX2k/scrbreak/releases/latest)

# FAQ (Frequently Asked Questions)
* **Q:** I started this program and I can't find any buttons to stop it/How do I stop the timer of this program?

  **A:** To stop this program you will need to do that manually via task manager or `taskkill` command (the `taskkill` command is prefered)

  ```bat
  taskkill /f /im scrbreak.exe
  ```
  
* **Q:** This program doesn't start automatically with windows/I need it to start automatically when I turn my PC on.
  
  **A:** You will need to create a shortcut to this program's executable and place it in your **Startup** folder.
  
  * Open **Run** (<kbd>Win</kbd>+<kbd>R</kbd>)
  * Type the following path.
  
  ```
  shell:startup
  ```
  
  * Press **OK** or <kbd>Enter</kbd>
  * Move the shortcut you recently created to this folder.
  
  (There are also more advanced ways to achieve that, but I won't be covering them all, because that would make this a very long document)

# Features
* Free and Open-Source
* Written in Python 3
* Highly customizable
* Supports command line (CLI) mode

# Building scrbreak from source
## 1-Preparing your workstation
Building **scrbreak** requires you to have all of the following dependencies installed on your computer:
* [pillow (PIL)](https://pypi.org/project/Pillow/)
* [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
* [awesometkinter](https://pypi.org/project/AwesomeTkinter/)
* [win10toast](https://pypi.org/project/win10toast/)

You will also need to install a compiler (like **pyinstaller**) to compile these python files into a single Windows executable.
* [Pyinstaller](https://pyinstaller.org/en/stable/installation.html)

You may need an IDE to make your changes to source files.
* [Visual Studio Code](https://code.visualstudio.com/)

## 2-Obtaining source files
You will need to have source files of **scrbreak** locally available in your PC so you can begin to compile them, You will need to have [git](https://git-scm.com/) installed.

```bat
mkdir working-dir
cd working-dir
git clone https://github.com/insertx2k/scrbreak
```

## 3-Testing source files
You will need to test the provided source files to make sure that you don't need to make your own changes, This step is required and doesn't need an explaination.

## 4-Compiling source files
This guide is for compiling source files using **pyinstaller**, Other compilers aren't covered by this guide.

```bat
pyinstaller --distpath "scrbreak_x64_distpath" --workpath "scrbreak_x64_workpath" --clean --onefile --add-data "working-dir\scrbreak\core\icon0.ico";"/core" --add-data "<python-installation-dir>\Lib\site-packages\customtkinter";"/customtkinter" --hidden-import core.windows --hidden-import core.notification --hidden-import time --hidden-import sys --hidden-import os --hidden-import core --hidden-import win10toast --hidden-import customtkinter --hidden-import awesometkinter --hidden-import six --hidden-import appdirs --hidden-import packaging.requirements --windowed -i "working-dir\scrbreak\core\icon0.ico" --name "scrbreak" --runtime-tmpdir "%localappdata%\scrbreak_temp" working-dir\scrbreak\main.py
```

Be sure to replace all of the following:
* `<python-installation-dir>` - With the directory where Python is installed in.


