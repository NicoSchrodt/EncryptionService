import os
import sys


# takes a relative path and return an absolute path
def resource_path(relative_path):
    try:  # only work if python project was converted to exe file
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")
    return os.path.join(base_path, relative_path)
