# -*- coding: utf-8 -*-

""" Wechat class to handle everything

"""

import urlparse
import hashlib

from .parser import XMLMsgParser
from .render import MsgRender


class Wechat(object):
    """ Handle everything about wechat

    usage:
    w = Wechat(token, appid, secret, body)

    get xml node value, such as MsgType: w.xml.MsgType

    """

    def __init__(self,
                 token=None,
                 appid=None,
                 secret=None,
                 url=None,
                 body=None):
        """
        :param string token: user defined token at wechat platform
        :param string appid: appid from wechat platform
        :param string secret: secret from wechat platform
        :param string url: request url(full path) from tencent server,
                           used to get ["timestamp", "nonce", "signature"]
        :param string body: request body from tencent server

        """
        self.xml = XMLMsgParser(msg=body)
        self._token = token
        self._appid = appid
        self._secret = secret
        self._url = url

    def reply_text(self,
                   content,
                   from_username=None,
                   to_username=None,
                   create_time=None):
        """ generate a text reply xml string
        wiki: http://mp.weixin.qq.com/wiki/14/89b871b5466b19b3efa4ada8e577d45e.html

        :param string content: content to send
        :param string from_username: from_username
        :param string to_username: to_username
        :param string create_time: message create time
        :rtype: string

        """
        params = {
            "content": content,
            "from_username": from_username or self.xml.ToUserName,
            "to_username": to_username or self.xml.FromUserName,
            "create_time": create_time,
        }
        return MsgRender.text(**params)

    def reply_image(self,
                    media_id,
                    from_username=None,
                    to_username=None,
                    create_time=None):
        """ generate a text reply xml string
        wiki: http://mp.weixin.qq.com/wiki/14/89b871b5466b19b3efa4ada8e577d45e.html

        :param string media_id: image id to send
        :param string from_username: from_username
        :param string to_username: to_username
        :param string create_time: message create time
        :rtype: string

        """
        params = {
            "to_username": to_username or self.xml.FromUserName,
            "from_username": from_username or self.xml.ToUserName,
            "create_time": create_time,
            "media_id": media_id,
        }
        return MsgRender.image(**params)

    @property
    def auth_success(self):
        """ return True if the uri is from tencent server
        wiki: http://mp.weixin.qq.com/wiki/4/2ccadaef44fe1e4b0322355c2312bfa8.html

        :rtype: bool

        """
        modified_key = self._modify_key("auth_success")
        if modified_key in self.__dict__:
            return self.__dict__[modified_key]

        parser = urlparse.parse_qs(urlparse.urlparse(self._url).query)
        timestamp = parser.get("timestamp", None)
        nonce = parser.get("nonce", None)
        signature = parser.get("signature", None)
        if timestamp is None or nonce is None or signature is None:
            self.__dict__[modified_key] = False
            return False

        hash_string = ''.join(sorted([self._token, timestamp, nonce]))
        success = signature == hashlib.sha1(hash_string).hexdigest()
        self.__dict__[modified_key] = success
        return success

    @staticmethod
    def _modify_key(key):
        """cache key, value in self.__dict__, generate a modified key

        :rtype: string

        """
        return "_modified_%s_" % key
