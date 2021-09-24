# Note that this code is not mine.
# Credit: https://cx-freeze.readthedocs.io/en/latest/setup_script.html

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {'packages' : ["os"], 'includes' : ["tkinter", "youtube_dl"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Youtube Video Downloader",
    version = "1.0",
    description = """Created by Braden Franklin""",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, shortcutName="Youtube Video Downloader",
            shortcutDir="DesktopFolder")]
)