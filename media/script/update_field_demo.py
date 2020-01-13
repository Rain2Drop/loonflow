from service.ticket.ticket_base_service import TicketBaseService


def update_field():
    title, msg = TicketBaseService.get_ticket_field_value(ticket_id, 'title')  # ticket_id会通过exec传过来

    TicketBaseService.update_ticket_field_value(ticket_id, {'title': title + title})


update_field()
