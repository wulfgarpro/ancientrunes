#!/bin/bash

first=true
last_processed=""

for file in $(find glyphs/ -name "*.png");
do
    if $first; then
        /usr/bin/python3 find_img_match.py "$file" --with_text=True --threshold=0.95
        if [ $? -ne 1 ]; then
            last_processed="${file//glyphs\//''}"
            first=false
        fi
    else
        /usr/bin/python3 find_img_match.py "$file" --container="res_$(echo ${last_processed}).jpg" --with_text=True --threshold=0.95
        if [ $? -ne 1 ]; then
            last_processed="${file//glyphs\//''}"
        fi
    fi
done
/bin/cp -v res_$(echo ${last_processed}).jpg solution.jpg

