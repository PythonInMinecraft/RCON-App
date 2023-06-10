"""Main file for the project"""

#Internal imports
import builder.lib_installer as inst

installer = inst.LibInstaller()

#Externals exports
try:
    import os
except ModuleNotFoundError:
    raise RuntimeError
try:
    import tkinter
except ModuleNotFoundError:
    installer.install("tkinter")