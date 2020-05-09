# shutting down computer with python
import os
import platform

if platform.system() == "windows":
    os.system("shutdown -s -t 0")
else:
    os.system("shutdown -h now")
