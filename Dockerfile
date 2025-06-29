FROM public.ecr.aws/lambda/python:3.13

ENV EMAIL_FROM=
ENV OWNER_CONTACT=
ENV OWNER_SIGN=
ENV GMAP_LINK=
ENV SMTP_SERVER=
ENV SMTP_PORT=
ENV SMTP_USN=
ENV SMTP_PWD=

COPY common common
COPY config config
COPY main.py .
COPY templates templates

CMD [ "main.lambda_handler" ]