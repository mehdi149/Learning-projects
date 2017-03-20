#!/usr/bin/env python

import numpy as np
import itertools
import scipy.sparse as sparse


def poly_dense(X, degree):
    n_samples, n_features = X.shape

    # Find permutations/combinations which add to degree or less
    deg_min = 1
    combs = itertools.product(*(range(degree + 1) for i in range(n_features)))
    combs = np.array([c for c in combs if deg_min <= sum(c) <= degree])

    return (X[:, np.newaxis, :] ** combs).prod(-1).reshape(n_samples, -1)


def polynomial_features(X, degree):
    """Compute polynomial features of CSC matrix X."""
    if not sparse.isspmatrix_csc(X):
        return None

    n_samples, n_features = X.shape

    # store element-wise powers of X
    X_powers = [X]
    for i in range(1, degree):
        Y = X.copy()
        Y.data **= i + 1
        X_powers.append(Y)

    combs = itertools.product(*(range(degree + 1) for i in range(n_features)))
    # not sure if having a bias term in a sparse matrix is a good idea
    combs = np.array([c for c in combs if 1 <= sum(c) <= degree]) - 1

    Z = None
    Xf = []
    for i in range(combs.shape[0]):
        init = False
        for j, k in enumerate(combs[i, :]):
            if k >= 0:
                if init:
                    Z = Z.multiply(X_powers[k][:, j])
                else:
                    Z = X_powers[k][:, j].copy()
                    init = True
        Xf.append(Z)

    return sparse.hstack(Xf)


X = sparse.csc_matrix([[1,2],[3,4]])
print(X.todense())

Xt = polynomial_features(X, 3)
print(Xt.todense())

Xf = poly_dense(X.toarray(), 3)
print(Xf)