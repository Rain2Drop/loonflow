import hashlib
import os

from service.ticket.ticket_base_service import TicketBaseService

import requests
import json

LOONFLOW_YEE_URL = os.environ['LOONFLOW_YEE_URL']


def update_topic_doc():
    user_name, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'make_slides_assignee')
    topic_id, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'topic_id')

    slides_file, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'slides_file')
    slides_object = json.loads(slides_file)

    update_doc(user_name, topic_id, slides_object[0]['url'], slides_object[0]['name'])


def update_doc(user_name, topic_id, url, original_name):
    sha256 = hashlib.sha256()
    with open('/run/secrets/yee_internal_secret', 'rt') as f:
        secret = f.read().strip()
    sha256.update(secret.encode('utf-8'))
    res = sha256.hexdigest()

    post_data = dict(username=user_name, internal_secret=res)
    resp = requests.post(LOONFLOW_YEE_URL + 'yee/api/v1/authorizations', json=post_data).json()
    token = resp['token']

    url_tokens = url.split("/")
    headers = {'Authorization': 'Bearer ' + token}
    post_data = dict(id=topic_id, original_name=original_name, key=url_tokens[len(url_tokens) - 1], refer=True)
    resp = requests.post(LOONFLOW_YEE_URL + 'yee/api/v1/users/' + user_name + '/topics/' + topic_id + '/docs',
                         json=post_data, headers=headers)
    if not resp.ok:
        raise Exception('更新Topic对应的课件信息失败')


update_topic_doc()
# update_doc('admin', 'CxfyobwYLK9nzCxfy',
#            'https://rain2drop-workflow.oss-cn-shanghai.aliyuncs.com/FmvDJNctTKbREcNaiV0-9az9Ki-r.txt', 'sql.txt')
