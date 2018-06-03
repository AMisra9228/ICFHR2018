import tflearn
import numpy as np
from tflearn.layers.conv import conv_2d, max_pool_2d
#from tflearn.data_utils import build_hdf5_image_dataset
from tflearn.data_utils import image_preloader
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression

#dataset file 
dataset_file='imagelist'

X, Y = image_preloader(dataset_file, image_shape=(128, 128, 1), mode='file', categorical_labels=True, normalize=True, grayscale=True)
X=np.reshape(X, (-1, 128, 128 ,1))
print(np.shape(Y))
#print(np.array(Y).tolist())
'''
# Error : Can not update dimension of the X set => Can not be used in model.fit without proper tensor dimension
#build HDF5 database
build_hdf5_image_dataset(dataset_file, image_shape=(128, 128), mode='file', output_path='dataset.h5', categorical_labels=True, normalize=True, grayscale=True)

#load HDF5 dataset
h5f=h5py.File('dataset.h5', 'r')
X=h5f['X']
Y=h5f['Y']

print(X.shape, X.dtype)
print(Y.shape, Y.dtype)
'''

#model.fit(X, Y) is hopefully supported
# Building convolutional neural network

convnet=input_data(shape=[None, 128, 128, 1], name='input')
convnet=conv_2d(convnet, 32, 3, activation='relu')
convnet=max_pool_2d(convnet, 2)

convnet=conv_2d(convnet, 64, 3, activation='relu')
convnet=conv_2d(convnet, 64, 3, activation='relu')
convnet=max_pool_2d(convnet, 2)

convnet=conv_2d(convnet, 256, 3, activation='relu')
convnet=max_pool_2d(convnet, 2)

convnet=conv_2d(convnet, 512, 3, activation='relu')
convnet=max_pool_2d(convnet, 2)

convnet=conv_2d(convnet, 1024, 3, activation='relu')
convnet=max_pool_2d(convnet, 2)

convnet=fully_connected(convnet, 4096, activation='relu')
convnet=dropout(convnet,0.8)
convnet=fully_connected(convnet, 30, activation='softmax')

convnet=regression(convnet, optimizer='SGD', learning_rate=0.01, loss='categorical_crossentropy', name='targets')

model=tflearn.DNN(convnet)

## In case there is a aready fitted model, we load it and again fit it for increasing accuracy
## In case you are running for first line , comment the line below as #model.load('ICFHR.tfl')
#model.load('ICFHR.tfl')
#print(model.evaluate(X,Y))
model.fit({'input' :X}, {'targets' :Y}, n_epoch=111, validation_set=None, show_metric=True, run_id='ICFHR2018')
#model.fit(X, Y)
model.save('ICFHR.tfl')


