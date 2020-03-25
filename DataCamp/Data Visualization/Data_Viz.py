import matplotlib.pyplot as plt
import numpy as np

year = [1,2,3,4,5]
physical_sciences = [0.2, 0.4, 0.6, 0.9, 2.2]
computer_science = [0.1, 0.22, 0.16, 1.9, 1.2]
health = [10,70,30,40,50]
education = [11,22,33,99,55]

#1 - Multiple plots on single axis

plt.plot(year, physical_sciences, color='blue')
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
# Display the plot
plt.show()

# **********************************************************************************************

#2 - Using axes()
# In calling plt.axes([xlo, ylo, width, height]), a set of axes is created and made active with lower corner at coordinates
# (xlo, ylo) of the specified width and height. Note that these coordinates can be passed to plt.axes() in the form of a
# list or a tuple.
# The coordinates and lengths are values between 0 and 1 representing lengths relative to the dimensions of the figure.
# After issuing a plt.axes() command, plots generated are put in that set of axes.

# Create plot axes for the first line plot
plt.axes([0.05, 0.05, 0.425, 0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525, 0.05, 0.425, 0.9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()

# End result: there now two separate plots with their own axes, & the axes for each plot are slightly different.

# **********************************************************************************************

#3 - Using subplot() (1)
# plt.axes() requires a lot of effort to use well because the coordinates of the axes need to be set manually. A better
# alternative is to use plt.subplot() to determine the layout automatically.
# Rather than using plt.axes() to explicitly lay out the axes, you will use plt.subplot(m, n, k) to make the subplot grid
# of dimensions m by n and to make the kth subplot active (subplots are numbered starting from 1 row-wise from the top
# left corner of the subplot grid).

# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()

# **********************************************************************************************

#4 - Creating a 2x2 subplot

# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

# **********************************************************************************************
#5 Controlling axis limits using xlim() & ylim()  (zooming in on a portion of graph)
# **********************************************************************************************

# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red')
plt.plot(year, physical_sciences, color='blue')

# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis range to period bw 1990-2010
plt.xlim([1, 3])

# Set the y-axis range
plt.ylim([0.1,1.9])

# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()

# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png')

# **********************************************************************************************
# 6 - using plt.axis([xmin, xmax, ymin, ymax]) instead of xlim() & ylim() here

# Plot in blue the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='blue')

# Plot in red the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences,color='red')

# Set the x-axis and y-axis limits  to select the time period between 1990 and 2010 on the x-axis as well as the interval between 0 and 50% awarded on the y-axis.
plt.axis((1,3, 0.1, 1.9))

# Show the figure
plt.show()

# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png')

# **********************************************************************************************
# 7- Legends, Annotations & Plot styles
# **********************************************************************************************

# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science')

# Specify the label 'Physical Sciences'
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc= 'lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

# **********************************************************************************************
# 8 - Annotations: like text and arrows can be used to emphasize specific observations.

year = np.array([1,2,3,4,5])
physical_sciences = np.array([0.2, 0.4, 0.6, 0.9, 2.2])
computer_science = np.array([0.1, 0.22, 0.16, 1.9, 1.2])
health = np.array([10,70,30,40,50])
education = np.array([11,22,33,99,55])
# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science:
# argmax() returns the index position of max value existing in array
yr_max = year[computer_science.argmax()]

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Add a black arrow annotation
# The arrow will point to the location given by xy and the text i.e. 'Maximum' will appear at the location given by xytext
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+0.2, cs_max+0.2), arrowprops = dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.tight_layout()
plt.show()

# **********************************************************************************************
# 9 - Modifying styles

# To list all the available style sheets you can execute:
print(plt.style.available)

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Set the style to 'ggplot'
plt.style.use('ggplot')

# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1)

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()




