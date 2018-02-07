import numpy as np

features = np.array([0.49671415, -0.1382643, 0.64768854])

# You see above that sometimes you'll want a column vector, even though by default Numpy arrays work like row vectors.
# It's possible to get the transpose of an array like so arr.T
print(features)

# but for a 1D array, the transpose will return a row vector
print(features.T)

# Instead, use arr[:,None] to create a column vector:
print(features[:, None])

# Alternatively, you can create arrays with two dimensions.
print(np.array(features, ndmin=2))

# Then, you can use arr.T to get the column vector.
print(np.array(features, ndmin=2).T)
