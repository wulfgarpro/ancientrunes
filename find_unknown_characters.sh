#!/bin/bash
set -x
first=true
last_processed=""
for file in $(find -name "*.png");
do
    if $first; then
        python3 find_img_match.py "$file"
        last_processed="$file"
        first=false
    else
        python3 find_img_match.py "$file" "res_$(echo ${last_processed:2}).jpg"
        last_processed="$file"
    fi
done
