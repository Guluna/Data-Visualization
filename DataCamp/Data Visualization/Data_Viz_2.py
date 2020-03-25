# 2D arrays for bivariate f(,y) functions & images


# Numpy arrays are just like lists but with homogenous data type
# Indexing with brackets: 1D array[index], 2D array[index0, index1]
# Slicing notation is start:stop(not included):stride, 1D array[start:stop(not included):stride],
#           2D array[start:stop(not included):stride, start:stop(not included):stride]

# pixel intensity: smallest entry is black & largest is white

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate two 1-D arrays: u, v
# The array u should contain 41 values uniformly spaced between -2 and +2. The array v should contain 21 values uniformly spaced between -1 and +1
x = np.linspace(-2, 2, 41)
y = np.linspace(-1, 1, 21)        # so basically x & y would give us 41 by 21 grid

# Generate 2-D arrays from u and v: X, Y
# this gives cartesian coordinate sys with u and v as coordinate range
X,Y = np.meshgrid(x,y)

# Z is the fn we want to plot within coordinate range of x & y
Z = np.sin(3*np.sqrt(X**2 + Y**2))

# Display the resulting image with pcolor()
plt.pcolor(X, Y, Z)
plt.axis('tight')
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')

plt.pcolor(Z)    # if we want our coordinate system to start from (0,0)
plt.show()

plt.contour(Z)
plt.show()

plt.contour(X, Y, Z, 40)     # here X & Y are used for tickmarks & 5 is the number of contours we want to plot
plt.show()

plt.contourf(X, Y, Z, 40)     # produces filled contour plots
plt.show()
#
# # # **********************************************************************************************
# A = np.array([[1, 1, 1], [2, 0, 1], [1, 0, -1]])
# plt.pcolor(A, cmap='Blues')
# plt.colorbar()
# plt.show()

# # **********************************************************************************************

# pcolor() stand for pseudocolor plot (i.e. its not grayscale)
# plt.pcolor(z, cmap='gray') will plot a fig in grayscale; plt.pcolor(z, cmap='autumn') will plot a fig in red & yellow hues
# colorbar() gives a vertical color bar on right of plot i.e. associating numerical values to color in some continuous way


# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X,Y,Z, 20)

# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(X,Y,Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(X,Y,Z, 20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

# # **********************************************************************************************
# practicing diff cmap options

# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

# # **********************************************************************************************
# Generate a 2-D histogram
# The function plt.hist2d() uses rectangular bins to construct a two dimensional histogram. As an alternative, the function
# plt.hexbin() uses hexagonal bins.

df = pd.read_csv('auto_mpg.csv')

plt.hist2d(df.hp, df.mpg, bins=(20,20), range=((40,235),(8,48)))
# Add a color bar to the histogram
plt.colorbar()
# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()


# Put hp along the horizontal axis and mpg along the vertical axis.
# Specify a hexagonal tesselation with 15 hexagons across the x-direction and 12 hexagons across the y-direction using gridsize.
# Specify the rectangular region covered with the optional extent argument: use hp from 40 to 235 and mpg from 8 to 48.

# Generate a 2d histogram with hexagonal bins
plt.hexbin(df.hp, df.mpg, gridsize=(15, 12), extent=(40, 235, 8, 48))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()


# # **********************************************************************************************
# Working with images (Remember image is a matrix of diff intensity values)
# To read an image from file, use plt.imread() by passing the path to a file, such as a PNG or JPG file.
# The color image can be plotted as usual using plt.imshow().
# The resulting image loaded is a NumPy array of three dimensions. The array typically has dimensions M×N×3
# , where M×N
# is the dimensions of the image. The third dimensions are referred to as color channels (typically red, green, and blue).
# The color channels can be extracted by Numpy array slicing.


# Load the image into an array: img
img = plt.imread('NASA.jpg')
# Print the shape of the image
print(img.shape)
# Display the image
plt.imshow(img)
# Hide the axes
plt.axis('off')
plt.show()

# Grayscale images are just rectangular 2D arrays e.g.
A = np.array([[1, 1, 1], [2, 0, 1], [1, 0, -1]])
plt.pcolor(A, cmap='gray')
plt.colorbar()
plt.show()


# Color images are 3D arrays with RGB values from  0 to 255 e.g.
# The array typically has dimensions M×N×3, where M×N is the dimensions of the image. The third dimensions are referred
# to as color channels (typically red, green, and blue).

img_3d = np.zeros((40,50,3))    # creating a 3D array filled with zeroes
img_3d[:, :25] = [0,0,0]        # set all rows uptill 25th column to black color
img_3d[:, 25:] = [1,1,1]        # set all rows after 25th column to white color
plt.imshow(img_3d)
plt.show()


# # **********************************************************************************************
# Converting colored image to Grayscale, use cmap='gray'
# Print the shape of the existing image array.
# Compute the sum of the red, green, and blue channels of img by using the .sum() method with axis=2.
# Print the shape of the intensity array to verify this is the shape you expect.
# Plot intensity with plt.imshow() using a 'gray' colormap.

# Load the image into an array: img
img = plt.imread('NASA.jpg')
# Print the shape of the image
print(img.shape)
# Compute the sum of the red, green and blue channels: intensity
intensity = img.mean(axis=2)        # average the RGB colors
# Print the shape of the intensity
print(intensity.shape)      # Notice how the array is now 2D.
# Display the intensity with a colormap of 'gray'
plt.imshow(intensity)
# Add a colorbar
plt.colorbar()
# Hide the axes and show the figure
plt.axis('off')
plt.show()

