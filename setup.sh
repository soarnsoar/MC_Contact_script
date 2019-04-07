export _JHCHOI_REQUEST_MONITOR=`pwd`


#####Update list####

###Update Signal?##
while [ 1 ];do


    echo -e "Update Run2Legacy signal list from the google doc??[y/n]: \c "
    read sig
    sigans=0
    if [ "$sig" = "y" ]; then
	sig=1
	sigans=1
		
    elif [ "$sig" = "n" ]; then
	sig=0
	sigans=1
    
    else
    echo "Please answer y OR n"
    
    fi

    if [ $sigans -eq 1 ];then
	break
    fi

done
###Update BKG?###
while [ 1 ];do


    echo -e "Update Run2Legacy bkg list from google doc??[y/n]: \c "
    read bkg
    bkgans=0
    if [ "$bkg" = "y" ]; then
        bkg=1
        bkgans=1

    elif [ "$bkg" = "n" ]; then
        bkg=0
        bkgans=1

    else
    echo "Please answer y OR n"

    fi

    if [ $bkgans -eq 1 ];then
        break
    fi

done

##########

if [ $sig -eq 1 ];then
    
    pushd $_JHCHOI_REQUEST_MONITOR/Run2Legacy
    python Update_sig_list_from_google_doc.py
    popd
fi

if [ $bkg -eq 1 ];then

    pushd $_JHCHOI_REQUEST_MONITOR/Run2Legacy
    python Update_bkg_list_from_google_doc.py
    popd
fi
