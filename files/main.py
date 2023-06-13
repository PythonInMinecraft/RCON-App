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
try:
    from threading import Thread
except ModuleNotFoundError:
    installer.install("threading")
    from threading import Thread
try:
    from time import *
except ModuleNotFoundError:
    installer.install("time")
    from time import *


import interract.service as serv

service = serv.Interface()