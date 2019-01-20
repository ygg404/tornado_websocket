#coding=utf-8
from .main_handler import *

handlers = [
    (r'/ChatRoom', ChatRoom),
    (r'/ChatHandler', ChatHandler),
]

# handlers += user_urls
