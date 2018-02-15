import sys
import os

if sys.version_info[0] >=3:
    os.system("python python_3/pybench.py")
else:
    os.system("python python_2/pybench.py")
