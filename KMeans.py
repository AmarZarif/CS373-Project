import numpy as np
from numpy import linalg as la
import cvxopt
import cvxopt.solvers
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn import preprocessing
import pandas as pd


class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        """ Implementation of K-Means Clustering algorithm.
        
        Original Code:
        https://pythonprogramming.net/k-means-from-scratch-2-machine-learning-tutorial/?completed=/k-means-from-scratch-machine-learning-tutorial/

        k (int):
        tol (float):
        max_iter (int):
        """
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

        self.centroids = None
        self.classifications = None

    def fit(self, data, X):
        """ Group the data into clusters """
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in X:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        """ Predict the label of data """

        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

