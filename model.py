import numpy as np
import numpy.linalg as LA
from scipy.stats.mstats import gmean
import random

class Model(object):
    MAX_ITERATIONS = 10000

    def fit(self, data, k=None):
        if k is None:
            N = len(data)
            if N <= 20:
                k = N - 4
            else:
                k = N - 20
            if k <= 0:
                k = 1
        num_features = self.num_features(data)
        centroids = self.init_centroids(num_features, k)
        iterations = 0
        old_centroids = None
        while not self.should_stop(old_centroids, centroids, iterations):
            old_centroids = centroids
            iterations += 1
            labels = self.assign_labels(data, centroids)
            centroids = self.calc_centroids(labels, k, num_features)
        return labels

    def num_features(self, data):
        return 1 if isinstance(list(data.values())[0][0], int) \
                    else len(list(data.values())[0][0])

    def init_centroids(self, dimension, num_clusters):
        return {i: np.array(tuple((random.uniform(0, 100)
            for d in range(dimension))))
                for i in range(num_clusters)}

    def should_stop(self, old_centroids, centroids, iterations):
        if iterations > self.MAX_ITERATIONS:
            return True
        if old_centroids is None:
            return False
        return {k: list(v) for k, v in old_centroids.items()} \
                        == {k: list(v) for k, v in centroids.items()}

    def assign_labels(self, data, centroids):
        labels = {}
        for s, (f, i) in data.items():
            for label, _ in [min([(l, LA.norm(np.array(f - c)))
                    for l, c in centroids.items()], key=lambda x: x[1])]:
                if label in labels:
                    labels[label][s] = (f, i)
                else:
                    labels[label] = {s: (f, i)}
        return labels

    def calc_centroids(self, labels, k, num_features):
        centroids = {}
        for l in range(k):
            if l in labels:
                centroids[l] = gmean([f for _, (f, _) in labels[l].items()])
            else:
                centroids[l] = np.array(tuple((random.uniform(0, 100)
                    for d in range(num_features))))
        return centroids
