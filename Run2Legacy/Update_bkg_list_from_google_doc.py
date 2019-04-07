print "@@@Updating background list from@@@"

print 'https://docs.google.com/spreadsheets/d/1mf0az7nGkZviCJ9s6azYNlp8SDcNtSpWbfRYhEwYssY/edit#gid=499447744'
print ' '
import os
#https://docs.google.com/spreadsheets/d/1mf0az7nGkZviCJ9s6azYNlp8SDcNtSpWbfRYhEwYssY/edit#gid=499447744


KEY="1mf0az7nGkZviCJ9s6azYNlp8SDcNtSpWbfRYhEwYssY"

##Key:Value = sheet_name:Name_for_txt 
list_sheet={
    "DY(NLO)":"DY_NLO",\
    "DY(LO)":"DY_LO",\
    "SingleTop":"SingleTop",\
    "TT":"TT",\
    "WJets":"WJets",\
    "Multi boson":"Multi_boson",\
    "QCD":"QCD",\
    "tZq":"tZq"
}




list_YEARFORMAT_RANGE={
   
    "2016NanoAODv4":"B4:B1000",\
   
    "2017NanoAODv4":"D4:D1000",\
   
    "2018NanoAODv4":"F3:F1000",
    }

list_YEAR={ '2016', '2017', '2018'   }

for year in list_YEAR:
    os.system('rm -rf '+year+'/BKG/request_list')
 


for year_format, cell_range in list_YEARFORMAT_RANGE.items():
    for sheet, process in list_sheet.items():


        filename=process+'_'+year_format+'.txt'
        download_url='"https://docs.google.com/spreadsheets/d/'+KEY+'/gviz/tq?tqx=out:csv&sheet='+sheet+'&range='+cell_range+'"'
        print "==Download : "+filename+"=="
        os.system('wget -q -O '+filename+" "+download_url)


        for year in list_YEAR:
            if (year in year_format):
                os.system('mkdir -p '+year+'/BKG/request_list')

                #print "=="+'mv '+filename+' '+year+'/BKG/request_list/'+filename+"=="
                os.system('mv '+filename+' '+year+'/BKG/request_list/'+filename)
    


