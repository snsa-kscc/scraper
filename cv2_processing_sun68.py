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

        top_left = (300, 300)
        bottom_right = (2700, 2700)

        cropped_image = img[top_left[1]:bottom_right[1],
                            top_left[0]:bottom_right[0]]

        resized_img = cv2.resize(cropped_image, (1000, 1000))

        output_filename = os.path.join(
            resize_folder_path, filename)

        cv2.imwrite(output_filename, resized_img)

print('Done.')
