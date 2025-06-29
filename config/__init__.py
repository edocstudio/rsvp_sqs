from os import getenv

EMAIL_FROM = getenv('EMAIL_FROM')
OWNER_CONTACT = getenv('OWNER_CONTACT')
OWNER_SIGN = getenv('OWNER_SIGN')
GMAP_LINK = getenv('GMAP_LINK')
SMTP_SERVER = getenv('SMTP_SERVER')
SMTP_PORT = int(getenv('SMTP_PORT', '0'))
SMTP_USN = getenv('SMTP_USN')
SMTP_PWD = getenv('SMTP_PWD')