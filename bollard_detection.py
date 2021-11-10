# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 03:21:25 2021

@author: ajitj
"""

#%%
# example of inference with a pre-trained coco model
#import mrcnn
#import mrcnn.config
#import mrcnn.model
#import mrcnn.visualize
import os

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from mrcnn.visualize import display_instances
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from matplotlib import pyplot 
from matplotlib.patches import Rectangle
import numpy as np
import cv2
# define 81 classes that the coco model knowns about
class_names = ['BG', 'car']
 
# define the test configuration
class TestConfig(Config):
     NAME = "test"
     GPU_COUNT = 1
     IMAGES_PER_GPU = 1
     NUM_CLASSES = 1 + 1
 
# define the model
rcnn = MaskRCNN(mode='inference', model_dir='../', config=TestConfig())

# Initialize the Mask R-CNN model for inference and then load the weights.
# This step builds the Keras model architecture.
#rcnn = MaskRCNN(mode="inference", 
#                             config=TestConfig(),
#                             model_dir=os.getcwd())





# load coco model weights
#rcnn.load_weights(r'C:\Users\ajitj\OneDrive - Universitetet i Agder\Teaching\MasterProgram\Applied ML and Robotics\MAS512-G_AJ_2021\CNN_ML\ObjectDetection\mask_rcnn_balloon_0003.h5', by_name=True)
rcnn.load_weights(r'C:\Users\Lise\Documents\Silje\OD\ObjectDetection\mask_rcnn_balloon_0010.h5', by_name=True) #aj replace by trained model
#load image
img = load_img(r'C:\Users\Lise\Documents\Silje\OD\ObjectDetection\Lepton_Capture_41.jpeg')# aj replace by car image
img = img_to_array(img)
# make prediction
results = rcnn.detect([img], verbose=0) #AJ print to see the details
# get dictionary for first prediction
r = results[0]
#Extract the first bbox;  (x1, y1) refer to the top left corner and (x2, y2) the bottom right corner
print (r['rois'][0])
# show photo with bounding boxes, masks, class labels and scores
display_instances(img, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])


#%%
#validate multiple images
import os
#from PIL import Image

#val_path=(r'C:\Users\ajitj\OneDrive - Universitetet i Agder\TensorFlow_Bollard\MaskRNN_Org\Mask_RCNN\images\val')
#val_path=(r'C:\Users\ajitj\OneDrive - Universitetet i Agder\TensorFlow_Bollard\MaskRNN_Org\Mask_RCNN\images\val\image_104_scaled.png')#image_104_scaled.png
# val_path=(r'C:\Users\Lise\Documents\Silje\MAS512_G_Lab\ObjectDetection\images\val')

# files = [i for i in os.listdir(val_path) if os.path.isfile(os.path.join(val_path,i))] #list of all files in val_path
# #print (files)
# val_list=[x for x in range(2)] # 1; 19,20; 18,20 select range of images for validation make 1000,1002 to select other images 1000,1008
# val_files = [] # validation images
# val_image_path=[] # validation image path
# counter=0 #counter for increasing the index in val_files to iterate through different images to validate
# weight='mask_rcnn_balloon_0003.h5'
# #title=['MaskRnn_%s;%s'%(weight,val_files)]
# for i in files:
#     for j in val_list:
#         if ('image_%d_scaled' %(j) in i): #image_%d_scaled
#             val_files.append(i)
#             val_image_path.append(os.path.join(val_path, val_files[counter][:])) #0
#             counter=counter+1
#     val_image=[] #validation image 
# for filename in val_image_path:
#     val_im=load_img(filename)
#     #val_image.append(val_im)
#     img1 = img_to_array(val_im)
#     # make prediction
#     results1 = rcnn.detect([img1], verbose=0) #AJ print to see the details
#     # get dictionary for first prediction
#     r1 = results1[0]
#     #make title for image
#     title='MaskRnn_%s'%(weight)
#     title1=title+';'+os.path.basename(filename)
#     # show photo with bounding boxes, masks, class labels and scores
#     display_instances(img1, r1['rois'], r1['masks'], r1['class_ids'], class_names, r1['scores'], title1, figsize=(8, 8)) 
#     #to change the label and score text colour to blue (default is 'w)' -- visualize.py line 147 - color='b'
#     #ax.text(x1, y1 + 8, caption, color='b', size=11, backgroundcolor="none") --to change the text location adjist x1 and y1 in this syntax
#     # the r1['rois'] gives bb co-ordingate - y1,x1, y2, x2. These refer to the top let and bottom right corner respectively

