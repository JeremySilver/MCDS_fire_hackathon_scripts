import constants
from constants import PLOT_FIGS_HERE

# # Importing libraries for visualization
import matplotlib
from matplotlib import pyplot as plt

def renderTerrain(data):
    # Plot and save the DEM ROI including land and sea
    res = plt.imshow(data, interpolation='nearest')
    plt.title('Terrain height for the region of interest (with oceans masked)')
    if not PLOT_FIGS_HERE:
        plt.savefig("images/dem_roi_landsea.png")
        plt.close()

def renderTerrainNegative(data):
    # Replace ocean points (negative values) with zero for better visualization
    data[data < -100] = 0.0
    
    # Plot and save the modified DEM ROI
    res = plt.imshow(data, interpolation='nearest')
    plt.title('Terrain height for the region of interest')
    if not PLOT_FIGS_HERE:
        plt.savefig("images/dem_roi.png")
        plt.close()