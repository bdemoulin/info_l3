import numpy as np
import scipy.stats as sp

# sets stores the four Anscombe data sets
# slopes stores the slope and the intercept of the linear regression
sets = []
slopes = []

# First, we need to load the data
for i in range(0,4):

    anscombe_set = np.loadtxt("anscombe.dat",skiprows=4,usecols=(2*i,2*i+1))
    sets += [anscombe_set]

# k indexes the sets
k = 0

for data in sets :

    # For each dataset we compute the mean value and the deviation for x and y.
    mean_x = np.mean(sets[k][:,0])
    var_x = np.var(sets[k][:,0])
    mean_y = np.mean(sets[k][:,1])
    var_y = np.var(sets[k][:,1])

    print "Mean value for set {} in x: {:.4f}, variance {:.2f}".format(k,mean_x,var_x)
    print "Mean value for set {} in y: {:.4f}, variance {:.2f}".format(k,mean_y,var_y)
    
    # Then the R coefficient (sp.pearson returns a list of elements)
    pearson = sp.pearsonr(data[:,0],data[:,1])[0]

    print "Correlation: {}".format(pearson)
    
    # Then the linear regression returns a lot of stuff, we only need the firts two
    slope = sp.linregress(data[:,0],data[:,1])[0]
    intercept = sp.linregress(data[:,0],data[:,1])[1]

    print "Linear equation: y = {:.3f}x + {:.3f}".format(slope, intercept)

    print "\n"
    
    # Update ok k to go to next set
    k += 1
    # Storage of the slope and the intercept.
    slopes += [[slope, intercept]]


import matplotlib.pyplot as plt

# Creation of the figure
fig = plt.figure()

# We need four different plots. sub_plot(nrows, ncols, plot_number)
axes = [ fig.add_subplot(2,2,1),
         fig.add_subplot(2,2,2),
         fig.add_subplot(2,2,3),
         fig.add_subplot(2,2,4) ]


for data,axis,slope in zip(sets,axes,slopes):
    # Set the limits of the graphs
    axis.set_xlim([0,20])
    axis.set_ylim([0,20])
    # Load the Anscombe sets 
    x = data[:,0]
    y = data[:,1]
    # plot of the points of the set
    axis.plot(x, y, marker='o', ls='None', markerfacecolor='white',
              markeredgecolor='orange')
    
    # Plot of the linear regression line
    t = np.arange(0., 20., 0.1)
    axis.plot(t,slope[0]*t + slope[1])
    
# Show the plot !
plt.show()

