import pymongo

from service.ticket.ticket_base_service import TicketBaseService

MONGO_URI = 'mongodb://host.docker.internal:20000'
MONGO_DB_NAME = 'ekweb'


def update_slides_make_field():
    topic_index, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'topic_index')
    db = pymongo.MongoClient(MONGO_URI)[MONGO_DB_NAME]

    topic_doc = db['topics'].find({'index': int(topic_index)})[0]
    topic_name = topic_doc.get('title')
    topic_id = topic_doc.get('_id')
    TicketBaseService.update_ticket_field_value(ticket_id, {'topic_name': topic_name})
    TicketBaseService.update_ticket_field_value(ticket_id, {'topic_id': topic_id})

    lessons_doc = db['lessons'].find({'topic': topic_id, 'internalOnly': True})[0]
    lesson_id = lessons_doc.get('_id')
    edit_slides_url = 'http://192.168.1.163:4000/yee/#/pcHome/editSlides/' + lesson_id
    TicketBaseService.update_ticket_field_value(ticket_id, {'edit_slides_url': edit_slides_url})


update_slides_make_field()
