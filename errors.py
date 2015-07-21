# -*- coding: utf-8 -*-

""" Defined errors of current package

"""


class AuthError(Exception):
    """Auth request from tencent server failed

    """

    def __str__(self):
        return repr(u"Auth request from tencent server failed")
