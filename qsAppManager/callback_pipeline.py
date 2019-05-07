# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-05-06 20:17:48


import json
from __init__ import *


class callback_pipeline:
    """class which uses a collection of API calls to perform tasks

TODO:
    update master item
    delete master item
    create master item
    create variable
    delete variable
    export master items
    export variables

Args:

Attributes:

"""

    def __init__(self, url):
        self.ws = qsEngineCommunication(url)


callback_pipeline(url)
