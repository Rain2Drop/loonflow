import pymongo
import os

from service.ticket.ticket_base_service import TicketBaseService

MONGO_URI = 'mongodb://host.docker.internal:20000'
MONGO_DB_NAME = 'ekweb'
LOONFLOW_YEE_URL = 'https://www.rain2drop.com/'


def update_slides_make_ticket_field():
    topic_index, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'topic_index')
    db = pymongo.MongoClient(MONGO_URI)[MONGO_DB_NAME]

    topic_doc = db['topics'].find({'index': int(topic_index)})[0]
    topic_name = topic_doc.get('title')
    topic_id = topic_doc.get('_id')
    TicketBaseService.update_ticket_field_value(ticket_id, {'topic_name': topic_name, 'topic_id': topic_id,
                                                            'title': '课件制作:' + topic_index + '-' + topic_name})

    # 有参考视频的时候提供截图链接
    count = db['lessons'].count_documents({'topic': topic_id, 'internalOnly': True})

    if count > 0:
        lessons_doc = db['lessons'].find({'topic': topic_id, 'internalOnly': True})[0]
        lesson_id = lessons_doc.get('_id')
        edit_slides_url = LOONFLOW_YEE_URL + 'yee/#/pcHome/editSlides/' + lesson_id
        TicketBaseService.update_ticket_field_value(ticket_id, {'edit_slides_url': edit_slides_url})
    else:
        TicketBaseService.update_ticket_state(ticket_id, 9, '脚本')

update_slides_make_ticket_field()
