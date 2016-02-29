__author__ = 'alakus'

from enum import Enum


class AccountType(Enum):
    CHECKING = '1'
    SAVINGS = '2'
    BUSINESS = '3'

    @classmethod
    def tostring(cls, val):
        for k, v in vars(cls).iteritems():
            if v == val:
                return k

    @classmethod
    def fromstring(cls, str):
        return getattr(cls, str.upper(), None)