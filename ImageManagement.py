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
    adjective = ["Awesome ", "Amazing ", "Excellent ", "Stunning ", "Cool ", "Lovely ", "Wonderful ", "Superb ",
                 "Spectacular ", "Great ", "Fantastic ", "Nice ", "Impressive ", "Fabulous ", "Splendid ",
                 "Captivating ", "Formidable ", "Enchanting "]

    wow_introduction = ["What a ", "Love this ", "Daaaamn, ", "", "", "", "", "", "", "", "", "", ""]

    object = ["image", "photo", "shot", "work", "picture", "frame", "snapshot", "composition", "capture", "scene"]

    congrats = [" Congrats!", " Congratulations!", " Good job!", " Well taken!", "", "", "", "", "", "", "", "", ""]

    sentence_start = ["The ", "Looking back at the ", "Remembering the ", "This picture reminds me of the ",
                      "We took some great pictures back in the ", "Thinking of the ", "It was one "]

    purpose = ["trip", "holiday", "excursion", "adventure", "vist"]

    nostalgia = [" We can't wait to go back there!", "It brings me back!", "Hope we get to revisit soon!"]

    hashtags = "\n\n\n\n#sony #sonyalpha #travel #citybreak #love #instagood #photooftheday #picoftheday" \
               "#beautiful #happy #cute #photography #nature #instadaily"

    location = image_path.split("/")[-2]
    caption = random.choice(sentence_start) + random.choice(adjective).lower() + random.choice(purpose) + \
              " we had in " + location + ".... " + random.choice(nostalgia) + hashtags
    return caption


def generate_simp_comment():
    adjective = ["Awesome ", "Amazing ", "Excellent ", "Stunning ", "Cool ", "Lovely ", "Wonderful ", "Superb ",
                 "Spectacular ", "Great ", "Fantastic ", "Nice ", "Impressive ", "Fabulous ", "Splendid ",
                 "Captivating ", "Formidable ", "Enchanting "]

    wow_introduction = ["What a ", "Love this ", "Daaaamn, ", "", "", "", "", "", "", "", "", "", ""]

    objective = ["image", "photo", "shot", "work", "picture", "frame", "snapshot", "composition", "capture", "scene"]

    congrats = [" Congrats!", " Congratulations!", " Good job!", " Well taken!", "Love you!", "", "", "", "", "", "",
                "", ""]

    caption = random.choice(wow_introduction) + random.choice(adjective) + random.choice(objective).lower() + \
              ", Simion!" + random.choice(congrats)

    return caption


def get_image_path(parent_folder):
    print(parent_folder)
    dir_list = os.listdir(parent_folder)
    subfolder = parent_folder + "/" + random.choice(dir_list)
    if len(os.listdir(subfolder)) == 0:
        os.rmdir(subfolder)
        subfolder = parent_folder + "/" + random.choice(dir_list)
    file_list = os.listdir(subfolder)
    return subfolder + "/" + random.choice(file_list)


if __name__ == "__main__":
    print(generate_simp_comment())

