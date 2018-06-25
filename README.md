# OSM Jalisco

Public geo data for Jalisco prepared by MapBox, ready for contribution to OSM. Check out our [public issue tracker](https://github.com/mapbox/mapping) to join the OSM mapping party and for more information about how to contribute.

## Accessing the data

All ````.osm```` files and ````.py```` translation scripts can be found in this repo by clicking on the ````Downloads```` tab and navigating to the appropriate file. They are also available as a ````.zip```` file by clicking on the ````Download as zip```` tab.

## Using the data

[See instructions for using the data with Potlatch](http://www.openstreetmap.org/user/Richard/diary)

All ````.osm```` files can be imported into OpenStreetMap's open source desktop editor [JOSM](http://josm.openstreetmap.de/) but cannot be uploaded directly to OSM. This data is simply intended to serve as a resource to guide and encourage users to accurately map this region on their own.

To import the data select File, Open.

![](http://farm8.staticflickr.com/7239/7118786805_24b68e7817.jpg)

Navigate to the appropriate directory and select the file.

![](http://farm8.staticflickr.com/7261/7118786977_7d4864fc53.jpg)

Once the file has uploaded you'll want to turn on Bing satellite imagery which will serve as the base layer for all of your tracing. Select Imagery - Bing Sat to add this layer into JOSM.

![](http://farm8.staticflickr.com/7200/6972707992_e96e1b7ff3.jpg)

Zoom to the region you want to trace and download the OSM data that is already there by selecting the ````Download map data```` icon.

![](http://farm8.staticflickr.com/7049/7118786941_74b7d15488.jpg)

To start tracing add a new layer by selecting File - New Layer.

![](http://farm8.staticflickr.com/7176/6972707882_cc72cf70bd.jpg)

By default JOSM will activate the new layer, deactivating the Jalisco data layer previously imported and preventing you from viewing its properties. To reactivate this layer to refer to its tagging information select it in the layer list then select the ````Activate selected layer```` icon.

![](http://farm9.staticflickr.com/8141/6972707964_cac95da327.jpg)

Then select the appropriate road segment and its properties will appear in the window on the right.

![](http://farm8.staticflickr.com/7081/7118786871_d7b1163bfe.jpg)

Alternate between layers using the same method, and remember to only edit your own layer and not the Jalisco road data provided. If you are new to OSM, check out our post about [tracing satellite imagery](http://mapbox.com/blog/satellite-tracing-osm/) on the MapBox blog for more help getting started.

## Sourcing the data

All geo data was obtained in shapefile format from the Sistem de Informacion Territorial del Estado de Jalisco ([SITEL](http://sitel.jalisco.gob.mx/index2.php)) website and made availabe to OSM with [permission from Carlos Ruiz](https://gist.github.com/2648407/d5c5f6af02d1670ae1c839a6de0b9650997490f8). We wrote the python scripts to translate each file's metadata into appropriate OSM tagging, using [pnorman's](https://github.com/pnorman) version of [ogr2osm](http://wiki.openstreetmap.org/wiki/Ogr2osm#pnorman.27s_updated_version) to convert to ````.osm```` format with the following command:

````python ogr2osm.py /your/file/path/Camino_2011.shp -t /your/file/path/jalisco-caminos.py```` 

### PLEASE READ THE OGR2OSM DOCUMENTATION CAREFULLY AND ALERT THE COMMUNITY BEFORE RUNNING ANY SCRIPTED IMPORTS
