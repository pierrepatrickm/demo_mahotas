# -*- coding: cp1252 -*-

import numpy as np
from mahotas.io import freeimage
from mahotas.io.freeimage import imread,imsave

# Chargement d'un TIF multipages constituant un stack
img_stack = freeimage.read_multipage('E:\images\tif_multipages.tif',0)
# Obtention des dimensions du stack
print np.shape(img_stack)

# Calcul de l'image moyenne du stack
time_averaged_stack = np.mean(img_stack, 0).astype(np.uint16)
# Sauvegarde de l'image moyenne du stack
freeimage.imsave('E:\images\image_moyenne_stack.tif', time_averaged_stack)
print np.shape(time_averaged_stack)



