import sys
sys.path.append('~/packages')
import os
sys.path.append('./src')
# help('modules') # uncomment for debugging modules

import utilities
# from utilities import sayHello

# import time
import datetimes
from datetimes import STUDY_DATETIME_RANGE
study_period_bounds = STUDY_DATETIME_RANGE # Rename/remove this when setup finished

#run startup scripst
import boot
from boot import jupyterEnvFixes
jupyterEnvFixes()

# Importing libraries for data manipulation and analysis
import numpy as np
import xarray
import dask
import glob
import gzip
import cftime
import time
import io

# Importing libraries for geospatial data
import geopandas as gpd
import rasterio as rio
from shapely.geometry import Point

# extract ROI data
import data
from data import getRoiData
roi_data = getRoiData()

# Flip the vertical orientation for plotting
dem_roi_arr = roi_data[::-1, :]

# Render Data
import graphing
from graphing import renderTerrain
from graphing import renderTerrainNegative

# Plot and save the DEM ROI including land and sea
renderTerrain(dem_roi_arr)

# Replace ocean points (negative values) with zero for better visualization
renderTerrainNegative(dem_roi_arr)

print('finished')