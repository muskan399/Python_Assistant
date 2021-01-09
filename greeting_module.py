import os
import subprocess as sp
def close():
    sp.getoutput("pulseaudio --start")
    os.system("tput reset")
    os.system("figlet 'Thank You'")
    os.system("espeak-ng 'Thank you for using my services'")
    exit()

