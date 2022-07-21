params = dict()
params['short_access_token'] = ""
params['access_token'] = ""
params['app_id'] = ""
params['app_secret'] = ""

params['graph_domain'] = 'https://graph.facebook.com'
params['graph_version'] = 'v14.0'
params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
params['ig_username'] = 'simion.vase'
params['instagram_account_id'] = ""
params['page_id'] = ""


def get_parameters():
    return params
