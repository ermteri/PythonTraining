#!/usr/bin/env python3

import argparse
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled


def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
        if tag == 'Image DateTime':
            date = exif[tag]

    return geotagging, date


def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)


def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return lat, lon


def run(args):
    parser = argparse.ArgumentParser(description='Show image on map.')
    parser.add_argument('-f','--file', type=str, help='The image file', required=True)
    args = parser.parse_args()
    exif = get_exif(args.file)
    try:
        labeled = get_labeled_exif(exif)
        for label in labeled:
            print(label, exif[label])
    except ValueError as e:
        print('Failed to read exif in {} due to {}'.format(args.file, e))


if __name__ == '__main__':
    run(sys.argv)
