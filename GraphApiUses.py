import json
import time
import Config as Cfg
import requests


def image_upload(image_link, image_caption, account="main"):
    if account == "main":
        params = Cfg.get_parameters("main")
    else:
        params = Cfg.get_parameters("test_account")

    # Create a container
    upload = dict()
    upload['image_url'] = str(image_link)
    upload['caption'] = image_caption
    upload['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] + "/media"
    creation_id = requests.post(url, upload)
    container_id = creation_id.json()['id']

    # Upload the container
    url = params['endpoint_base'] + params['instagram_account_id'] + "/media_publish"
    image_params = dict()
    image_params['creation_id'] = str(container_id)
    image_params['access_token'] = params['access_token']
    response = requests.post(url, image_params)
    print(response.json())
    return response


def get_insights(account="main"):
    if account == "main":
        params = Cfg.get_parameters("main")
    else:
        params = Cfg.get_parameters("test_account")
    # Define url
    url = params['endpoint_base'] + params['instagram_account_id'] + "/media"

    # Define Endpoint Parameters
    endpoint_params = dict()
    endpoint_params['fields'] = ''
    endpoint_params['access_token'] = params['access_token']

    # Requests Data
    data = requests.get(url, endpoint_params)
    print(data.json())

    url = params['endpoint_base'] + params['instagram_account_id']

    # Define Endpoint Parameters
    endpoint_params = dict()
    endpoint_params['fields'] = 'id,website,username,biography,ig_id,' \
                                'followers_count, media_count, name, profile_picture_url'
    endpoint_params['access_token'] = params['access_token']

    # Requests Data
    data = requests.get(url, endpoint_params)
    print(data.json())
    return json.loads(data.content)


def get_used_quota(account="main"):
    if account == "main":
        params = Cfg.get_parameters("main")
    else:
        params = Cfg.get_parameters("test_account")
    # define url
    url = params['endpoint_base'] + params['instagram_account_id'] + "/" + "content_publishing_limit"

    # define parameters
    endpoint_params = dict()
    endpoint_params['fields'] = 'quota_usage,rate_limit_settings'
    endpoint_params['access_token'] = params['access_token']
    endpoint_params['since'] = str(int(time.time())-86300)

    # Requests Data
    data = requests.get(url, endpoint_params)
    print("The daily quota usage is at ", data.json()['data'][0]['quota_usage'])
    return data.json()['data'][0]['quota_usage']


if __name__ == "__main__":
    print(get_used_quota(False))
