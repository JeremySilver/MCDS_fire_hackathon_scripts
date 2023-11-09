import numpy as np

# Importing library for working with netCDF files
import netCDF4 as nc

import geo
from geo import getBoundingCoords

def getRoiData():
    # Set Bounding Coordinates
    boundingCoords = getBoundingCoords(True)
    roi_lon_bounds = boundingCoords[0]
    roi_lat_bounds = boundingCoords[1]
    
    # Load DEM data from NetCDF file
    dem_dataset = nc.Dataset('data/DEM/dem-9s.nc')
    dem_lon = dem_dataset.variables['lon'][:].data
    dem_lat = dem_dataset.variables['lat'][:].data
    
    # Find the DEM indices corresponding to the ROI
    roi_ixlim = np.searchsorted(dem_lon, roi_lon_bounds)
    roi_iylim = np.searchsorted(dem_lat, roi_lat_bounds)
    
    # Extract DEM data for ROI
    dem_roi_arr = dem_dataset.variables['Band1'][roi_iylim[0]:roi_iylim[1], roi_ixlim[0]:roi_ixlim[1]][:].data
    dem_dataset.close()

    # return data
    return dem_roi_arr