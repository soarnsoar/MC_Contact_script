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

1)go to Make_McM_monitor_html.py file

2)In the file, find if __name__ == __main__

3) change the line like below
Make_McM_monitor_html( TITLE_OF_HTML_PAGE, TXT_file_Location  )
e.g.)
Make_McM_monitor_html("Autumn18_MC_HWW", "request_list/Autumn18_HWW.txt")

4) run the script
python Make_McM_monitor_html.py

then you can get Autumn18_MC_HWW.html

5)move the html output to your webserver.



6)By running the script every 10min, you can update the status of requests.

