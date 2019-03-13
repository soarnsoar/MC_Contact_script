#from status_monitor_parser import status_monitor_parser
#https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_HIG-RunIIFall18wmLHEGS-01328

from status_monitor_parser import *

info_list=[ row_info("McM status"), \
            row_info("Production status"), \
            row_info("Number of events requested"),\
            row_info("Number of events produced"),\
            row_info("Primary output","href="), \
            row_info("Days since request approval")\
]



prepid="HIG-RunIIFall18wmLHEGS-01330"
my_request=status_monitor_parser(prepid)
my_request.row_info_list=info_list


my_request.parse_html()
#for info in my_request.row_info_list:
#    print "@@"
#    print info.name
#    print info.value





from html_maker import *
my_html=jh_html()
my_html.title="test title"
my_html.tabs.append("Prep.id")
my_html.tabs.append("dataset")
my_html.tabs.append("McM")
for info in info_list:
    #my_html.tabs=["1st","2nd","3rd"]
    my_html.tabs.append(info.name)


this_data=[]
this_data.append(my_request.prepid)
this_data.append(my_request.dataset)
this_data.append(my_request.mcm)
for info in my_request.row_info_list:
    #my_html.add_data(["a","b","c"])
    #my_html.add_data
    this_data.append(info.value)
my_html.add_data(this_data)
my_html.make()
