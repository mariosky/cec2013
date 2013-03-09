__author__ = 'mariosky'

from pylab import *


w2_file = open("w2-256-p512-Real.dat")
w4_file = open("w4-256-p512-Real.dat")
w8_file = open("w8-256-p512-Real.dat")
w16_file = open("w16-256-p512-Real.dat")
w28_file = open("w28-256-p512-Real.dat")

w2_time = [ map(float,line[:-1].split(","))[1] for line in w2_file if len(line.split(",")) == 3 ]
w4_time = [ map(float,line[:-1].split(","))[1] for line in w4_file if len(line.split(",")) == 3 ]
w8_time = [ map(float,line[:-1].split(","))[1] for line in w8_file if len(line.split(",")) == 3 ]
w16_time = [ map(float,line[:-1].split(","))[1] for line in w16_file if len(line.split(",")) == 3 ]
w28_time = [ map(float,line[:-1].split(","))[1] for line in w28_file if len(line.split(",")) == 3 ]


data = [w2_time, w4_time, w8_time, w16_time, w28_time]
# multiple box plots on one figure
fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Average time (in seconds) to solution. 256 peaks/ 512 bits)')
ax1.set_xlabel('Number of workers')
ax1.set_ylabel('Time in seconds')

xtickNames = plt.setp(ax1, xticklabels= ["2","4","16","18","28"] )
#plt.setp(xtickNames, rotation=45, fontsize=8)
plt.setp(xtickNames)
#show()
plt.savefig('plot_time.eps')

w2_file.close()
w4_file.close()
w8_file.close()
w16_file.close()
w28_file.close()