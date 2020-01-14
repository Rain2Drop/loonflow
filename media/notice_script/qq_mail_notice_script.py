"""
loonflow在调用通知脚本时会将工单一些属性通过全局变量的方式传进来，所以在此脚本中可以直接使用。变量如下
globals = {'title_result': title_result, 'content_result': content_result,
                   'participant': ticket_obj.participant, 'participant_type_id': ticket_obj.participant_type_id,
                   'multi_all_person': ticket_obj.multi_all_person, 'ticket_value_info': ticket_value_info,
                   'last_flow_log': last_flow_log, 'participant_info_list': participant_info_list}

"""
from email.header import Header
from email.mime.text import MIMEText
import smtplib

smtp_server = 'smtp.exmail.qq.com'  # 腾讯服务器地址
from_addr = 'system_noreply@ek12.com'
with open('/run/secrets/smtp_password', 'rt') as f:
    password = f.read().strip()


def email_notice_script_call():
    email_set = set()
    for participant_info in participant_info_list:
        email_set.add(participant_info['email'])

    for email in email_set:
        send_mail(email, title_result, content_result)


def send_mail(to_addr, subject, context):
    # 内容初始化，定义内容格式（普通文本，html）
    msg = MIMEText(context, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr

    # 邮件标题
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # 服务端配置，账密登陆
    server = smtplib.SMTP_SSL(smtp_server, 465)

    # 登陆服务器
    server.login(from_addr, password)

    # 发送邮件及退出
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送地址需与登陆的邮箱一致
    server.quit()


email_notice_script_call()
