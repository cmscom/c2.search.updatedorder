# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory


_ = MessageFactory("c2.search.updatedorder")

from c2.search.updatedorder import monkey  # noqa
