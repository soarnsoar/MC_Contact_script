ARR_YEARS=( 2016 2017 2018  )
for year in ${ARR_YEARS[@]};do

    mkdir -p Run2Legacy/${year}/Signal/
    mkdir -p Run2Legacy/${year}/BKG/
    cp run_tmp.py Run2Legacy/${year}/Signal/run.py
    cp run_tmp.py Run2Legacy/${year}/BKG//run.py

done
