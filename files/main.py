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
    import tkinter as tk
except ModuleNotFoundError:
    installer.install("tkinter")
    import tkinter as tk
try:
    from mcrcon import MCRcon
except ModuleNotFoundError:
    installer.install("mcrcon")
    from mcrcon import MCRcon

