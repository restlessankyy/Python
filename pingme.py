import os
from datetime import *
print os.stat("ippy.py")
print datetime.fromtimestamp(os.stat('ippy.py').st_mtime)
