#!/bin/bash

first=true
last_processed=""

for file in $(find characters -name "*.png");
do
    if $first; then
        /usr/bin/python3 find_img_match.py "$file"
        if [ $? -ne 1 ]; then
            last_processed="${file//characters\//''}"
            first=false
        fi
    else
        /usr/bin/python3 find_img_match.py "$file" --container="res_$(echo ${last_processed}).jpg"
        if [ $? -ne 1 ]; then
            last_processed="${file//characters\//''}"
        fi
    fi
done
/bin/cp -v res_$(echo ${last_processed}).jpg known_characters.jpg

