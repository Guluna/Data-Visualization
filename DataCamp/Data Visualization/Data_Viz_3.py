# # **********************************************************************************************
# Time Series & Image Processing

import matplotlib.pyplot as plt
import pandas as pd

pi_df = pd.read_csv('PI.csv')

# transforming a csv file with dates column into a pandas time-series object (changing type of DATE from string
# to date_time object & setting DATE column as index column)
pi_df.DATE = pd.to_datetime(pi_df.DATE)
pi_df.set_index('DATE', inplace=True)
type(pi_df.index)


# Plot the time series in magenta
plt.plot(pi_df.PI, color='magenta', label='Personal Income')
plt.title('Personal Income data of US Economy')
# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')
# Specify the orientation of the xticks
plt.xticks(rotation=60)         # x-ticks are distorted
# Display the plot
plt.show()


# # **********************************************************************************************
# Slicing a time series

# Unlike slicing from standard Python lists, tuples, and strings, when slicing time series by labels (and other pandas
# Series & DataFrames by labels), the slice includes the right-most portion of the slice. That is, extracting my_time_series['1990':'1995']
# extracts data from my_time_series corresponding to 1990, 1991, 1992, 1993, 1994, and 1995 inclusive.


view = pi_df['2007':'2008']
plt.xticks(rotation=45)
plt.title('Slicing PI time series: 2007 to 2008')
plt.plot(view, color='green')
plt.tight_layout()
plt.show()


# Partial string indexing works without slicing as well. For instance, using my_time_series['1995'], my_time_series['1999-05'],
# and my_time_series['2000-11-04'] respectively extracts views of the time series my_time_series corresponding to the entire
# year 1995, the entire month May 1999, and the entire day November 4, 2000.

# Slice PI from 2007 to 2009 (3 years) inclusive: view
view_1 = pi_df['2007':'2009']

# Plot the sliced series in the top subplot in red
plt.subplot(2,1,1)
plt.plot(view_1, color='red')
plt.title('PI: 2007 to 2008')
plt.xticks(rotation=45)

# Reassign the series by year 2010
view_2 = pi_df['2010']
# Plot the sliced series in the bottom subplot in green
plt.subplot(2,1,2)
plt.plot(view_2, color='green')
plt.title('PI: Year 2010')
plt.xticks(rotation=45)
# Improve spacing and display the plot
plt.tight_layout()
plt.show()


# Plotting an inset view
# Remember, rather than comparing plots with subplots or overlayed plots, you can generate an inset view directly using plt.axes().

# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = pi_df['2007-11':'2008-04']

# Plot the entire series 
plt.plot(pi_df)
plt.xticks(rotation=45)
plt.title('PI: 1959-2019')

