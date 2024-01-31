import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show

# Define the file path to your raster for the year 2022
raster_path_2022 ="C:\\Users\\a850840\\OneDrive - Yara International ASA\\Desktop\\New folder\\Haveri\\Haveri_coconut.tif"
pixel_size = 30  # Set the pixel size in meters

# Open the raster file for the year 2022
with rasterio.open(raster_path_2022) as src_2022:
    # Read the raster data as a NumPy array
    raster_array_2022 = src_2022.read(1)

    # Plot the raster file for the year 2022
    show(raster_array_2022, cmap='viridis', title='Raster 2022')

    # Calculate the area for sub-band 1 (paddy) for the year 2022
    paddy_mask_2022 = (raster_array_2022 == 1).astype(np.uint8)
    area_pixels_2022 = np.sum(paddy_mask_2022)
    area_square_meters_2022 = area_pixels_2022 * pixel_size ** 2
    area_hectares_2022 = area_square_meters_2022 / 10000

    print("Area of paddy in 2022:")
    print(f"In square meters: {area_square_meters_2022:.9f} square meters")
    print(f"In hectares: {area_hectares_2022:.9f} hectares")
    print(f"In pixels: {area_pixels_2022} pixels")
    print("-------------------------------")

# Input areas for paddy in the previous two years
input_area_2021 = 21000  # Replace with the actual area for 2021
input_area_2020 = 20000  # Replace with the actual area for 2020

# Plotting
years = ['2020', '2021', '2022']
areas = [input_area_2020, input_area_2021, area_hectares_2022]

plt.bar(years, areas, color=['blue', 'green', 'orange'])
plt.xlabel('Year')
plt.ylabel('Paddy Area (Hectares)')
plt.title('Comparison of Paddy Area Over Years')
plt.show()