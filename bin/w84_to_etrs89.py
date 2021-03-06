# -*- coding: utf-8 -*-
'''
Created on 10. feb. 2014

@author: Norwegian Polar Institute
'''
import os
import arcpy
from arcpy import env
connDir = "C:/Users/ermias/AppData/Roaming/ESRI/Desktop10.2/ArcCatalog/"
connName = "svbk@geodb@localhost.sde"
dbConn = connDir + connName


def w84_to_etrs89 (indir, outdir):
    # Output coordinate system - ETRS1989 UTM zone 33 north
    out_cs = "PROJCS['ETRS_1989_UTM_Zone_33N',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',15.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    env.workspace = indir
    # Input feature classes
    input_features =  arcpy.ListFeatureClasses()
    # Output workspace
    out_workspace = outdir + "/" + os.path.basename(indir).lower() + ".gdb"
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    if not arcpy.Exists(out_workspace):
        arcpy.CreateFileGDB_management(os.path.dirname(out_workspace), os.path.basename(out_workspace))
    arcpy.BatchProject_management(input_features, out_workspace, out_cs, "#","#")
    print "projecting: ", input_features

shp_dir = "W:/NP/SvalbardTema/Miljo/SjopattedyrObservasjon"
out_dir = "E:/Data/NP/SvalbardTema/etrs89/miljo"

w84_to_etrs89 (shp_dir, out_dir)
# export feature classess to postgis
env.workspace = out_dir + "/" + os.path.basename(shp_dir).lower() + ".gdb"
input_features =  arcpy.ListFeatureClasses()
arcpy.FeatureClassToGeodatabase_conversion(input_features,dbConn)