from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from string import Template
from config import (
    EMAIL_FROM,
    OWNER_CONTACT,
    OWNER_SIGN,
    GMAP_LINK,
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USN,
    SMTP_PWD
)

def __mapping_side(x: str) -> str:
    return {
        'groom': 'ฝ่ายเจ้าบ่าว',
        'bride': 'ฝ่ายเจ้าสาว',
        'both': 'ทั้งคู่'
    }.get(x, '-')

def send_rsvp_email(full_name: str, mail: str, side: str, guest: str, status: str = '') -> None:
    msg = MIMEMultipart()
    msg['From'] = formataddr(("Aon & Bank Wedding", EMAIL_FROM))
    msg['To'] = mail
    msg['Subject'] = 'การยืนยันการลงทะเบียนงานแต่งงาน'
    data = {
        'full_name': full_name,
        'owner_contact': OWNER_CONTACT,
        'owner_sign': OWNER_SIGN
    }
    if status == 'accept':
        file_tpl = './templates/accept.tpl'
        data.update({
            'map_link': GMAP_LINK,
            'side': __mapping_side(side),
            'guest': guest,
        })
    elif status == 'decline':
        file_tpl = './templates/decline.tpl'
    else:
        return

    try:
        with open(file_tpl, "r", encoding="utf-8") as file:
            content = file.read()
        message = Template(content).substitute(**data)
        msg.attach(MIMEText(message, 'html'))

        with SMTP(SMTP_SERVER, SMTP_PORT) as mailserver:
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.login(SMTP_USN, SMTP_PWD)
            mailserver.sendmail(EMAIL_FROM, mail, msg.as_string())
    except Exception as e:
        raise Exception(f"Failed to send email to {mail}: {e}")
