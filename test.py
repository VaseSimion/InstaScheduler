import os
import random
import ImageManagement as Im
from PIL import Image
import math


if __name__ == "__main__":
    photo_folder = "D:\\Exported photos"
    dir_list = os.listdir(photo_folder)
    print(dir_list)
    subfolder = photo_folder + "\\" + random.choice(dir_list)
    print(subfolder)
    file_list = os.listdir(subfolder)
    print(file_list)

