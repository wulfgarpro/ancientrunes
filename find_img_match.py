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
    '11': 'I',
    '12': 'C',
    '13': 'H',
    '14': 'O',
    '15': 'F',
    '16': 'S',
    '17': 'Y',
    '18': 'L',
    '19': 'V',
    '20': 'W',
    '21': 'T'
}


def _do_match(template, **kwargs):
    container=IMG_CONTAINER
    with_text=False
    threshold=0.9
    if 'container' in kwargs and kwargs['container'] is not None:
        container = kwargs['container']
    if 'with_text' in kwargs and kwargs['with_text'] is not None:
        with_text = kwargs['with_text']
    if 'threshold' in kwargs and kwargs['threshold'] is not None:
        threshold = kwargs['threshold']
    match_index = template.replace(".png", "")
    match_index = match_index.replace("./", "")
    match_index = match_index.replace("characters/", "")
    if MATCH_TEST[match_index] == '':
        print("Skipping {}, no guess".format(match_index))
        sys.exit(1)
    print("Matching {} in {}".format(template, container))
    print("Index is: {}".format(match_index))
    img_container = cv2.imread(container)
    img_template = cv2.imread(template)
    height, width = img_template.shape[:-1]
    res = cv2.matchTemplate(img_container, img_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for point in zip(*loc[::-1]):
        if with_text:
            cv2.putText(img_container, MATCH_TEST[match_index], (
                point[0], point[1] + height), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 240), 8)
        else:
            cv2.rectangle(img_container, point,
                          (point[0] + width, point[1] + height), (0, 0, 255), 2)
    res_name = "res_{}.jpg".format(os.path.basename(template))
    print("Writing result to {}".format(res_name))
    cv2.imwrite(res_name, img_container)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("template", type=str, help="The template to match.")
    parser.add_argument("--container", dest="container", type=str, help="The container to search.")
    parser.add_argument("--with_text", dest="with_text", type=bool, default=False, help="Match guessed characters and put text.")
    parser.add_argument("--threshold", dest="threshold", type=float, default=0.9, help="Fine tune match threshold.")
    args = parser.parse_args()
    _do_match(args.template, container=args.container, with_text=args.with_text, threshold=args.threshold)

