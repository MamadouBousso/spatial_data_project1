import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os
import zipfile
import rasterio as rio
from rasterio.mask import mask
import glob
from itertools import product
from rasterio import windows
from rasterio.plot import show
from osgeo import gdal
from rasterio.warp import calculate_default_transform, reproject, Resampling
import json