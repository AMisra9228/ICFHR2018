# Python Codes for Task 1
## This codes works only on signature database flavour 1

## Steps for running codes :::
> Step 1 : Create a directory somewhere in your filesystem(let's say 'x') and move all downloaded\* files there.\
 Step 2 : Go to 'x'  and create directory 'data'.\
Step 3 : Copy all directories from Signature flavour 1 dataset to 'data'(example :move 'Signer_1' ,'Signer_2',..., 'Signer_30' to 'data')\
Step 4 : Run ``buildTrainingImageList.py``. This creates list of input files for training. (Only needed if you further need to train model)\
Step 5 : Run ``trainModel.py``. This starts the training process. (Only needed if you further need to train model)\
Step 6 : Run ``buildGenuineTestList.py``. This creates list of genuine signature images needed for exhaustive testing.\
Step 7 : Run ``testModel.py``. Check output file 'genuine_output'


**\*\*Exhautive testing on forgery images not yet done** \
**\*\*Files will be added/updated when further modifications will be done.**