plt.imshow(intensity, cmap='gray')      # produces grayscale image
# Add a colorbar
plt.colorbar()
# Hide the axes and show the figure
plt.axis('off')
plt.show()


# # **********************************************************************************************
# Aspect Ratio is the ratio of displayed width to height so e.g. aspect = 2, means width is 2x height
# range used to label the x- and y-axes is known as the extent

# Load the image into an array: img
img = plt.imread('NASA.jpg')

# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2,2,1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=0.5)

# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2,2,2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=1)

# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2,2,3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=2)

# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2,2,4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2,-1,0,1,2])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-2,2,-1,1), aspect=2)

# Improve spacing and display the figure
plt.tight_layout()
plt.show()

# # **********************************************************************************************
# Rescaling pixel intensities


# Load the image into an array: image
image = plt.imread('low_contrast.jpg')
plt.title('Original (Low contrast) image')
plt.imshow(image)
plt.show()

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." %
      (rescaled_image.min(), rescaled_image.max()))

# Display the rescaled image
# As you can see, the rescaled image has pixel intensities in between 0 and 256 i.e high contrast
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image.astype('uint8'))
plt.show()


# # **********************************************************************************************
# Time to get our hands dirty with Seaborn which is built on top of matplotlib to create attractive statistical plots with ease

# using seaborn to fit and visualize a simple linear regression between two variables using sns.lmplot()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

auto_df = pd.read_csv('auto_mpg.csv')

# One difference between seaborn and regular matplotlib plotting is that you can pass pandas DataFrames directly to the
# plot and refer to each column by name. For example, if you were to plot the column 'price' vs the column 'area' from a
# DataFrame df, you could call sns.lmplot(x='area', y='price', data=df).

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto_df)
# Display the plot
plt.show()


# Plotting residuals of a regression
# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto_df, color='green')     # notice the dotted horizontal line for zero residuals
# Display the plot
plt.show()


# Higher order regressions
# Does a second order regression perform significantly better than a simple linear regression?
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto_df['weight'], auto_df['mpg'], label='data', color='red', marker='o')
# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto_df, color='blue', scatter=None, label='First Order')
# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto_df, color='green', scatter=None, label='Second Order', order=2)
# Add a legend and display the plot
plt.legend(loc= 'upper right')
plt.show()


# Grouping linear regressions by hue
# Seaborn makes it possible to apply linear regressions separately for subsets of the data by applying a groupby operation.
# Using the hue argument, you can specify
# a categorical variable by which to group data observations. The distinct groups of points are used to produce distinct
# regressions with different hues in the plot.
# Use the keyword argument palette to specify the 'Set1' palette for coloring the distinct groups.

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data= auto_df, hue='origin', palette='Set1')
# Display the plot
plt.show()


# Creating a grid of subplots rather than overlaying linear regressions of grouped data in the same plot
# It is easier to make sense of the three regression lines now that they each have their own subplot.
sns.lmplot(x='weight', y='hp', data= auto_df, col='origin')     # horizontally stacked
plt.show()
sns.lmplot(x='weight', y='hp', data= auto_df, row='origin')       # vertically stacked
plt.show()

# Also practiced with strip plots, swarm plots & violin plots

# Make a strip plot of 'hp' grouped by 'cyl'
# Here, 'hp' is the continuous variable, and 'cyl' is the categorical variable. The strip plot shows that automobiles
# with more cylinders tend to have higher horsepower.
plt.subplot(2,1,1)
sns.stripplot(x='cylinders', y='hp', data=auto_df)
# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cylinders', y='hp', data=auto_df, jitter=True, size=3)
# Display the plot
plt.show()


# Constructing swarm plots
# As you have seen, a strip plot can be visually crowded even with jitter applied and smaller point sizes. An alternative
# is provided by the swarm plot (sns.swarmplot()), which is very similar but spreads out the points to avoid overlap and
# provides a better visual overview of the data.
sns.swarmplot(x='cylinders', y='hp', data=auto_df)
plt.show()
# Swarm plots are generally easier to understand than strip plots because they spread out the points to avoid overlap.

# violin plots are a nice way of visualizing the relationship between a continuous variable and a categorical variable.
sns.violinplot(x='cylinders', y='hp', data=auto_df)
plt.show()


# # **********************************************************************************************
# Visualizing Multivariate distributions using jointplots, pairplots, heatmaps etc
# There are numerous strategies to visualize how pairs of continuous random variables vary jointly. Regression and
# residual plots are one strategy. Another is to visualize a bivariate distribution.

sns.jointplot(x='hp', y='mpg', data=auto_df)
plt.show()
sns.jointplot(x='hp', y='mpg', data=auto_df, kind='hex')
plt.show()


# Data sets often contain more than two continuous variables. The function sns.jointplot() is restricted to representing
# joint variation between only two quantities (i.e., two columns of a DataFrame).
# The function sns.pairplot() constructs a
# grid of all joint plots pairwise from all pairs of (non-categorical) columns in a DataFrame. The non-categorical columns
# are identified and the corresponding joint plots are plotted in a square grid of subplots. The diagonal of the subplot
# grid shows the univariate histograms of the individual columns.

sns.pairplot(auto_df)       # Seaborn's pairplots are an excellent way of visualizing the relationship between all continuous variables in a dataset.
plt.show()

sns.pairplot(auto_df, kind='reg', hue='origin')
plt.show()
#
# # If your pair plot starts to become visually overwhelming, heat maps are a great alternative.



