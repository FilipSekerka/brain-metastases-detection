import h5py
import numpy as np
import os, os.path
from matplotlib import pyplot as plt
from skimage.transform import resize

# imgs = []
# path = os.path.join("deep learning models", "data", "imgTrn")
# valid_images = [".jpg", ".gif", ".png", ".tga"]
# count = 0
# for f in os.listdir(path):
#     count += 1
#     if count > 10:
#         break
#     file_name = os.path.join(path, f)
#     arr = plt.imread(file_name)
#     resized_arr = resize(arr, (256, 256))
#     imgs.append(resized_arr)
#
# data = np.array(imgs)[:, :, :, 0]
# print(data.shape)
#
# f1 = h5py.File("deep learning models/data/imgVal.h5", "w")
# dset1 = f1.create_dataset("dataset_01", (10, 256, 256), dtype='i', data=data)
# f1.close()


count = 0
new_file = [['image_name', 'xmin', 'xmax', 'ymin', 'ymax', 'class_id']]
with open("data/labels_trn.csv") as file:
    file.readline()

    for line in file:
        line = line.rstrip()
        count += 1
        if count > 10:
            break

        values = line.split(",")
        new_file.append([str(count)] + values[3:] + ["0"])
        # new_file.append([values[0]] + values[3:] + ["0"])

with open("data/labels_trn_new.csv", "w") as file:
    for line in new_file:
        print(",".join(line), file=file)

with open("data/labels_val_new.csv", "w") as file:
    for line in new_file:
        print(",".join(line), file=file)
