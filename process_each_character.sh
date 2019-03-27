#!/bin/bash

for file in $(find -name "characters/*.png");
do
    /usr/bin/python3 find_img_match.py $file
done
