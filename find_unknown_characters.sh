#!/bin/bash
set -x
first=true
last_processed=""
for file in $(find characters -name "*.png");
do
    if $first; then
        python3 find_img_match.py "$file"
        last_processed="$file"
        first=false
    else
        echo "here"
        python3 find_img_match.py "$file" "res_$last_processed.jpg"
        last_processed="$file"
    fi
done
