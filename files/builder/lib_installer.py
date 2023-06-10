"""Installer file"""
#Externals import
import os

#Class

class LibInstaller(object):
    def install(self, lib):
        print("Installing the missing librairy...")
        os.system("pip install {0}")