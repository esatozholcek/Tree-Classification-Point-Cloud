# **Tree-Classification-Point-Cloud**
## Overview
This project focuses on the classification of trees in Lidar data using machine learning techniques. The Lidar data is stored in a LAS file format (.laz), containing approximately 9 million points. The ground truth for tree classification is provided by a PNG file and a shapefile (.shp), which contains polygons defining the bounds of tree areas. A Digital Surface Model (DSM) is available in TIFF format (.tiff).

## Installation
```bash
pip install -r requirements.txt
```
## Data
### SaintLouisLidar.laz
Contains Lidar point cloud data in LAS format. Each point in the cloud represents a 3D coordinate in space along with additional information such as intensity.

### SaintLouisTrees.shp
Provides the ground truth information for tree locations.
### SaintLouisTrees.png
Serves as an additional ground truth, indicating tree (value 220) and non-tree (value 0) locations in a 1D representation.
### SaintLouisDSM.tif
The Digital Surface Model (DSM) is a TIFF file representing the terrain and surface features in the Lidar area. It provides additional context for tree classification.



### Collaborators

* Arzu Nisa Yalçınkaya
* Mehdi Yarğın
* Mahmut Esat Özhölçek
* Hatice Akkuş


