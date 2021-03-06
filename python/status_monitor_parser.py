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
        self.row_info_list[:] =[]
        self.row_info_list=copy.deepcopy(self.row_info_list)
        self.url_workflow = "https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+self.prepid
        self.url_get_dictionary = "https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/"+self.prepid

    def __del__(self):
        self.dataset="NEED DATASETNAME"
        self.mcm=""
        self.prepid=""
        self.row_info_list[:]=[]
        self.url_workflow=""
        
    def search_by_flag(self,line,name,line_flag, word_flag):
        #print "@@search_by_flag,line"
        #print line
        #print "@line_flag="+line_flag
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
                        #print "@@this_dataset from Primary output@@"
                        #print value_split
                        this_dataset=value_split[1]
                        this_dataset=this_dataset.split("/")[1]
                        self.dataset=this_dataset

                    value=value_split[0]
                    
        return value
        
    def parse_html(self):
        #print "@parse_html@"
        #url = "https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+campaign+step+"-"+str(request_id)
        
        temp_file="_status_html_temp.txt"
        os.system("rm "+temp_file+" 2> /dev/null")
        
        os.system("wget -q -O "+temp_file+" "+str(self.url_workflow)  )
        #os.system("wget -O "+temp_file+" "+str(self.url_workflow)  )
        
        f = open(temp_file,'r')
        #print "@readlines"
        lines=f.readlines()
        #print "@for all line  of "+self.prepid
        #print lines
        for line in lines:
            #print "@"+line
            for row in self.row_info_list:
                value=self.search_by_flag(line,row.name,row.name,row.word_flag)
                if value :
                    row.value=value
                    #print "value="+row.value
                    break





                
        if self.dataset=="NEED DATASETNAME":
            ##From Get directory##
            print "@USE GET DIRECTORY@"
            temp_file2="_get_dir_html_temp.txt"
            os.system("rm "+temp_file2+" 2> /dev/null")
            #get_dir_url="https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/"+self.prepid
            get_dir_url=self.url_get_dictionary
            os.system("wget --no-check-certificate -q -O "+temp_file2+" "+str(get_dir_url))
            f2 = open(temp_file2,'r')
            line=f2.readlines()[-1]
            #for line in lines2:
            #print "@@@"+l
            ####Take dataset_name###
            dataset=line.split("dataset_name")[-1]
            dataset=dataset.split('"')[2]
            self.dataset=copy.deepcopy(dataset)


            '''
            ###Requested events###
            total_events=line.split("total_events")[-1]
            total_events=total_events.split('"')[1]
            total_events=total_events.strip()
            total_events=total_events.lstrip(":")
            total_events=total_events.rstrip(',')
            total_events=total_events.strip()
            #print total_events


            ###complete_events###
            completed_events=line.split("completed_events")[-1]
            completed_events=completed_events.split('"')[1]
            completed_events=completed_events.strip()
            completed_events=completed_events.lstrip(":")
            completed_events=completed_events.rstrip(',')
            completed_events=completed_events.strip()
            #            print completed_events

            '''
            ##Get its root request(1st request of the chain)###

            first_request=line.split('"pdmv_prep_id": "task_')[-1]
            first_request=first_request.split('"')[0]
            #print first_request

            #print "@@"+dataset
            #for l in dataset:
            #   print "@@"+l
            f2.close()
            ###Now we got 1st request###
            ##Status of the 1st request##
            url_1st="https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+first_request
            os.system("rm "+temp_file+" 2> /dev/null")
            os.system("wget -q -O "+temp_file+" "+str(url_1st)  )
            f = open(temp_file,'r')
            #print "@readlines"
            lines=f.readlines()
            #print "@for all line  of "+self.prepid
            #print lines
            for line in lines:
                #print "@"+line
                for row in self.row_info_list:
                    value=self.search_by_flag(line,row.name,row.name,row.word_flag)
                    if value :
                        row.value=value
                        #print "value="+row.value
                        break

            #os.system("rm "+temp_file2+" 2> /dev/null")
        
        #os.system("rm "+temp_file)
        f.close()


