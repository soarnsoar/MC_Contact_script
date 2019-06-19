YEAR=(2016 2017 2018)
DIRS=(Signal Interference BKG)



for yr in ${YEAR[@]};do

    for dir in ${DIRS[@]};do
	
	pushd ${yr}/${dir}
	source while_loop.sh &> while_loop.log&
	popd

    done

done
