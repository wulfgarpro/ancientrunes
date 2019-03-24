#!/usr/bin/env python

import os
import cv2
import numpy as np

IMG_CONTAINER = "AncientRunes.jpg"

def _do_match(template, container=IMG_CONTAINER):
    print("Matching {} in {}".format(template, IMG_CONTAINER))
    img_container = cv2.imread(container)
    img_template = cv2.imread(template)
    h, w = img_template.shape[:-1]
    res = cv2.matchTemplate(img_container, img_template, cv2.TM_CCOEFF_NORMED)
    threshold = .9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_container, pt, (pt[0] + w, pt[1] + h), (0, 0 , 255), 2) 
    res_name = "res_{}.jpg".format(os.path.basename(template))
    print("Writing result to {}".format(res_name))
    cv2.imwrite(res_name, img_container) 

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        _do_match(sys.argv[1], sys.argv[2])
    else:
        _do_match(sys.argv[1])