# Specify the axes
plt.axes([0.25,0.5,0.35,0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()


# # **********************************************************************************************
# Computing Moving Average for a time series (using rolling window operation)

pi_df['Moving_Average_30'] = pi_df['PI'].rolling(window=30).mean()
pi_df['Moving_Average_75'] = pi_df['PI'].rolling(window=75).mean()
pi_df['Moving_Average_125'] = pi_df['PI'].rolling(window=125).mean()
pi_df['Moving_Average_250'] = pi_df['PI'].rolling(window=250).mean()


# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2,2,1)
plt.plot(pi_df['Moving_Average_30'], color='green')
plt.plot(pi_df.PI, 'k-.')
plt.xticks(rotation=60)
plt.title('30 month averages')

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2,2,2)
plt.plot(pi_df['Moving_Average_75'], 'red')
plt.plot(pi_df.PI, 'k-.')
plt.xticks(rotation=60)
plt.title('75 month averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(pi_df['Moving_Average_125'], 'magenta')
plt.plot(pi_df.PI, 'k-.')
plt.xticks(rotation=60)
plt.title('125 month averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2,2,4)
plt.plot(pi_df['Moving_Average_250'], 'cyan')
plt.plot(pi_df.PI, 'k-.')
plt.xticks(rotation=60)
plt.title('250 month averages')

# Display the plot
plt.show()


# plot pre-computed moving standard deviations of the same stock prices, this time together on common axes.
# The time series  is not plotted in this case; it is of a different length scale than the standard deviations.

pi_df['Moving_Average_30'] = pi_df['PI'].rolling(window=30).std()
pi_df['Moving_Average_75'] = pi_df['PI'].rolling(window=75).std()
pi_df['Moving_Average_125'] = pi_df['PI'].rolling(window=125).std()
pi_df['Moving_Average_250'] = pi_df['PI'].rolling(window=250).std()

# Plot std_30 in red
plt.plot(pi_df['Moving_Average_30'], color='red', label='30 months')
plt.plot(pi_df['Moving_Average_75'], color= 'cyan', label='75 months')
plt.plot(pi_df['Moving_Average_125'], color= 'green', label='125 months')
plt.plot(pi_df['Moving_Average_250'], color= 'magenta', label='250 months')
plt.legend(loc='upper left')
plt.title('Moving standard deviations')
plt.show()



# # # **********************************************************************************************
# Image Manipulation (Histogram Equalization in images)
# Extracting a histogram from a grayscale image

# Load the image into an array: image
image = plt.imread('low_contrast.jpg')
# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')
# Flatten the image into 1 dimension: pixels so that it can be used with hist fn
pixels = image.flatten()
# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256), density=True, color='red', alpha=0.4)       # range is interval of available values,
# normed=True (normed is deprecated, use density=True instead) rescales the total area under histogram to be equal to 1
# alpha introduces transparency in histogram bars
plt.show()

# In last histogram plot we observed that values are concentrated between 125-200 in histogram. We want them to spread out.


# A histogram of a continuous random variable is sometimes called a Probability Distribution Function (or PDF). The area
# under a PDF (a definite integral) is called a Cumulative Distribution Function (or CDF). The CDF quantifies the probability
# of observing certain pixel intensities.


# # # **********************************************************************************************

# plot the PDF and CDF of pixel intensities from a grayscale image.
# histogram option cumulative=True permits viewing the CDF instead of the PDF.
# Notice that plt.grid('off') switches off distracting grid lines.
# The command plt.twinx() allows two plots to be overlayed sharing the x-axis but with different scales on the y-axis.


# Display image in top subplot using color map 'gray'
plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2, 1, 2)
pdf = plt.hist(pixels, bins=64, range=(0, 256), density=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0, 256),
               density=True, cumulative=True,
               color='blue', alpha=0.4)

# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()

# Notice that the histogram is not well centered over the range of possible pixel intensies. The CDF rises sharply near
# the middle (that relates to the overall grayness of the image).


# # # **********************************************************************************************
# Histogram equalization is an image processing procedure that reassigns image pixel intensities. The basic idea is to use
# interpolation to map the original CDF of pixel intensities to a CDF that is almost a straight line. In essence, the pixel
# intensities are spread out and this has the practical effect of making a sharper, contrast-enhanced image.

import numpy as np
# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), density=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)

# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image.astype('uint8'), cmap='gray')

# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), density=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, density=True,
               color='blue', alpha=0.4)
plt.show()

# Histogram equalization can help make an image sharper.



# # # **********************************************************************************************
# Extracting histograms from a color image
# plot three overlaid color histograms on common axes (one for each channel) in a subplot as well as the original image in a separate subplot.

# Load the image into an array: image
image = plt.imread('nebula.jpg')

# Display image in top subplot
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image)

# Extract 2-D arrays of the RGB channels: red, green, blue
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]

# Flatten the 2-D arrays of the RGB channels into 1-D
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()

# Overlay histograms of the pixels of each color in the bottom subplot
plt.subplot(2,1,2)
plt.title('Histograms from color image')
plt.xlim((0,256))
plt.hist(red_pixels, bins=64, density=True, color='red', alpha=0.2)
plt.hist(green_pixels, bins=64, density=True, color='green', alpha=0.2)
plt.hist(blue_pixels, bins=64, density=True, color='blue', alpha=0.2)

# Display the plot
plt.show()
