#!/bin/bash
#set -x
first=true
last_processed=""
for file in $(find -name "*.png");
do
    if $first; then
        python3 find_img_match.py "$file"
        exit_status=$?
        if [ ${exit_status} -ne 1 ]; then
            last_processed="$file"
            first=false
        fi
    else
        python3 find_img_match.py "$file" "res_$(echo ${last_processed:2}).jpg"
        exit_status=$?
        if [ ${exit_status} -ne 1 ]; then
            last_processed="$file"
        fi
    fi
done
#python3 find_img_match.py "$file" "res_$(echo ${last_processed:2}).jpg"
