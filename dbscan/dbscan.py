# -*- coding: utf-8 -*-


from matplotlib.pylab import *
import numpy as np




class dbscan():

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

        # amount of datasets
        self.dataCount = self.data.shape[1]

        # initialize filtered data
        self.filtered = False

        # initialize amount of clusters
        self.clusterCount = 0

        # initialize minPoints
        self.minPoints = minPoints

        # initialize epsilon
        self.epsilon = epsilon

        # initialize a datamap for each point
        # 0: point is not visited (not calculated yet)
        # 1: point is core point
        # 2: point is density-reachable
        # 3: point is noise
        self.datamap = np.zeros(self.data.shape[1])

        # filter data 
        self.filter()

    
    def filter(self):
       
        # iterate over every dataset
        for i in xrange(0, self.dataCount):
           
            # indexes of neighborhood points
            neighborPoints = self.__regionQuery(i)

            # number of neighborhood points
            neighborCount = neighborPoints.shape[0]


            if neighborCount < self.minPoints:
                # mark point as noise
                self.datamap[i] = 3
            else:
                # found new cluster
                self.clusterCount += 1
                self.__expandCluster()

        filteredKeys = np.where( self.datamap != 3 )
        filteredKeys = filteredKeys[0]

        self.filtered = np.zeros((2,filteredKeys.shape[0]))

        for i in xrange(0, len(filteredKeys)):
            self.filtered[0][i] = self.data[0][filteredKeys[i]]
            self.filtered[1][i] = self.data[1][filteredKeys[i]]


    def __expandCluster(self):
        return


    def __regionQuery(self, i):
        
        # this returns a tuple containing 1D-Arrays of indexes which match our conditions
        points = np.where( 
                (self.data[0] > self.data[0][i] - self.epsilon)
                &
                (self.data[0] < self.data[0][i] + self.epsilon)
                &
                (self.data[1] > self.data[1][i] - self.epsilon)
                &
                (self.data[1] < self.data[1][i] + self.epsilon)
                )

        # this returns our array (tuple is not necessary)
        return points[0]

    
    def plot(self):

        plt.subplot(2,2,1)
        plt.title("unfiltered")
        plt.plot(self.data[0], self.data[1], color="r", marker="o")

        plt.subplot(2,2,2)
        plt.title("filtered")
        plt.plot(self.filtered[0], self.filtered[1], color="b", marker="x")

        plt.subplot(2,2,3)
        plt.title("combined")
        plt.plot(self.data[0], self.data[1], color="r", marker="o")
        plt.plot(self.filtered[0], self.filtered[1], color="b", marker="x")


        plt.show()
















