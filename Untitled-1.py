# %%
import laspy
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
import numpy as np

# %%
las_file = laspy.read("data/SaintLouisLiDAR.las")

attributes_to_print = list(las_file.point_format.dimension_names)
attributes_to_print
# X,Y,Z, red, green, blue, intensity harici 0 tutmaktadır
# return_number ve number_of_returns 0 değil değişmektedir

# %%
print(las_file.point_format["classification"])
print(type(las_file))


# %%
point = las_file.points[0]
print(f"X: {point.x}, Y: {point.y}, Z: {point.z}, Intensity: {point.intensity}, classification: {point.classification}")

# %%
import random

def extract_data(point):
    return {
        "X": getattr(point, "X"),
        "Y": getattr(point, "Y"),
        "Z": getattr(point, "Z"),
        "intensity": getattr(point, "intensity"),
        "red": getattr(point, "red"),
        "green": getattr(point, "green"),
        "blue": getattr(point, "blue"),
    }


df = pd.DataFrame([extract_data(p) for p in las_file.points[:10]])
print(df.head())


len_data = len(las_file.points)
points = las_file.points
for i in range(10):
    rand = random.randint(0, len_data)
    point = points[i]

    print(", ".join([f"{attr}: {getattr(point, attr)}" for attr in attributes_to_print]))

    # print(f"X: {point.x}, Y: {point.y}, Z: {point.z}, Intensity: {point.intensity}, classification: {point.classification}")

# %%
# X of shp to np array
x_values = np.array([getattr(point, "X") for point in points[:]])


# %%
# Y of shp to np array
y_values = np.array([getattr(point, "Y") for point in points[:]])


# %%
print(x_values[1000000])
print(getattr(points[1000000], "X"))
print(len(points))
print(type(points[0]))

# %%
print(type(points))
print(points[0].x)

# %%

shape_file = gpd.read_file("data/SaintLouisTrees/SaintLouisTrees.shp")
print(shape_file.head())
print(type(shape_file))
print()

print(shape_file.columns)
shape_file.drop('id', axis=1)
list_16 = list(shape_file.loc[16, "geometry"].exterior.coords)
first_point_x, first_point_y = list_16[0]
second_point_x, second_point_y = list_16[1]
print(list_16)

# Create a plot
plt.figure(figsize=(8, 6))


for i in range(len(list_16)):
    plt.plot(list_16[i][0], list_16[i][1], 'o', color='red', markersize=10)
    plt.annotate(
        f"{i}." "Point",
        xy=(list_16[i][0], list_16[i][1]),
        xytext=(5, -5),
        textcoords='offset points',
    )


# Add labels and title
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("First and Second Points of Polygon 16")

# Show the plot
plt.show()



# %%
print(list(shape_file.loc[16, "geometry"].exterior.coords))
print(len(shape_file.loc[16, "geometry"].exterior.coords))
print(shape_file.loc[16, "geometry"])
shape_file.loc[16, "geometry"]
# shape_file.plot(figsize=(10,10),edgecolor="k", facecolor="none") # color="green"

# %%
def is_inside(points, xp, yp):
    count = 0
    for i in range(len(points)-1):
        (x1,y1) = points[i]
        (x2,y2) = points[i+1]
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
            count += 1
        
    return count%2 == 1

print(is_inside(list_16, -90.33627979371984, 38.8421272995463))
    

# %%
def onclick(event):
    xp, yp = event.xdata, event.ydata
    if is_inside(list_16, xp, yp):
        print("inside")
        plt.plot(xp, yp, "go", markersize=5)
    else:
        print("outside")
        plt.plot(xp, yp, "ro", markersize=5)
    plt.gcf().canvas.draw()

plt.figure(figsize=(10,10))
plt.gca().set_aspect("equal")
xs, ys = zip(*list_16)
plt.gcf().canvas.mpl_connect("button_press_event", onclick)
plt.plot(xs, ys, "b-", linewidth=0.8)
plt.show()

# %%
# import sys
# !{sys.executable} -m pip install tifffile

# !pip install tifffile

import tifffile as tiff

tiff_file = tiff.imread("data/SaintLouisDSM/SaintLouisDSM.tif")

print(tiff_file.shape)
print(tiff_file.dtype)
print(tiff_file)

# %%

tif_file = rasterio.open("data/SaintLouisDSM/SaintLouisDSM.tif")
show(tif_file)
print(tif_file.width, tif_file.height)
print(type(tif_file))
print(tif_file.bounds)
print(tif_file.transform)
print(tif_file.transform * (0,0))
print(tif_file.transform * (tif_file.width, tif_file.height))
print(tif_file.read(1).shape) # returns numpy array
print(tif_file.read(1)[0,0])


