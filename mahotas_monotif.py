# -*- coding: cp1252 -*-
import numpy as np
import mahotas

# Ouverture d'un tif simple
img_single = mahotas.imread(r'E:\images\tif_simple.tif')
# Obtention des dimensions de l'image
print np.shape(img_single)
