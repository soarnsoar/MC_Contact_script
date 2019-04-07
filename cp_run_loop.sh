ARR_YEARS=( 2016 2017 2018  )
for year in ${ARR_YEARS[@]};do

    mkdir -p Run2Legacy/${year}/Signal/
    mkdir -p Run2Legacy/${year}/BKG/
    mkdir -p Run2Legacy/${year}/Interference/
    cp run_tmp.py Run2Legacy/${year}/Signal/run.py
    cp run_tmp.py Run2Legacy/${year}/BKG//run.py
    cp run_tmp.py Run2Legacy/${year}/Interference//run.py
    cp while_loop.sh Run2Legacy/${year}/Signal/while_loop.sh
    cp while_loop.sh Run2Legacy/${year}/BKG/while_loop.sh
    cp while_loop.sh Run2Legacy/${year}/Interference/while_loop.sh
done
