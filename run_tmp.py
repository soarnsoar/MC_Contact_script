import sys
import os
WORKDIR=os.environ["_JHCHOI_REQUEST_MONITOR"]
#sys.path.append('/var/www/html/USER/jhchoi/HWW/request_monitor/MC_Contact_script/')
sys.path.append(WORKDIR+"/python")

from Make_McM_monitor_html import *

Make_McM_monitor_html("test", "request_list/2016_Legacy_HWW.txt")


