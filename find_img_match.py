#!/usr/bin/env python3

import os
import sys
import cv2
import numpy as np

IMG_CONTAINER = "AncientRunes.jpg"

MATCH_TEST = {
    '1': 'A',
    '2': 'B',
    '3': 'M',
    '4': 'U',
    '5': 'G',
    '6': 'P',
    '7': 'R',
    '8': 'E',
    '9': 'N',
    '10': 'D',
    '12': 'I',
    '13': 'C',
    '14': 'H',
    '15': 'O',
    '16': 'F',
    '17': 'S',
    '18': 'Y',
    '19': 'L',
    '20': 'V',
    '21': 'W',
    '22': 'T'
}

def _do_match(template, container=IMG_CONTAINER):
    match_index = template.replace(".png", "")
    match_index = match_index.replace("./", "")
    if MATCH_TEST[match_index] == '':
        print("Skipping {}, no guess".format(match_index))
        sys.exit(1)
    print("Matching {} in {}".format(template, container))
    print("Index is: {}".format(match_index))
    img_container = cv2.imread(container)
    img_template = cv2.imread(template)
    h, w = img_template.shape[:-1]
    res = cv2.matchTemplate(img_container, img_template, cv2.TM_CCOEFF_NORMED)
    threshold = .96
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(img_container, pt, (pt[0] + w, pt[1] + h), (0, 0 , 255), 2) 
        cv2.putText(img_container, MATCH_TEST[match_index], (pt[0], pt[1] + h), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0,240), 8)
    res_name = "res_{}.jpg".format(os.path.basename(template))
    print("Writing result to {}".format(res_name))
    cv2.imwrite(res_name, img_container) 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        _do_match(sys.argv[1], sys.argv[2])
    else:
        _do_match(sys.argv[1])

