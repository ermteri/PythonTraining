#!/usr/bin/env python3
import webbrowser
import argparse
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


class GeoData:
    def __init__(self):
        pass

    def get_exif(self, filename):
        image = Image.open(filename)
        image.verify()
        return image._getexif()

    def get_geotagging(self, exif):
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
            if tag == 'DateTimeOriginal':
                date = exif[idx]

        return geotagging, date

    def get_decimal_from_dms(self, dms, ref):

        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, 5)

    def get_coordinates(self, image_file):
        exif = self.get_exif(image_file)
        geotags, date = self.get_geotagging(exif)
        lat = self.get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

        lon = self.get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

        return lat, lon, date


def run(argv):
    parser = argparse.ArgumentParser(description='Show image on map.')
    parser.add_argument('-f','--file', type=str, help='The image file', required=True)
    args = parser.parse_args()
    try:
        gd = GeoData()
        lat, lon = gd.get_coordinates(args.file)
        url = ' https://www.google.com/maps/search/?api=1&query={},{}'.format(lat, lon)
        print(url)
        browser = webbrowser.get('chrome')
        browser.open(url, new=0, autoraise=True)
    except ValueError as e:
        print('No GPS data in {} ({})'.format(args.file, e))


if __name__ == '__main__':
    run(sys.argv)
