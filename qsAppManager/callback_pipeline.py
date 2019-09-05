# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-04 20:05:04


import json

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