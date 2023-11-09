import os
import sys
import numpy as np
from matplotlib import cm
from osgeo import gdal, gdalnumeric, ogr, osr
import netCDF4 as nc
from pyproj import Proj, transform

import sys
sys.path.append('~/packages')

# GDAL does not use python exceptions by default
gdal.UseExceptions()

username = os.getenv('USER')
os.chdir('/home/{}/unzips/GRID_NVIS6_0_AUST_EXT_MVG'.format(username))
# shapefile_path = 'aus6_0e_mvg.ovr'
# shapefile_path = 'mvg6_0e_by_name.lyr'
# shapefile_path = 'aus6_0e_mvg.aux.xml'
# shapef = ogr.Open(shapefile_path)
# lyr = shapef.GetLayer( os.path.splitext( shapefile_path )[0])

# minX, maxX, minY, maxY = lyr.GetExtent()

shapefile_path = 'aus6_0e_mvg/w001001.adf'
shapef = gdal.Open(shapefile_path)
band = shapef.GetRasterBand(1)
rat = band.GetDefaultRAT()
attributeTable = {}
for icol in range(rat.GetColumnCount()):
    if rat.GetTypeOfCol(icol) == 0:
        val = [rat.GetValueAsInt(irow,icol) for irow in range(rat.GetRowCount())]
    elif rat.GetTypeOfCol(icol) == 1:
        val = [rat.GetValueAsDouble(irow,icol) for irow in range(rat.GetRowCount())]
    elif rat.GetTypeOfCol(icol) == 2:
        val = [rat.GetValueAsString(irow,icol) for irow in range(rat.GetRowCount())]
    name = rat.GetNameOfCol(icol)
    attributeTable[name] = val

## get the data type:
band.DataType
## returns a value of: 1
## this correspond to GDT_Byte (associated with std::uint8_t)
## (according to https://ahhz.github.io/raster/types/gdal_data_type/)

## read a 100 x 100 subset of the data
data = band.ReadAsArray(0, 0, 100, 100) ## .astype(np.byte)

## get the data type of the array returned
data.dtype ## dtype('int8')

text_file = open("attribute_table.txt", "w")
format_string = ''.join(["{}\t"] * 2) + '\n'
text_file.write(format_string.format(*[rat.GetNameOfCol(icol) for icol in range(rat.GetColumnCount())]))
for irow in range(rat.GetRowCount()):
    text_file.write(format_string.format(*tuple(rat.GetValueAsString(irow,icol) for icol in range(rat.GetColumnCount()))))

text_file.close()

blockSizes = band.GetBlockSize()
xBlockSize = blockSizes[0]
yBlockSize = blockSizes[1]    

rows = shapef.RasterXSize
cols = shapef.RasterYSize

## get the projection string
projection_string = shapef.GetProjection()
                    
## get the geotransform parameters of the file
transform0 = shapef.GetGeoTransform()
xOrigin = transform0[0]
yOrigin = transform0[3]
pixelWidth = transform0[1]
pixelHeight = transform0[5]
xVals = np.linspace(xOrigin, xOrigin + pixelWidth*rows, rows+1)
yVals = np.linspace(yOrigin, yOrigin + pixelHeight*cols, cols+1)
xValsMin = xVals.min()
xValsMax = xVals.max()
yValsMin = yVals.min()
yValsMax = yVals.max()
yValsIncreasing = yVals[::-1]

