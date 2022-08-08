import Config as Cfg
import base64
import requests
import os
import random
from PIL import Image
import math


def img_bb_image_upload(image_path):
    params = Cfg.get_parameters("test")
    key = params['imgbb_key']
    manage_image_size(image_path)
    with open(image_path, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        return res.json()['data']['url']


def manage_image_size(image_location):
    image_size = os.path.getsize(image_location)
    original_image = Image.open(image_location)
    width, height = original_image.size
    if image_size > 6000000:
        resize_factor = math.sqrt(6000000/image_size)
        new_image = original_image.resize((int(width*resize_factor), int(height*resize_factor)))
        new_image.save(image_location)
        print("Image has been resized")
    else:
        print("Original image was small enough")


def check_if_valid_ratio(image_location):
    original_image = Image.open(image_location)
    width, height = original_image.size
    if (0.8 < (height/width) < 1.91) or (0.8 < (width/height) < 1.91):
        return True
    else:
        print("Image had ratios too off ", image_location)
        return False


def generate_image_caption(image_path):
    caption = "Something that has to be created using the path " + image_path
    return caption


def get_image_path(parent_folder):
    files = os.listdir(parent_folder)

    return random.choice(list(files))
