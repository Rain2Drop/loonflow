from service.ticket.ticket_base_service import TicketBaseService


def create_lessons_make_sub_ticket():
    last_user, msg = TicketBaseService.get_ticket_state_last_man(ticket_id, 19)

    # workflow_id-子工单的对应的workflow transition_id-子工单对应的流转id
    # parent_ticket_state_id-父工单对应的状态id
    ticket_dict = dict(workflow_id=8, transition_id=21, username=last_user, parent_ticket_id=ticket_id,
                       parent_ticket_state_id=21, title='create by script - sub workflow demo1')
    TicketBaseService.new_ticket(ticket_dict, 'shutongflow')


    ticket_dict = dict(workflow_id=9, transition_id=23, username=last_user, parent_ticket_id=ticket_id,
                       parent_ticket_state_id=21, title='create by script - sub workflow demo2')
    TicketBaseService.new_ticket(ticket_dict, 'shutongflow')


create_lessons_make_sub_ticket()
