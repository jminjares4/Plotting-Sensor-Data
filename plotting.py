''''
Author: Jesus Minjares
Date: 11/02/2020
App:
    The application will use the matplotlib modules to plot
    the sensor data that is being store into a .csv file with
    the use of pyserial. FuncAnimation will allow to plot
    an animate plot to display live data from the file called
    'data.csv'
Note:
    Using PyCharm, inorder to run the following code the modules must be
    installed.
    Steps to install modules:
        Go to file
            Setting/Preferences
                Project
                    Python Inteperter
                        '+', top right for Windows, bottom left for MacOS
                            search for the module
                                install package/s
                                    enter ok
'''
# import modules
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
from matplotlib.animation import FuncAnimation

# path for the 'data.csv' file, if file in the same folder, use 'data.csv' as path
path = 'C:\\Users\\19152\\Desktop\\serialRead\\data.csv'
plt.style.use('seaborn-deep')  # set the style of the plot

offset = [500, 50, 250]  # hold the offset for each of the subplots
fig = plt.figure(figsize=(11, 6))  # set figure to 10*5 size
'''
Note: fig.add_subplot(221), 221 state that 2 rows, 2 cols at index 1
      1 2
      3 4
'''
axs = [fig.add_subplot(311), fig.add_subplot(313),fig.add_subplot(312)]  # store the subplots
titles = ['ADC vs Samples', 'ADC vs Time', 'CURRENT SIGNAL']  # titles for the subplots
xlabels = ['Sample', 'Time', 'Sample']  # xlabels
ylabels = ['ADC Raw', 'ADC Raw', 'ADC Raw']  # ylabels
color = ['red', 'black','blue']  # color of the line
legend = ['best']  # legend location

# animate function will allow to plot in real time
def animate(i):
    data = pd.read_csv(path)  # store the file data into the data
    sample = data['sample']  # store the sample
    time = data['time']
    adc_raw = data['adcRaw']  # store adc raw data
    volt = data['volt']  # store the volt

    # remove the offset[i] elements from the list
    x_axis = [sample[-offset[0]:], time[-offset[1]:], sample[-offset[2]:]]
    y_axis = [adc_raw[-offset[0]:], adc_raw[-offset[1]:], adc_raw[-offset[2]:]]

    curr_i = 0  # reset counter
    for ax in axs:  # iterate over the list of axs
        ax.cla()  # clear axis
        ax.set_title(titles[curr_i], weight='black', size=16)  # set the title text
        ax.set_ylabel(ylabels[curr_i], weight='bold', size=12)  # set the y label
        ax.set_xlabel(xlabels[curr_i], weight='bold', size=12)  # set the x label
        # plot x,y,color, label
        ax.plot(x_axis[curr_i], y_axis[curr_i], color[curr_i], label=ylabels[curr_i], marker='', linestyle='-', linewidth=2)
        ax.legend(loc=legend[0])  # set legend of each subplot
        ax.grid()  # set a grid
        ax.tick_params(axis='x', labelrotation=45)  # rotate the x axis label
        ax.tick_params(axis='y', labelrotation=0)  # rotate the y axis label
        mplcursors.cursor(multiple=False, hover=True)  # show annotation once hovering over the plot
        curr_i = curr_i + 1  # increment the counter


# call the FuncAnimation method to animate the plot
# set the current figure of the plot, pass the animate function, call it every 10ms
ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
plt.tight_layout(pad=5)  # set tight layout

plt.show()  # display the plot

