import cv2
import numpy as np
import os

folder_path = './assets'

resize_folder_path = os.path.join(folder_path, 'resize')
if not os.path.exists(resize_folder_path):
    os.makedirs(resize_folder_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        img = cv2.imread(os.path.join(folder_path, filename))

        height, width, channels = img.shape
        new_height = height + 120
        new_width = width + 120

        new_img = np.zeros((new_height, new_width, channels), np.uint8)
        new_img[:] = (255, 255, 255)

        new_img[60:new_height-60, 60:new_width-60] = img

        resized_img = cv2.resize(new_img, (1000, 1000))

        output_filename = os.path.join(
            resize_folder_path, filename)

        cv2.imwrite(output_filename, resized_img)

print('Done.')
