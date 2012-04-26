# OSM Jalisco

Public geo data for Jalisco prepared by MapBox, ready for contribution to OSM. Check out our [public issue tracker](https://github.com/mapbox/mapping) to join the OSM mapping party and for more information about how to contribute.

## Accessing the data

All ````.osm```` files and ````.py```` translation scripts can be found in this repo by clicking on the ````Downloads```` tab and navigating to the appropriate file. They are also available as a ````.zip```` file by clicking on the ````Download as zip```` tab.

## Using the data

````.osm```` files can be imported into OpenStreetMap's open source desktop editor [JOSM](http://josm.openstreetmap.de/) but cannot be uploaded directly to OSM. This data is simply intended to serve as a resource to enourage and help guide users accurately map this region on their own. If you are new to OSM, check out our post about [tracing satellite imagery in OSM](http://mapbox.com/blog/satellite-tracing-osm/) on the MapBox blog to get started.

## Sourcing the data

All geo data was obtained in shapefile format from the Instituto de Informacion Territorial del Estado de Jalisco ([SITEL](http://sitel.jalisco.gob.mx/index2.php)) website. We wrote the python scripts to translate each file's metadata into appropriate OSM tagging, using [ogr2osm](http://wiki.openstreetmap.org/wiki/Ogr2osm).

