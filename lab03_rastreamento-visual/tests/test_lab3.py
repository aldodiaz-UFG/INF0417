import os
import glob
import INF0417_labs.lab1 as lab1
from INF0417_labs import IMAGE_DIRECTORY
import PIL

def test_cameraman():
    cameraman = lab1.get_cameraman()
    assert len(cameraman) == 3
    assert cameraman[0].shape == (236,236)
    assert cameraman[2] == (1,-2)

def test_load_lab_image():
    pngs = [os.path.basename(im) for im in glob.glob(f"{IMAGE_DIRECTORY}/*.png")]
    for png in pngs:
        random_im = lab1.load_lab_image(png)