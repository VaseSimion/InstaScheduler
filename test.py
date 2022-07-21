import requests
import json
import Config as Cfg


def fb_test():
    params = Cfg.params
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
