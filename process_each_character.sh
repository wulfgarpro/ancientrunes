#!/bin/bash
for file in $(find characters -name "*.png");
do
    python3 find_img_match.py $file
done
