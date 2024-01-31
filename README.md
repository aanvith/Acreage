# Acreage

Paddy Area Analysis README
Overview
This Python script uses raster data to analyze and compare paddy area over multiple years. It employs the rasterio, numpy, and matplotlib libraries for raster data handling, array manipulation, and visualization, respectively.

Code Explanation
1. Importing Libraries
The script starts by importing necessary libraries: rasterio for raster data manipulation, numpy for array operations, and matplotlib.pyplot for plotting.
2. Raster File and Pixel Size Definition
The file path for the raster data of the year 2022 is specified (raster_path_2022), along with the pixel size in meters.
3. Opening and Plotting Raster for 2022
The raster file for 2022 is opened using rasterio. The script then reads the raster data and plots it using matplotlib.pyplot.
4. Calculating Paddy Area for 2022
The script calculates the area of paddy for the year 2022 by creating a binary mask for paddy pixels. It then computes the area in square meters, hectares, and pixels.
5. Comparison with Previous Years
The paddy areas for the years 2020 and 2021 are inputted manually (input_area_2020 and input_area_2021). The script creates a bar chart to visually compare the paddy areas over the specified years.
How to Use
Install the required libraries: rasterio, numpy, matplotlib.
Replace raster_path_2022, input_area_2021, and input_area_2020 with the actual file path for the raster of 2022 and the corresponding paddy areas for 2021 and 2020.
Run the script to analyze and visualize the paddy area over the specified years.
Feel free to contact for further assistance or clarifications.
