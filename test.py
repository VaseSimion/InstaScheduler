import requests
import json
import Config as Cfg
import base64
import requests


def fb_test():
    params = Cfg.get_parameters("test")
    # Define url
    url = params['endpoint_base'] + params['instagram_account_id']

    # Define Endpoint Parameters
    endpoint_params = dict()
    endpoint_params['fields'] = 'id,website,username,biography,ig_id,' \
                                'followers_count, media_count, name, profile_picture_url'
    endpoint_params['access_token'] = params['access_token']

    # Requests Data
    data = requests.get(url, endpoint_params)
    basic_insight = json.loads(data.content)
    print(basic_insight)

    upload = dict()
    upload['image_url'] = "https://i.ibb.co/XsGYzHY/DSC04951.jpg"
    upload['caption'] = "The perfect caption to the picure I want"
    upload['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] +"/media"

    creation_id = requests.post(url, upload)
    print(creation_id)
    container_id = creation_id.json()['id']
    url = params['endpoint_base'] + params['instagram_account_id'] +"/media_publish"
    image_params = dict()
    image_params['creation_id'] = str(container_id)
    image_params['access_token'] = params['access_token']
    response = requests.post(url, image_params)

    print(response)


def image_test():
    params = Cfg.get_parameters("test")
    key = params['imgbb_key']
    image_path = "DSC04389-2.jpg"

    with open(image_path, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        return res.json()['data']['url']
