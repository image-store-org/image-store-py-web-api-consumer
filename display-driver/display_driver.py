from PIL import Image
from pathlib import Path
import time
import os
def ImportJpgs():
    path_tree = os.walk("display-driver/jpg")
    for elem in path_tree:
        print(elem)
        for idx in range(0,len(elem[2])):
            JpgToBmp(elem[0],elem[2][idx])

def JpgToBmp(path, filename):
    full_path = os.path.abspath(path+"/"+filename)
    image = Image.open(full_path)
    image_grey = image.convert(mode="L",colors=16)
    path_bmp = "display-driver/bmp"
    path_save = path_bmp+"/"+path.split("display-driver/jpg")[1]+"/"
    if not os.path.exists(path_save):
        os.makedirs(path_save)
    image_grey.save(os.path.abspath(path_save+filename.split(".jpg")[0]+".bmp"))

ImportJpgs()