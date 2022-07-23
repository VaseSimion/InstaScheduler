import requests
import json
import Config as Cfg


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
    upload['image_url'] = "https://i.postimg.cc/Hxr0mXYd/DSC04936.jpg"
    upload['caption'] = "This just might be it!"
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



