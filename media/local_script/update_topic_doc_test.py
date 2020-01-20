import hashlib
from datetime import datetime

import requests

LOONFLOW_YEE_URL = 'https://www.rain2drop.com/'


def update_doc(user_name, topic_id, url, original_name):
    sha256 = hashlib.sha256()
    sha256.update('xiao9BENBEN'.encode('utf-8'))
    res = sha256.hexdigest()

    post_data = dict(username=user_name, internal_secret=res)
    resp = requests.post(LOONFLOW_YEE_URL + 'yee/api/v1/authorizations', json=post_data).json()
    token = resp['token']

    url_tokens = url.split("/")
    headers = {'Authorization': 'Bearer ' + token}
    post_data = dict(id=topic_id, original_name=original_name, key=url_tokens[len(url_tokens) - 1],
                     submitted=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), refer=True)
    resp = requests.post(LOONFLOW_YEE_URL + 'yee/api/v1/users/' + user_name + '/topics/' + topic_id + '/docs',
                         json=post_data, headers=headers)
    if not resp.ok:
        raise Exception('更新Topic对应的课件信息失败')



update_doc('admin', 'CxfyobwYLK9nzCxfy',
           'https://rain2drop-workflow.oss-cn-shanghai.aliyuncs.com/FmvDJNctTKbREcNaiV0-9az9Ki-r.txt', 'sql.txt')
