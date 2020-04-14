#!/usr/bin/env python3

import simplekml
from geo_data import GeoData

from pathlib import Path
result = list(Path("/Users/torsteneriksson/Downloads/bilder/").rglob("*.[jJ][pP][gG]"))
# result = list(Path("/Users/torsteneriksson/onedrive/Pictures/").rglob("*.[jJ][pP][gG]"))


gd = GeoData()

for year in ['2015', '2016', '2017', '2018', '2019', '2020']:
    kml = simplekml.Kml()
    points = dict()
    for image_file in result:
        try:
            lat, lon, when = gd.get_coordinates(image_file)
            if year in when:
                points[when] = [lat, lon, image_file]
        except Exception as e:
            pass # print("No GPS data in {}".format(image_file))
    keys = sorted(points)
    i = 0
    for key in keys:
        i = i + 1
        coords = [(points[key][1], points[key][0])]
        img_file = points[key][2]
        description = '<style type=“text/css”>#image {image-orientation: from-image;</style><img src="' + str(img_file) + '" alt="' + key + \
                      '" width="400" height=˓→"300" align="left" />'
        kml.newpoint(name=str(i), description=description, coords=coords)
        print('Added {}'.format(image_file))
    kml.savekmz('{}.kmz'.format(year))