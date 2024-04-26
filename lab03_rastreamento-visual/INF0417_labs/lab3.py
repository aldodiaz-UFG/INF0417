from pathlib import Path
import os
import numpy as np
from PIL import Image
from INF0417_labs import IMAGE_DIRECTORY

def load_lab_image(filename):
    """ Load a grayscale image by filename from the INF0417 image directory

    Example:
    >>> img = load_lab_image('cornertest.png')
    """

    path = str(IMAGE_DIRECTORY / filename)

    return np.asarray(Image.open(path).convert('L'))

def get_cameraman():
    """ Return I, J and true (col, row) displacement
    """

    n = 10 # Border crop
    img = load_lab_image('cameraman.tif')
    I = img[n:-n, n:-n]
    x, y = 1, -2
    J = img[n-y:-n-y, n-x:-n-x]
    assert I.shape == J.shape

    return I, J, (x, y)