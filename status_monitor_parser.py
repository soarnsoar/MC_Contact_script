#HIG-RunIIFall18wmLHEGS-01330
#<tr><td class=lpc>Number of events requested</td><td class=lpc>200,000</td></tr>
#<tr><td class=lpc>Number of events produced</td><td class=lpc>0 (0.0%)</td></tr>
#


#Primary output
#Days since request approval
import os
import copy

class row_info:
    def __init__(self,name,word_flag="class=lpc>"):
        self.name=name
        self.word_flag=word_flag
        self.value=""
        
class status_monitor_parser:
        
    suffix_remove=["</td></tr>","href='","'"]
    
    
    def __init__(self,prepid ):
        #mcm_status="NONE"
        #production_status="NONE"
        #N_request="NONE"
        #N_produced="NONE"
        #primary_output=""
        #day_since_approval=""
        self.dataset="NEED DATASETNAME"
        self.mcm="https://cms-pdmv.cern.ch/mcm/requests?prepid="+prepid
        self.prepid=prepid
        self.row_info_list=[]
        self.row_info_list=copy.deepcopy(self.row_info_list)
        self.url_workflow = "https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+self.prepid
    def search_by_flag(self,line,name,line_flag, word_flag):
        value=False
        if line_flag in line:
            line_elements = line.split()
            #print line_elements
            for word in line_elements:
                if word_flag in word and not(name in word):
                    value=word.replace(word_flag,"")






                    for suffix in self.suffix_remove:                                                                                           
                        value=value.replace(suffix,"")
                    value_split=value.split(">")
                    if line_flag=="Primary output": ##To find datasetname
                        this_dataset=value_split[1]
                        this_dataset=this_dataset.split("/")[1]
                        self.dataset=this_dataset
                        
                    value=value_split[0]
                    
        return value
        
    def parse_html(self):
        
        #url = "https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+campaign+step+"-"+str(request_id)
        
        temp_file="_status_html_temp.txt"
        os.system("rm "+temp_file+" 2> /dev/null")
        os.system("wget -q "+str(self.url_workflow)+" -O "+temp_file  )
        
        f = open(temp_file,'r')
        #print "@readlines"
        lines=f.readlines()
        #print "@for all line"

        for line in lines:
            
            for row in self.row_info_list:
                value=self.search_by_flag(line,row.name,row.name,row.word_flag)
                if value :
                    row.value=value
                    #print "value="+row.value
                    break
        os.system("rm "+temp_file)


