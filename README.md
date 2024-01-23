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
<br>
<img width="40%" hright="40%" alt="Ekran görüntüsü 2024-01-23 173626" src="https://github.com/esatozholcek/Tree-Classification-Point-Cloud/assets/91495699/3ba670c0-62c6-4757-a844-372f506d6990">
<img width="75%" height="75%" alt="Ekran görüntüsü 2024-01-23 173759" src="https://github.com/esatozholcek/Tree-Classification-Point-Cloud/assets/91495699/e5b2071b-42a9-41c1-a883-9aaf3dfbfbfd">

### SaintLouisTrees.shp
Provides the ground truth information for tree locations.
<br>
<img src="https://github.com/esatozholcek/Tree-Classification-Point-Cloud/assets/91495699/1c0c2b10-1e5b-4c53-a034-2d2f70c6a166" width="50%" height="50%">

### SaintLouisTrees.png
Serves as an additional ground truth, indicating tree (value 220) and non-tree (value 0) locations in a 1D representation.
<img src="https://github.com/esatozholcek/Tree-Classification-Point-Cloud/assets/91495699/a39ac38a-ec96-449a-b492-63173c70dbbf" width="50%" height="50%">


### SaintLouisDSM.tif
The Digital Surface Model (DSM) is a TIFF file representing the terrain and surface features in the Lidar area. It provides additional context for tree classification.



### Collaborators

* Arzu Nisa Yalçınkaya
* Mehdi Yarğın
* Mahmut Esat Özhölçek
* Hatice Akkuş


