import numpy as np
dataset = np.random.random((2,3))

print dataset
print dataset.max()
#print dataset.max(1)
print dataset.max(axis=0)

print np.reshape(dataset,(3,2))

print dataset
