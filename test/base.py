import requests

import config


host = '127.0.0.1'


def request(method, end_point, **kwargs):
    url = f'http://{host}:{config.PORT}/{end_point}'
    resp = requests.request(method=method, url=url, **kwargs)
    print(resp.status_code)
    return resp
