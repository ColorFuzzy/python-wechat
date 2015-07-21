# -*- coding: utf-8 -*-

""" Wechat server constants and limits

"""


class MsgType(object):
    """Wechat user message types
    wiki1: http://mp.weixin.qq.com/wiki/10/79502792eef98d6e0c6e1739da387346.html
    wiki2: http://mp.weixin.qq.com/wiki/2/5baf56ce4947d35003b86a9805634b1e.html

    """

    text = "text"
    image = "image"
    voice = "voice"
    video = "video"
    shortvideo = "shortvideo"
    location = "location"
    link = "link"
    event = "event"


class EventType(object):
    """Wechat user message event types
    wiki: http://mp.weixin.qq.com/wiki/2/5baf56ce4947d35003b86a9805634b1e.html

    """

    subscribe = "subscribe"
    unsubscribe = "unsubscribe"
    SCAN = "SCAN"
    LOCATION = "LOCATION"
    CLICK = "CLICK"
    VIEW = "VIEW"
