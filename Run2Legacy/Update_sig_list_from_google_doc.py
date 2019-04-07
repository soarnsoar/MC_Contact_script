print "@@@Updating signal list from@@@"
print 'https://docs.google.com/spreadsheets/d/1BG4BaHfPBDlYOVi-BW63sQwdS5WQ2ggZv2HWkIk29oU/edit#gid=986135503'
print ' '
import os
#https://docs.google.com/spreadsheets/d/1BG4BaHfPBDlYOVi-BW63sQwdS5WQ2ggZv2HWkIk29oU/edit#gid=986135503
KEY="1BG4BaHfPBDlYOVi-BW63sQwdS5WQ2ggZv2HWkIk29oU"

##Key:Value = sheet_name:Name_for_txt 
list_sheet={
    "ggH(2l2v)":"GluGluHToWWTo2L2Nu",\
    "VBFH(2l2v)":"VBFHToWWTo2L2Nu",\
    "ggH(lnuqq)":"GluGluHToWWToLNuQQ",\
    "VBF(lnuqq)":"VBFHToWWToLNuQQ",\
    "VH":"VH",\
    "Other sig":"Other_sig",\
    "Interference":"Interference"
}




list_YEARFORMAT_RANGE={
    "2016MiniAODv3":"B3:B1000",\
    "2016NanoAODv4":"C3:C1000",\
    "2017MiniAODv2":"D3:D1000",\
    "2017NanoAODv4":"E3:E1000",\
    "2018MiniAOD":"F3:F1000",\
    "2018NanoAODv4":"G3:G1000",
    }

list_YEAR={ '2016', '2017', '2018'   }
print "==Clean list directory=="
for year in list_YEAR:
    os.system('rm -rf '+year+'/Signal/request_list')
    os.system('rm -rf  '+year+'/Interference/request_list')
for year_format, cell_range in list_YEARFORMAT_RANGE.items():
    for sheet, process in list_sheet.items():


        filename=process+'_'+year_format+'.txt'
        download_url='"https://docs.google.com/spreadsheets/d/'+KEY+'/gviz/tq?tqx=out:csv&sheet='+sheet+'&range='+cell_range+'"'
        print "==Download : "+filename+"=="
        os.system('wget -q -O '+filename+" "+download_url)


        for year in list_YEAR:
            os.system('mkdir -p '+year+'/Signal/request_list')
            os.system('mkdir -p '+year+'/Interference/request_list')
            if (year in year_format) and (not 'Interference' in process):
                os.system('mv '+filename+' '+year+'/Signal/request_list/')
                #/var/www/html/USER/jhchoi/HWW/request_monitor/MC_Contact_script_190405/Run2Legacy/2016/Signal/request_list
            elif (year in year_format) and ('Interference' in process):
                os.system('mv '+filename+' '+year+'/Interference/request_list/')
    


