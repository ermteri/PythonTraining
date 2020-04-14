#!/usr/bin/env python3

import simplekml
from geo_data import GeoData


gd = GeoData()

try:
    lat, lon, when = gd.get_coordinates('bild1.jpg')
except Exception as e:
    print("No GPS data in bild1.jpg")
coords = [(lon, lat)]

kml = simplekml.Kml()
path = kml.addfile("bild1.jpg")
description = '<img src="bild1.jpg" alt="picture" width="400" height=˓→"300" align="left" />'
kml.newpoint(name='test', description=description, coords=coords)
kml.savekmz('kalle.kmz')
