# -*- coding: utf-8 -*-


from matplotlib.pylab import *
from collections import deque
import random
import numpy as np




class dbscan():

    

    # fields
    data = None
    dataCount = None

    clusters = None
    clusterCount = None

    filteredData = None

    minPoints = None
    epsilon = None

    datamap = None



    def __init__(self, datax, datay, minPoints, epsilon):
        """
            Creates a dbscan object to filter given datasets

            :param datax: 1D numpy array of x-input data
            :param datay: 1D numpy array of y-input data
            :param minPoints: integer, minimum neighborhood points for dbscan
            :param epsilon: float, minimum epsilon value for dbscan
        """
      

        ######################
        # exception handling #
        ######################

        # is datax set correctly?
        if not(type(datax) == np.ndarray) or not(vars().has_key("datax")):
            raise Exception("datax has to be set and be of type numpy.ndarray")

        # is datay set correctly?
        if not(type(datay) == np.ndarray) or not(vars().has_key("datay")):
            raise Exception("datay has to be set and be of type numpy.ndarray")

        # shapes of datax and datay have to match
        if datax.shape != datay.shape:
            raise Exception(
                    "shapes of datax and datay have to match."
                    + "\nshape of datax: " + str(datax.shape)
                    + "\nshape of datay: " + str(datay.shape)
                    )

        # is minPoints set correctly?
        if not(type(minPoints) == int) or not(vars().has_key("minPoints")):
            raise Exception("minPoints has to be set and be of type int")
        
        # is epsilon set correctly?
        if not(type(epsilon) == float) or not(vars().has_key("epsilon")):
            raise Exception("epsilon has to be set and be of type float")


        ########################
        # initialization stuff #
        ########################


        # initialize input data
        # row 0 contains datax, row 1 datay
        # each column represents one dataset of x,y-values
        self.data = np.array([datax,datay])

        # amount of datasets (input)
        self.dataCount = self.data.shape[1]

        # initialize filtered data
        self.filteredData = False

        # initialize amount of clusters
        self.clusterCount = 0

        # initialize clusters
        # contains all found clusters
        self.clusters = deque()

        # initialize minPoints (to build a cluster)
        self.minPoints = minPoints

        # initialize epsilon (maximum range for neighbors)
        self.epsilon = epsilon

        # initialize a datamap for each point
        # each value represents the following:
        # 0: point is not visited (not calculated yet)
        # 1: point is core point
        # 2: point is density-reachable
        # 3: point is noise
        #
        # e.g. 'datamap[2][5] = 1' means
        # the point 'data[2][5]' is a core point of a cluster
        #
        self.datamap = np.zeros(self.data.shape[1])

        # filter data 
        self.filter()

    

    def filter(self):

        # iterate over every dataset
        for i in xrange(0, self.dataCount):

            # if point is already visited: skip execution
            if self.datamap[i] != 0:
                continue

            # indexes of neighborhood points
            neighborPoints = self.__regionQuery(i)

            # number of neighborhood points
            neighborCount = len(neighborPoints)


            if neighborCount < self.minPoints:
                # mark point as noise
                self.datamap[i] = 3
            else:
                # found new cluster
                self.clusterCount += 1
                self.__expandCluster(i, neighborPoints)

        # get filteredKeys from datamap
        filteredKeys = np.where( self.datamap != 3 )
        filteredKeys = filteredKeys[0]
        
        # initialize filteredData with zeros
        self.filteredData = np.zeros((2,filteredKeys.shape[0]))

        # set filteredData
        for i in xrange(0, len(filteredKeys)):
            self.filteredData[0][i] = self.data[0][filteredKeys[i]] # x values
            self.filteredData[1][i] = self.data[1][filteredKeys[i]] # y values



    def __expandCluster(self, i, neighborPoints):

        # initialize a new cluster
        newCluster = deque()
        
        # container / iterator
        contNeighborPoints = list(neighborPoints)    

        for pointIndex in contNeighborPoints:
            
            # if point is not visited
            if self.datamap[pointIndex] == 0 or self.datamap[pointIndex] == 3:
                
                # current neighbors of current loop point
                curNeighbors = self.__regionQuery(pointIndex)

                # append new neighborhood to iterator
                [ contNeighborPoints.append(elem) for elem in curNeighbors ]           

                if len(curNeighbors) >= self.minPoints:
                    newCluster.append(pointIndex)
                    self.datamap[pointIndex] = 1 

                elif len(curNeighbors) > 0:
                    self.datamap[pointIndex] = 2

        self.clusters.append(newCluster)



    def __regionQuery(self, i):

        regionIndexes = deque()

        npiter = np.nditer( [self.data[0], self.data[1]], flags=["c_index"] )

        for x,y in npiter:
            
            if np.sqrt( (x - self.data[0][i])**2 + (y - self.data[1][i])**2  ) < self.epsilon:
                regionIndexes.append(npiter.index)

        points = np.array(regionIndexes)                





        # this returns a tuple containing 1D-Arrays of indexes which match our conditions
        #points = np.where(
                    #np.sqrt(
                        #( self.data[0] - self.data[0][i] )**2
                        #+
                        #( self.data[1] - self.data[0][i] )**2
                    #)
                    #<
                    #self.epsilon
                #)
        #points = np.where( 
                #(self.data[0] > self.data[0][i] - self.epsilon)
                #&
                #(self.data[0] < self.data[0][i] + self.epsilon)
                #&
                #(self.data[1] > self.data[1][i] - self.epsilon)
                #&
                #(self.data[1] < self.data[1][i] + self.epsilon)
                #)

        # this returns our array (tuple is not necessary)
        return points

    

    def plot(self):


        # unfiltered
        colors = ["b", "r", "g", "c", "m", "y", "k"]
        markers = ["+", "o", "x", "s", "h"]
        plt.subplot(2,2,1)
        plt.title("unfiltered")
        plt.ylim([-160,160])
        plt.xlim([-160,160])
        plt.plot(self.data[0], self.data[1], color="r", marker="o", linestyle="None")
        plt.text(-150, 130, "data pts: " + str(self.dataCount) )


        # filtered
        plt.subplot(2,2,2)
        plt.title("filtered")
        plt.ylim([-160,160])
        plt.xlim([-160,160])
        plt.plot(self.filteredData[0], self.filteredData[1], color="b", marker="o", linestyle="None")
        plt.text(-150, 130, "data pts: " + str(len(self.filteredData[0])) )


        # combined
        plt.subplot(2,2,3)
        plt.title("combined")
        plt.ylim([-160,160])
        plt.xlim([-160,160])
        plt.plot(
                map( lambda key: self.data[0][key], np.where(self.datamap == 3)[-1] ),
                map( lambda key: self.data[1][key], np.where(self.datamap == 3)[-1] ),
                color="r", marker="o", linestyle="None"
                )
        plt.plot(
                map( lambda key: self.data[0][key], np.where(self.datamap == 2)[-1] ),
                map( lambda key: self.data[1][key], np.where(self.datamap == 2)[-1] ),
                color="m", marker="o", linestyle="None"
                )
        plt.plot(
                map( lambda key: self.data[0][key], np.where(self.datamap == 1)[-1] ),
                map( lambda key: self.data[1][key], np.where(self.datamap == 1)[-1] ),
                color="b", marker="o", linestyle="None"
                )
        plt.text(-150, 130, "minPoints: " + str(self.minPoints))
        plt.text(-150, 110, "epsilon  : " + str(self.epsilon))

        # cluster
        plt.subplot(2,2,4)
        plt.title("clusters")
        plt.ylim([-160,160])
        plt.xlim([-160,160])

        for key,cluster in enumerate(self.clusters):

            xdata = np.take(self.data[0], cluster)
            ydata = np.take(self.data[1], cluster)

            plt.plot(xdata, ydata, color="b", marker="s", label="o", linestyle="None")

            for x,y in zip(xdata, ydata):
                plt.text(x+5, y-7, str(key), color="black", fontsize=9 )
    
        densityXdata = np.take(self.data[0], np.where(self.datamap == 2)[-1])
        densityYdata = np.take(self.data[1], np.where(self.datamap == 2)[-1])

        plt.plot(densityXdata, densityYdata, color="m", marker="o", linestyle="None")

        plt.text(-150, 130, "cluster: " + str(self.clusterCount) )
        plt.text(-150, 110, "core pts: " + str(len(np.where(self.datamap == 1)[0])) )
        plt.text(-150,  90, "dens pts: " + str(len(np.where(self.datamap == 2)[0])) )

        plt.show()
















