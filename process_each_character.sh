#!/bin/bash
for file in $(find -name "*.png");
do
    python3 find_img_match.py $file
done
