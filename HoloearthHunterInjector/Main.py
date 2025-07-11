import pyMeow as pm
import os.path as xzs
from os import _exit as exitfunc
def Main():
    process = pm.open_process("Holoearth.exe")
    if(xzs.isfile("HoloearthHunter.dll")):
        print("This DLL Cheeto Is Existed... Injecting, Please Wait...")
        pm.inject_library(process, "Holoearth.dll")
        print("Injected!!!")
        exitfunc(43)
    else:
        print("This Cheeto is WIP!!! Please wait Until This Cheeto will be done and compiled!!!")
        exitfunc(21)

if __name__ == "__main__":
    Main()