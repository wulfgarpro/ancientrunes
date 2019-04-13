#!/bin/bash

STATS="statistics.out"
/bin/rm "$STATS"

for file in $(find glyphs/ -name "*.png");
do
    /usr/bin/python3 find_img_match.py "$file" --threshold=0.95 --record_stats=True
done

TOTAL=$(awk '{sum += $2} END {print sum}' "$STATS")
echo -e "\n" >> "$STATS"
# TODO: how to use stats variable, which has a ., in awk
#/usr/bin/awk -v TOTAL="$TOTAL" STATS="$STATS" {'print $1"\t"$2 / TOTAL * 100 >> "STATS"'} "$STATS"
/usr/bin/awk -v TOTAL="$TOTAL" {'print $1"\t"$2 / TOTAL * 100 >> "statistics.out"'} "$STATS"
echo "See statistics.out"

# TODO: order results
# TODO: match results with known english frequencies
# TODO: use unknown script to find and assign frequencies to match dict

