from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import shutil
import os, re

pylab.rcParams['figure.figsize'] = (8.0, 10.0)
imgDir='../images'
dataDir='..'
dataType=['val2017', 'train2017']
annFile1='{}/annotations/instances_{}.json'.format(dataDir,dataType[0])
annFile2='{}/annotations/instances_{}.json'.format(dataDir,dataType[1])
coco1 = COCO(annFile1)
coco2 = COCO(annFile2)

catIds1 = coco1.getCatIds(catNms=['elephant'])
catIds2 = coco2.getCatIds(catNms=['elephant'])

imgIds1 = coco1.getImgIds(catIds=catIds1)
imgIds2 = coco2.getImgIds(catIds=catIds2)

print (len(imgIds1))
print (len(imgIds2))

source = 'annotations_pascalformat'
dest1 = 'elephants'
dest2 = 'elephantsIMG'

files = os.listdir(source)

fuk = 0

for i in range(len(imgIds1)):
  s = str(imgIds1[i]).zfill(12)
  try:
    shutil.copy(source + '/' + s + '.xml', dest1)
    shutil.copy(imgDir + '/' + s + '.jpg', dest2)
  except:
    fuk+=1
    continue
for i in range(len(imgIds2)):
  try:
    s = str(imgIds2[i]).zfill(12)
    shutil.copy(source + '/' + s + '.xml', dest1)
    shutil.copy(imgDir + '/' + s + '.jpg', dest2)
  except:
    fuk+=1
    continue
print (fuk)
