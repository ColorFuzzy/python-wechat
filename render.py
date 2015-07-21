# -*- coding: utf-8 -*-

""" Text for jinja to render Wechat reply

"""

import time
from jinja2 import Template


TEXT_TPL = u"""
<xml>
<ToUserName><![CDATA[{{ ToUserName }}]]></ToUserName>
<FromUserName><![CDATA[{{ FromUserName }}]]></FromUserName>
<CreateTime>{{ CreateTime }}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{{ Content }}]]></Content>
</xml>
"""

IMAGE_TPL = u"""
<xml>
<ToUserName><![CDATA[{{ ToUserName }}]]></ToUserName>
<FromUserName><![CDATA[{{ FromUserName }}]]></FromUserName>
<CreateTime>{{ CreateTime }}</CreateTime>
<MsgType><![CDATA[image]]></MsgType>
<Image>
<MediaId><![CDATA[{{ MediaId }}]]></MediaId>
</Image>
</xml>
"""


class MsgRender(object):

    @classmethod
    def text(cls, content, from_username, to_username, create_time=None):
        context = {
            "Content": content,
            "FromUserName": from_username,
            "ToUserName": to_username,
            "CreateTime": create_time or timestamp(),
        }
        return Template(TEXT_TPL).render(**context)

    @classmethod
    def image(cls, media_id, from_username, to_username, create_time=None):
        context = {
            "MediaId": media_id,
            "FromUserName": from_username,
            "ToUserName": to_username,
            "CreateTime": create_time or timestamp(),
        }
        return Template(IMAGE_TPL).render(**context)


def timestamp():
    """return current timestamp in seconds

    :rtype: int

    """
    return int(time.time())
