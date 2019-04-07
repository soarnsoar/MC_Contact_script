
###
dir_request="request_list/"
###
#        for file in glob.glob(_dir_+"/*"+self.output_format):
import glob
txt_list=glob.glob(dir_request+"/*.txt")



import sys
import os
WORKDIR=os.environ["_JHCHOI_REQUEST_MONITOR"]

sys.path.append(WORKDIR+"/python")

from Make_McM_monitor_html import *
#print txt_list

for txt in txt_list:
    #name=txt.lstrip(dir_request)

    name=txt.split("/")[-1]
    name=name.split(".txt")[0]
    print name
    Make_McM_monitor_html(name, txt)


