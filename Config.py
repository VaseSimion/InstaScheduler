# curl -i -X GET "https://graph.facebook.com/v14.0/17841402344136693?fields=biography%2Cid%2Cusername%2Cwebsite&access_token={EAAR5PFHQ3ewBANBEaP6eab4opaHQkgNcnVKggT2zZBSu6jOkieLbFVAwLFeqEODSB8WR0AcFLucQpaPTooSv8MuZCgFwjANZCMpb9TAO5E86vcctCpRyyP5VEqnQgZBaWZB83tGB3yvei2Hd4BCvNpZBew1F716hfzNJZB18xcqWy1YtATFVMZCd}


def get_parameters(whom):
    params = dict()
    params['graph_domain'] = 'https://graph.facebook.com'
    params['graph_version'] = 'v14.0'
    params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
    params['imgbb_key'] = "XX"

    if whom == "main":
        params['app_id'] = "XX"
        params['app_secret'] = "XX"
        params['short_access_token'] = 'XX'
        params['access_token'] = "XX"
        params['ig_username'] = 'XX.XX'
        params['instagram_account_id'] = 'XX'
        params['page_id'] = 'XX'
    else:
        params['app_id'] = "XX"
        params['app_secret'] = "XX"
        params['short_access_token'] = "XX"
        params['access_token'] = "XX"
        params['ig_username'] = 'X.X.X.X.X'
        params['instagram_account_id'] = 'XX'
        params['page_id'] = 'XX'
    return params


#curl -i -X GET "https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={appID}&client_secret={AppSecret}&fb_exchange_token={AppToken}"