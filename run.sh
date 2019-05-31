#! /bin/bash

rm -rf work/*

luser=${LTI_LINKY_USER?"No Linky username specified"}
lpass=${LTI_LINKY_PASS?"No Linky password specified"}
iurl=${LTI_IDB_URL?"No InfluxDB URL specified"}
idb=${LTI_IDB_DB?"No database specified"}
iloc=${LTI_IDB_LOC?"No localisation specified"}

python3 linkyCrawler.py -u $luser -p $lpass > work/data.json
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi

python3 jsonToLineProtocol.py -s work/data.json -l $iloc > work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi

./pusher -t 30s -u $iurl -d $idb -f work/data.txt
#cat work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi
