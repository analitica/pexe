@echo off
"%programFiles%\git\bin\git.exe" pull origin master
cd c:\pexe\pexe
c:\python27\python.exe pexe.py
