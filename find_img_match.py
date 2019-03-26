#!/usr/bin/env python3

import os
import cv2
import numpy as np

IMG_CONTAINER = "AncientRunes.jpg"

MATCH_TEST = {
    '1': 'A',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': 'T',
    '8': 'E',
    '9': '',
    '10': 'D',
    '12': 'I',
    '13': '',
    '14': '',
    '15': 'O',
    '16': '',
    '17': 'S',
    '18': '',
    '19': '',
    '20': '',
    '21': ''
}

def _do_match(template, container=IMG_CONTAINER):
    print("Matching {} in {}".format(template, container))
    match_index = template.replace(".png", "")
    match_index = match_index.replace("./", "")
    print("Index is: {}".format(match_index))
    img_container = cv2.imread(container)
    img_template = cv2.imread(template)
    h, w = img_template.shape[:-1]
    res = cv2.matchTemplate(img_container, img_template, cv2.TM_CCOEFF_NORMED)
    threshold = .95
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(img_container, pt, (pt[0] + w, pt[1] + h), (0, 0 , 255), 2) 
        cv2.putText(img_container, MATCH_TEST[match_index], (pt[0], pt[1] + h), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,255), 8)
    res_name = "res_{}.jpg".format(os.path.basename(template))
    print("Writing result to {}".format(res_name))
    cv2.imwrite(res_name, img_container) 

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        _do_match(sys.argv[1], sys.argv[2])
    else:
        _do_match(sys.argv[1])

