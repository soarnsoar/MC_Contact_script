while [ 1 ];do

    #python run.py 
    python Update_bkg_list_from_google_doc.py
    python Update_sig_list_from_google_doc.py

    sleep 3600

done
