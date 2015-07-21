# -*- coding: utf-8 -*-

from .errors import AuthError


class NotProvide(object):
    """
    NotProvide is different from None sometimes None is a valid value
    """
    pass


def require_auth(func):
    """ensure this request is from wechat server
    raise exception at auth failed

    """

    def inner(self, *args, **kwargs):
        if not self.auth_success:
            raise AuthError()
        return func(self, *args, **kwargs)
    return inner
