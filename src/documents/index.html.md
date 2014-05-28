```
title: 'Home'
layout: default
sections:
    - 'carousel'
    - 'basemaps'
    - 'thematic-map-services'
    - 'terms-of-use'


labels:
    carousel: 'Map Viewers'
    basemaps: 'Basemaps'
    thematic-map-services: 'Thematic Map Services'
    terms-of-use: 'Terms of Use'
```

Norwegian Polar Institute Maps and Services
==========================================

<br/>
<div id="myCarousel" class="carousel slide" data-ride="carousel">
            <ul class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#myCarousel" data-slide-to="1" class></li>
                <li data-target="#myCarousel" data-slide-to="2" class></li>
                <li data-target="#myCarousel" data-slide-to="3" class></li>
                <li data-target="#myCarousel" data-slide-to="4" class></li>
            </ul>
            <div class="carousel-inner">
                <div class="item active">
                    <a class="block" id="mapItem0" href="http://svalbardkartet.npolar.no" target="_blank"><img src="/public/images/svalbardkartet_thumbnail.png" alt=""></a>
                    <div class="container">
                        <div class="carousel-caption">
                            <h5 class="caption-headline"><a class="caption-link" href="http://svalbardkartet.npolar.no" target="_blank">Svalbardkartet</a></h5>
                            <p class="caption-text">
                                An interactive thematic atlas of Svalbard supplemented with a rich datasets of environmental data layers with advanced map viewer capable of high-resolution map printing, identifiying map objects, advanced drawing and measurements...
                            </p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <a class="block" id="mapItem1" href="http://toposvalbard.npolar.no" target="_blank"><img src="/public/images/toposvalbard_thumbnail.png" alt=""></a>
                    <div class="container">
                        <div class="carousel-caption">
                            <h5 class="caption-headline"><a class="caption-link" href="http://toposvalbard.npolar.no" target="_blank">Toposvalbard</a></h5>
                            <p class="caption-text">
                                A fast and interactive topographical map portal of Svalbard with detailed topography and placenames, 3D view of Svalbard as well as areal and landscape photos...
                            </p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <a class="block" id="mapItem2" href="http://topojanmayen.npolar.no" target="_blank">
                    <img src="../public/images/topojanmayen_thumbnail.png" alt=""></a>
                    <div class="container">
                        <div class="carousel-caption">
                            <h5 class="caption-headline"><a class="caption-link" href="http://topojanmayen.npolar.no" target="_blank">TopoJanMayen</a></h5>
                            <p class="caption-text">
                                TopoJanMayen is an interactive topographical map of Jan Mayen. <br/>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <a class="block" id="mapItem3" href="http://geodata.npolar.no/barentsportal" target="_blank"><img src="/public/images/barentsportal_thumbnail.png" alt=""></a>
                    <div class="container">
                        <div class="carousel-caption">
                            <h5 class="caption-headline"><a class="caption-link" href="http://geodata.npolar.no/barentsportal" target="_blank">Barentsportal</a></h5>
                            <p class="caption-text">
                                 Interactive thematic atlas of the joint Norwegian-Russian environmental status report for the barents sea... <a class="caption-link" href="http://geodata.npolar.no/barentsportal" target="_blank">check out the new features</a>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <a class="block" id="mapItem4" href="http://geodata.npolar.no/cryoclim" target="_blank"><img src="/public/images/cryoclim_thumbnail.png" alt=""></a>
                    <div class="container">
                        <div class="carousel-caption">
                            <h5 class="caption-headline"><a class="caption-link" href="http://geodata.npolar.no/cryoclim" target="_blank">Svalbard Glaciers (Cryoclim)</a></h5>
                            <p class="caption-text">
                                Svalbard Glaciers portal is an interactive map portal presenting dynamic maps of surface types and area outlines of glaciers of Svalbard...
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <a class="left carousel-control" href="#myCarousel" data-slide="prev"><!--&lsaquo;--></a>
            <a class="right carousel-control" href="#myCarousel" data-slide="next"><!--&rsaquo;--></a>
</div>


## Basemaps
Norwegian Polar Institute provides access to a wide range of basemap and
thematic map services for the Norwegian polar regions which can be
consumed to create interactive web mapping applications.

