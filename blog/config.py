import os
import socket

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fgkjnxlk/fmazkfmcnm'
    IS_PRODUCTION = socket.gethostname() == 'mouadhadji'
    FLASKR_SETTINGS = os.environ.get('FLASKR_SETTINGS') or ''
