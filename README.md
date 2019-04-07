!!Please note that this code is not that fast.... It take 1sec per 1 request to monitor it LOL!!

How to Use

0) Make txt file containing request list 
e.g.)
> cat request_list/Autumn18_HWW.txt
HIG-RunIIFall18wmLHEGS-00855
HIG-RunIIFall18wmLHEGS-00854
HIG-RunIIFall18wmLHEGS-00574
HIG-RunIIFall18wmLHEGS-00856
HIG-RunIIFall18wmLHEGS-00857

1)cp run_tmp.py and open the new file



2) change the line like below
Make_McM_monitor_html( TITLE_OF_HTML_PAGE, TXT_file_Location  )
e.g.)
Make_McM_monitor_html("Autumn18_MC_HWW", "request_list/Autumn18_HWW.txt")

3) run the script
python <your_new_file>.py

then you can get Autumn18_MC_HWW.html

4)move the html output to your webserver.