NPI offers a selection of basemap services that are cached services.
[Tiled (cached) map
service](http://webhelp.esri.com/arcgisserver/9.2/dotnet/manager/publishing/static_map_svcs.htm)
is a regular map service that has been predrawn by the server at defined
scales (zoom levels) in order to serve maps fast. The services can be
used in clients with support for ArcGIS Server tiles such as OpenLayers,
Google Maps or Esri's JavaScript API in the same way as Google Maps or
Esri Maps is built up. Read the **[developer's guide](documentation)** on how to create web
applications with those basemaps.

#### Services in Map Cache:

| Service Name | Layers  | Projection    | Service URL | Capabilities |
| ------------ | ------- | ------------- | ----------- | ------------ |
| [NP_Basiskart_Svalbard_WMTS_25833](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_Svalbard_WMTS_25833/MapServer?f=jsapi) | Svalbard topography | ETRS 89 UTM 33 (EPSG:25833) | [ArcGIS Rest](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_Svalbard_WMTS_25833/MapServer) | [WMTS](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_Svalbard_WMTS_25833/MapServer/WMTS/1.0.0/WMTSCapabilities.xml); [WMS](http://geodata.npolar.no/arcgis/services/Basisdata/NP_Basiskart_Svalbard_WMTS_25833/MapServer/WMSServer?request=GetCapabilities&service=WMS) |
| [NP_Basiskart_JanMayen_WMTS_25829](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25829/MapServer?f=jsapi) | Jan Mayen topography | ETRS 89 UTM 29 (EPSG:25829) | [ArcGIS Rest](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25829/MapServer) | [WMTS](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25829/MapServer/WMTS/1.0.0/WMTSCapabilities.xml); [WMS](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25829/MapServer/WMSServer?request=GetCapabilities&service=WMS) |
| [NP_Basiskart_JanMayen_WMTS_25833](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25833/MapServer?f=jsapi)| Jan Mayen topography | ETRS 89 UTM 33 (EPSG:25833) | [ArcGIS Rest](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25833/MapServer) | [WMTS](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25833/MapServer/WMTS/1.0.0/WMTSCapabilities.xml); [WMS](http://geodata.npolar.no/arcgis/rest/services/Basisdata/NP_Basiskart_JanMayen_WMTS_25833/MapServer/WMSServer?request=GetCapabilities&service=WMS) |


#### Zoom levels and scales

To easily combine cache from different services in the same map window,
there is an advantage to have a common definition of the geographic area
that defines the service. Because the cached services have fixed zoom
levels, the service can not deliver tiles that lies between two defined
zoom levels.

The table shows the zoom level used when creating cache at Norwegian
Polar Institute which is similar to Norwegian Mapping Authority's [cache
standard](http://www.kartverket.no/Kart/Kartverksted/Visningstjenester/Cache-tjenester/).


#### Overview of zoom levels, scales and resolution

|Zoom Level|Scale|Resolution|
|----------|-----|----------|
|0|1:81920000|21674.7100160867|
|1|1:40960000|10837.3550080434|
|2|1:20480000|5418.67750402168|
|3|1:10240000|2709.33875201084|
|4|1:5120000|1354.66937600542|
|5|1:2560000|677.334688002709|
|6|1:1280000|338.667344001355|
|7|1:640000|169.333672000677|
|8|1:320000|84.6668360003387|
|9|1:160000|42.3334180001693|
|10|1:80000|21.1667090000847|
|11|1:40000|10.5833545000423|
|12|1:20000|5.29167725002117|
|13|1:10000|2.64583862501058|


#### Image formats and coordinate systems

Services are available in two image formats:

-   Image / jpeg (does not support transparency)
-   Image / png (supports transparency)

Tile size for jpeg is about 1/3 of the png so it must be considered what
is important, speed or support for transparency. The image tiles have a
resolution of 96 dpi with a size of (256x256 pixels).

------------------------

## Thematic Map Services

Polar institute delivers a wealth of thematic maps as dynamic map
services. Dynamic map service is a service where a server request to
send map section in the form of raster files back to the user, either
directly in the browser, a web application or a desktop application.


|Service URL|Name|Show on Svalbardkartet|WMS Capabilities|Owner|
|-----------|----|----------------------|----------------|-----|
|[Glaciers](http://geodata.npolar.no/ArcGIS/rest/services/CryoClim/glaciers/MapServer)|Svalbard Glacier Area Outlines|[Isbreer](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=453925.632753013,8669122.04466099,615847.099861399,8764021.49848276&showOverviewMap=False&layers=6,0,0,5,1,0,4,1,0,3,1,0,10,1,0,9,0,3,0,1,2,8,0,0,0,0,0,11,0,0,)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/CryoClim/glaciers/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Geologi-S750](http://geodata.npolar.no/ArcGIS/rest/services/inspire2/Geologi_S750/MapServer)|Geological Map of Svalbard 1:750000|[Geologi 1:750000](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=365645.670692461,8609882.48352378,689488.604909234,8799681.39116732&showOverviewMap=False&layers=6,0,0,5,1,0,4,1,0,3,1,0,10,1,0,9,1,0,8,1,0,0,1,0,11,1,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire2/Geologi_S750/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Sjøfuglkolonier](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Sjofuglkolonier/MapServer)|Seabirds of Svalbard|[Sjøfugl kolonier](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=307569.069943427,8504296.67749686,955254.938376966,8937790.87781859&showOverviewMap=False&layers=6,0,0,5,0,0,4,0,1,2,3,0,0,10,0,0,9,0,0,8,0,0,0,0,0,11,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Sjofuglkolonier/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Hvalrossliggeplasser](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Hvalrossliggeplasser/MapServer)|Walrus haulout sites|[Hvalrossliggeplasser](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=8351.2081993814,8196250.95958335,1303722.94506646,9063239.36022681&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,1,0,3,1,0,10,1,0,9,1,0,8,0,0,0,0,0,11,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Hvalrossliggeplasser/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Roye](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Roye/MapServer)|Arctic char in Svalbard|[Roye](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=262500.541078252,8566556.29469205,910186.409511791,8946154.10997914&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,1,1,3,1,0,10,1,0,9,1,0,8,0,0,0,0,0,11,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Roye/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[SjøpattedyrObservasjon](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/SjopattedyrObservasjon/MapServer)|Marine mammals sightings|[Sjøpattedyr Observasjoner2009](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=False&showDataFrame=True&extent=-559883.954708953,7528121.63475736,2030859.5190252,9262098.43604428&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,1,24,3,1,0,10,1,0,9,1,0,8,0,0,0,0,0,11,0,0,&)|[GetCapablities](http://geodata.npolar.no/ArcGIS/services/inspire3/SjopattedyrObservasjon/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Vegetasjon](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Vegetasjon/MapServer)|Svalbard Vegetation|[Vegetasjon](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=261571.293060411,8499650.43740767,909257.161493954,8879248.25269476&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,1,59,3,1,0,10,1,0,9,1,0,8,0,0,0,0,0,11,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Vegetasjon/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Biogeografiske](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Biogeografiske/MapServer)|Biogeographic zones of Svalbard|[Biogeografiske](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=261803.605064871,8499650.43740767,909489.473498414,8879248.25269476&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,1,58,3,1,0,10,1,0,9,1,0,8,0,0,0,0,0,11,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Biogeografiske/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Norwegian Polar Institute|
|[Strandrydding](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Strandrydding/MapServer)|Beach cleaning activities in Svalbard|[Strandrydding](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=211390.499731244,8618245.71568432,859076.36816479,8997843.53097142&showOverviewMap=False&layers=6,0,0,5,0,0,4,0,2,52,56,3,0,0,10,0,0,9,0,0,8,0,0,12,0,0,0,0,0,&)|[GetCapablities](http://geodata.npolar.no/ArcGIS/services/inspire3/Strandrydding/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Governor of Svalbard|
|[Skuterbegrensning](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Fritid/MapServer/3)|Snowmobile restrictions on Svalbard|[Skuterbegrensning](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=374010.303218889,8605352.39943682,697853.237435661,8795151.30708036&showOverviewMap=False&layers=6,0,0,5,0,0,4,0,0,3,0,0,10,0,1,1,9,0,0,8,0,0,12,0,0,0,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Fritid/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Governor of Svalbard|
|[Skyte-jaktforbudssoner](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Fritid/MapServer/2)|Hunting restrictions on Svalbard|[Skyte-jaktforbudssoner](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=368434.815111858,8613018.69558399,692277.749328628,8802817.60322753&showOverviewMap=False&layers=6,0,0,5,0,0,4,0,0,3,0,0,10,0,1,2,9,0,0,8,0,0,12,0,0,0,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Fritid/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Governor of Svalbard|
|[Svalbardgrenser](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Svalbardgrenser/MapServer)|Svalbard sea borders|[Svalbardgrenser](http://svalbardkartet.npolar.no/en/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=True&showDataFrame=True&extent=-370783.383444695,7960802.74306346,2219960.09028954,9479194.00421186&showOverviewMap=False&layers=6,0,0,5,1,0,4,0,0,3,0,1,7,10,1,0,9,1,0,8,0,0,12,0,0,0,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Svalbardgrenser/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Governor of Svalbard|
|[Utmål](http://geodata.npolar.no/ArcGIS/rest/services/inspire3/Utmaal/MapServer)|Utmål på Svalbard|[Utmål](http://svalbardkartet.npolar.no/Viewer.html?Viewer=Svalbardkartet&showAdvancedTools=False&showDataFrame=True&extent=359738.293451629,8557835.33834338,738029.716701142,8874489.30498465&showOverviewMap=False&layers=6,0,0,5,0,0,4,0,0,3,0,1,5,10,0,0,9,0,0,8,0,0,12,0,0,0,0,0,&)|[GetCapabilities](http://geodata.npolar.no/ArcGIS/services/inspire3/Utmaal/MapServer/WMSServer?request=GetCapabilities&service=WMS)|Bergmesteren for Svalbard|

Dynamic services based on WMS specification are flexible and provides the user
with many options, such as:

-   Choosing which map projection will be produced in
-   Turn on or off layers in the service.
-   Choose scale freely
-   Which image format and transparency to be produced
-   Retrieving Legend of the various map layers
-   Obtaining basic information about objects on the map from attributes
    (feature info) etc

All services are published on NPI's **[map services directory](http://geodata.npolar.no/arcgis/rest/services/inspire3)**.

------------------------

## Terms of Use

By using the map services, you agree with the [terms of
use](http://geodata.npolar.no/bruksvilkar).

* * * * *

**Norwegian Polar Data**
 
 Norwegian Polar Institute
 
 9296 Tromsø
 
 Norway