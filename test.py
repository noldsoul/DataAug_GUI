import os
import numpy as np
import pandas as pd
import glob
import argparse
import shutil


# # parser.add_argument('')

# # images = sorted(glob.glob(path + '/' + '*.jpg'))
# # masks  = sorted(glob.glob(path + '/' + '*.png'))
# path = '/home/chandradeep_p/Desktop/datasets/Mapillary/data_augmentation/images'
# mask_path = ['/home/chandradeep_p/Desktop/datasets/Mapillary/validation/labels', '/home/chandradeep_p/Desktop/datasets/Mapillary/training/labels']
# image_list = []
# mask_list_1 = []
# mask_list_2 = []

# ###### Appending style images


# ####### Appending mask_validation
# for orig_root, dirs_, files in os.walk(mask_path[0], topdown=False):
#     for filename in files:
#         # print(root+ '/'+ filename)
#         mask_list_1.append(filename)
# ###### Appending mask_train
# for orig_root, dirs_, files in os.walk(mask_path[1], topdown=False):
#     for filename in files:
#         # print(root+ '/'+ filename)
#         mask_list_2.append(filename)


# #### Searching for masks for images
# for orig_root, dirs, files in os.walk(path, topdown=False):
#     for filename in files:
#             if filename.endswith('.jpg'):
#                 count = 0
#                 mask_name = filename.split('.')[0] + '.png'
#                 if (mask_name in mask_list_1):
#                         shutil.copyfile(mask_path[0] + '/' + mask_name, orig_root + '/' + mask_name )
#                         count+=1
#                 elif ((mask_name in mask_list_2)):
#                         shutil.copyfile(mask_path[1] + '/' + mask_name, orig_root + '/' + mask_name )
#                         count+=1


# #### Conversion of jpg to PNG for model
# from PIL import Image
# path = '/home/chandradeep_p/Desktop/datasets/Mapillary/data_augmentation/styles/images'
# for orig_root, dirs, files in os.walk(path, topdown=False):
#     for filename in files:
#             if filename.endswith('.jpg'):
#                 image = Image.open(orig_root + '/' + filename)
#                 image.save(orig_root + '/' + filename.split('.')[0] + '.png')
#                 os.remove(orig_root + '/' + filename)
#                 print('Processing ',filename)

                        
# ############ For content image
# from PIL import Image
# path = '/home/chandradeep_p/Desktop/datasets/Mapillary/training/images'
# des_path ='/home/chandradeep_p/Desktop/datasets/Mapillary/data_augmentation/content/converted_png_image'
# color_label_dest = '/home/chandradeep_p/Desktop/datasets/Mapillary/data_augmentation/content/color_labels'
# color_label_src = '/home/chandradeep_p/Desktop/datasets/Mapillary/training/labels'
# count = 0
# for orig_root, dirs, files in os.walk(path, topdown=False):
#     for filename in files:
#             if filename.endswith('.jpg'):
#                 image = Image.open(orig_root + '/' + filename)
#                 image.save(des_path + '/' + filename.split('.')[0] + '.png')
#                 shutil.copyfile(color_label_src + '/' + filename.split('.')[0] + '.png',color_label_dest + '/' + filename.split('.')[0] + '.png' )
#                 print('Processing ',filename)
#                 count+=1
#                 if count > 10:
#                         break

######## Style copying
style_image_path = '/home/deeplearning/Desktop/chandradeep/data_augmentation/styles/images/fog/AJDLKgfDEjp4bx49JIRg7A.png'
style_label_path ='/home/deeplearning/Desktop/chandradeep/data_augmentation/styles/color_labels/fog/AJDLKgfDEjp4bx49JIRg7A.png'

image_des_path ='/home/deeplearning/Desktop/chandradeep/data_augmentation/input_dataset/style_images'
label_des_path = '/home/deeplearning/Desktop/chandradeep/data_augmentation/input_dataset/style_labels'
path = '/home/deeplearning/Desktop/chandradeep/data_augmentation/input_dataset/content_images'
count = 0
for orig_root, dirs, files in os.walk(path, topdown=False):
    for filename in files:
            if filename.endswith('.png'):
                    shutil.copyfile(style_image_path, image_des_path + '/' + filename)
                    shutil.copyfile(style_label_path, label_des_path + '/' + filename)