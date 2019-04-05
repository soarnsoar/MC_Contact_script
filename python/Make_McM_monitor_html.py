#from status_monitor_parser import status_monitor_parser
#https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_HIG-RunIIFall18wmLHEGS-01328
import copy
from status_monitor_parser import *
from html_maker import *


def Make_McM_monitor_html(TITLE, TXT):
    info_list=[ row_info("McM status"), \
                row_info("Production status"), \
                row_info("Number of events requested"),\
                row_info("Number of events produced"),\
                row_info("Primary output","href="), \
                row_info("Days since request approval")\
    ]





    ####Define jhhtml object####
    ##title row##
    my_html=jh_html()
    my_html.title=TITLE
    my_html.tabs.append("Prep.id")
    my_html.tabs.append("dataset")
    my_html.tabs.append("McM")
    for info in info_list:
        
        my_html.tabs.append(info.name)
        
    ####Now 1st line is defined###
    ###Fill data####
    
    f_input = open(TXT,'r') ##Load from txt
    txtlines=f_input.readlines()

    for this_request in txtlines:
        if this_request == "" : continue
        if this_request.strip().startswith( "#" ) : continue
        #prepid="HIG-RunIIFall18wmLHEGS-01330"
        print "@@ADD "+this_request
        prepid=this_request
        my_request=status_monitor_parser(prepid)
        my_request.row_info_list=copy.deepcopy(info_list)
        ntrial=0
        
        while [ ntrial < 10 ]:

            try:
                my_request.parse_html()
                break
            except:
                print "ntrial="+str(ntrial)
                ntrial+=1
            if ntrial == 10:
                print "!!!SKIP!!!   "+this_request
                break
        if ntrial == 10: continue
        
        

        this_data=[]
        this_data[:]=[]
        this_data.append(my_request.prepid)
        this_data.append(my_request.dataset)
        this_data.append(my_request.mcm)
        for info in my_request.row_info_list:
            #my_html.add_data(["a","b","c"])
            #my_html.add_data
            
            this_data.append(info.value)
        #this_data=copy.deepcopy(this_data)
        my_html.add_data(copy.deepcopy(this_data)) ## add line
        del my_request
    ###Now all of the lines are added


    
    my_html.make(TITLE+".html")##export 
    f_input.close()


