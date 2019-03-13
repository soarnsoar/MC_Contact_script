
#<tr><td class=lpc>Number of events requested</td><td class=lpc>200,000</td></tr>
#<tr><td class=lpc>Number of events produced</td><td class=lpc>0 (0.0%)</td></tr>
#


#Primary output
#Days since request approval
import os







    

def status_monitor_parser(campaign,step,request_id):
    
    url = "https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_"+campaign+step+"-"+str(request_id)

    mcm_status_flag="McM status"
    mcm_status_word_flag="class=lpc>"
    
    production_status_flag="Production status"
    production_status_word_flag="class=lpc>"
    
    N_request_flag="Number of events requested<"
    N_request_word_flag="class=lpc>"

    N_produced_flag="Number of events produced"
    N_produced_word_flag="class=lpc>"



    
    temp_file="_status_monitor_temp.txt"
    os.system("rm "+temp_file+" 2> /dev/null")
    os.system("wget -q "+str(url)+" -O "+temp_file  )
    
    f = open("status.txt",'r')
    mcm_status="NONE"
    production_status="NONE"
    #print "@readlines"
    lines=f.readlines()
    #print "@for all line"
    for line in lines:
        if mcm_status_flag in line:
            line_elements = line.split()
            #print line_elements
            for word in line_elements:
                if mcm_status_word_flag in word and not("McM" in word):
                    mcm_status=word.replace(mcm_status_word_flag,"")
                    mcm_status=mcm_status("</td></tr>","")
        if production_status_flag in line:
            line_elements=line.split()
            #print line_elements
            for word in line_elements:
                if production_status_word_flag in word and not("Production" in word):
                    production_status=word.replace(production_status_word_flag,"")
                    production_status=production_status.replace("</td></tr>","")
                    
    os.system("rm "+temp_file)
    print "mcm_status="+mcm_status
    print "production_status="+production_status

                                                                                                                                                                                                                                                                                
