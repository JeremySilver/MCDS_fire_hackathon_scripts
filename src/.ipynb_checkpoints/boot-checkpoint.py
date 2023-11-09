### This fets up environment and symlinks

import os
import constants
from constants import RUNNING_ON_JUPYTER_HUB

def jupyterEnvFixes():
        if RUNNING_ON_JUPYTER_HUB:
            # We are assuming all of the datasets are under a subfolder of the current working directory called 'data'
            # note that this can be a symbolic link.
            #    
            # set up a link to the data directory:
            if not os.path.exists('data'):
                ## only create the symbolic link if the path does not already exist
                os.symlink('/mnt/mediaflux_fires_dataset/MCDS_fire_datasets','data')
            #
            # get some of the geoprocessing libraries (gdal, proj) to play nicely
            # gdal.SetConfigOption("GTIFF_SRS_SOURCE", "EPSG")
            # specify the path to the 'proj' library
            os.environ['PROJ_LIB'] = '/opt/conda/envs/python/share/proj'

###

