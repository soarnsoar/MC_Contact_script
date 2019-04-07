import glob
import sys
import os
from Make_McM_monitor_html import *


while 1:
###
    dir_request="request_list/"
    ###
    #        for file in glob.glob(_dir_+"/*"+self.output_format):
    
    txt_list=glob.glob(dir_request+"/*.txt")
    
    

    
    WORKDIR=os.environ["_JHCHOI_REQUEST_MONITOR"]
    
    sys.path.append(WORKDIR+"/python")
    
    
    #print txt_list
    
    
    for txt in txt_list:
        #name=txt.lstrip(dir_request)

        name=txt.split("/")[-1]
        name=name.split(".txt")[0]
        print name
        Make_McM_monitor_html(name, txt)


