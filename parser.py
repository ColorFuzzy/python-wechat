# -*- coding: utf-8 -*-

""" User request analyse and server response string generate.

"""

from xml import etree


class XMLMsgParser(object):
    """Make it easy to get key, value in request xml string

    usage: request = MessageParser(request_body)
    MsgType = request.MsgType

    """

    def __init__(self, msg=None):
        self._msg = msg

    def __contains__(self, xml_key):
        """Overloading the `in' operator, Return True if the xml has the given key

        :param string xml_key: xml node name
        :rtype: bool

        """
        try:
            getattr(self, xml_key)
        except KeyError:
            return False
        else:
            return True

    def __getattr__(self, xml_key):
        """Make it easy to get xml_key from self._msg
        usage: self.MsgType

        :param string xml_key: key in the request body

        """
        modified_key = self._modify_key(xml_key)
        if modified_key in self.__dict__:
            return self.__dict__[modified_key]

        node = self._parsed_msg.find(xml_key)
        if node is None:
            raise KeyError(u"key %s doesn't exist in self._msg" % xml_key)

        text = node.text
        self.__dict__[modified_key] = text
        return text

    @property
    def _parsed_msg(self):
        """parse self._body xml string and set it to self.__dict__

        """
        modified_key = self._modify_key("_parsed_msg")
        if modified_key in self.__dict__:
            return self.__dict__[modified_key]

        if self._msg is None:
            raise ValueError(u"self._msg should not be None")
        self.__dict__[modified_key] = etree.fromstring(self._msg)
        return self.__dict__[modified_key]

    @staticmethod
    def _modify_key(key):
        """cache key, value in self.__dict__, generate a modified key

        :rtype: string

        """
        return "_modified_%s_" % key
