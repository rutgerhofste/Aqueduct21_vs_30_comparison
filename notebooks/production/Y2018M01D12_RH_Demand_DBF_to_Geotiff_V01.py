
# coding: utf-8

# Y2018M01D12_RH_Demand_DBF_to_Geotiff_V01

# In[2]:

import os
if 'GDAL_DATA' not in os.environ:
    os.environ['GDAL_DATA'] = r'/usr/share/gdal/2.1'
from osgeo import gdal,ogr,osr
'GDAL_DATA' in os.environ
# If false, the GDAL_DATA variable is set incorrectly. You need this variable to obtain the spatial reference


# In[ ]:

# Input 

S3_INPUT_PATH_PRISTINE = "s3://wri-projects/Aqueduct30/processData/Y2017M08D23_RH_Merge_FAONames_V01/output/"
S3_INPUT_PATH_PROCESS = "s3://wri-projects/Aqueduct30/processData/Y2017M08D23_RH_Merge_FAONames_V01/output/"


# 

# In[ ]:



