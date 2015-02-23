__author__ = 'kuasha'

"""
230,75-270,125

237,82 - 266,122
29x40
"""
import numpy as np
from scipy import misc
from sklearn import datasets
from sklearn import svm
from sklearn import cluster

img=misc.imread("/Users/kuasha/Downloads/people.jpg")

print img.shape
print img.dtype

start = [(77, 230), (127, 270)]
cell_width = 29.5
cell_fl_start = 230
cell_crop_width = 40

cell_row_start = 77
cell_crop_height = 50
cell_height = 40

section_height = 309

images = []


for section in range(0,5):
    for c in range(0,6):
        for i in range(0,34):

            ys = cell_row_start+c*cell_height + section * section_height
            ye = cell_row_start+cell_crop_height+c*cell_height + section * section_height

            fc = img[ys:ye,
                 cell_fl_start+int(i*cell_width):(cell_fl_start+cell_crop_width)+int(i*cell_width), :]

            images.append(fc)

            #misc.imsave("fl"+str(section)+"_"+str(c)+"_"+str(i)+".jpg", fc)
#images.reshape((-1, 40*50))
images=np.asarray(images)
print images
images.reshape(1,-1)
print images.shape
k_means = cluster.KMeans(n_clusters=10, n_init=1)
k_means.fit(images)


