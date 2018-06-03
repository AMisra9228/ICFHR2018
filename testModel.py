import tflearn
import numpy as np
from tflearn.layers.conv import conv_2d, max_pool_2d
#from tflearn.data_utils import build_hdf5_image_dataset
from tflearn.data_utils import image_preloader
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression

#dataset file 
dataset_file='Genuine_testlist'

test_X, test_Y = image_preloader(dataset_file, image_shape=(128, 128, 1), mode='file', categorical_labels=True, normalize=True, grayscale=True)
test_X=np.reshape(test_X, (-1, 128, 128 ,1))

#print(np.shape(Y))
#print(np.array(Y).tolist())
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
model.load('ICFHR.tfl')
#print(model.predict(test_X)[0])

res=model.predict(test_X)	
textfile=open('Genuine_result','w')
for i in range(225):	# #genuine_testing_files (25*30)=750(from flavour_1, for each signer sample1-5 training and sample6-30 testing)
	textfile.write(np.array2string(np.amax(res[i]))+'\t->\t'+np.array2string(np.argmax(res[i]))+'\n')

textfile.close()

