import Config as Cfg
import base64
import requests
import os
import random
from PIL import Image
import math
import openai


def use_open_ai_for_caption(prompt):
    params = Cfg.get_parameters("test")
    openai.api_key = params['openai_key']
    prompts = [{"role": "system",
                "content": 'You create instagram picture description. The descriptions are very short and generic while using good words for SEO. You also add hashtags to make the picture popular. Do not use quotes'},
               {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompts,
    ).choices[0].message.content
    return response


def use_open_ai_for_commenting(prompt):
    params = Cfg.get_parameters("test")
    openai.api_key = params['openai_key']
    prompts = [{"role": "system",
                "content": 'You write comments to a specific user on instagram, you are very short and generic while using good words for SEO. You add emojys. Do not use quotes'},
               {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompts,
    ).choices[0].message.content
    return response


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
        resize_factor = math.sqrt(6000000 / image_size)
        new_image = original_image.resize((int(width * resize_factor), int(height * resize_factor)))
        new_image.save(image_location)
        print("Image has been resized")
    else:
        print("Original image was small enough")


def check_if_valid_ratio(image_location):
    original_image = Image.open(image_location)
    width, height = original_image.size
    if (0.8 < (height / width) < 1.91) or (0.8 < (width / height) < 1.91):
        return True
    else:
        print("Image had ratios too off ", image_location)
        return False


def generate_image_caption(image_path):
    location = image_path.split("/")[-2]
    text_user = "Create a description for a picture take in " + location + \
                ", be generic, end with a question to gain interactions. Do not use quotes"
    response = use_open_ai_for_caption(text_user)
    return response


def generate_simp_comment(name="Simion", content="landscape"):
    text_user = "Create a praise for this picture taken by " + name + ", the picture is of a " + content
    response = use_open_ai_for_commenting(text_user)
    return response


def generate_ai_portrait_text():
    orase_cu_ai = ["Alba Iulia", "Braila", "Aiud", "Craiova", "Baia Mare", "Gataia", "Mihailesti", "Valea lui Mihai",
                   "Strehaia", "Sinaia", "Sangeorz-Bai", "Podu Iloaoiei", "Bailesti", "Baile Tusnad", "Baile Olanesti",
                   "Baile Herculane", "Baile Govora", "Baia Sprie", "Baia Aries", "Baia de Arama"]

    text_user = "Create a description, in Romanian, for a portrait take in " + random.choice(orase_cu_ai) + \
                ", be generic, end with a question to gain interactions"
    response = use_open_ai_for_caption(text_user)
    return response


def get_image_path(parent_folder):
    # print(parent_folder)
    dir_list = os.listdir(parent_folder)
    subfolder = parent_folder + "/" + random.choice(dir_list)
    if len(os.listdir(subfolder)) == 0:
        os.rmdir(subfolder)
        subfolder = parent_folder + "/" + random.choice(dir_list)
    file_list = os.listdir(subfolder)
    return subfolder + "/" + random.choice(file_list)


if __name__ == "__main__":
    print(generate_simp_comment("@vase.simion", "landscape"))
    print(generate_image_caption("Instagram/Peru/Dsc.jpg"))
    print(generate_ai_portrait_text())

