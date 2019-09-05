# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-04 20:20:31

class qsEngineCommunication:
    """

    TODO:

    Args:

    Attributes:

    """

    def __init__(self, url):
        self.url = url
        self.ws = create_connection(self.url)
        self.session = self.ws.recv()

    @staticmethod
    def send_call(self, call_msg):
        self.ws.send(call_msg)
        return self.ws.recv()

    @staticmethod
    def close_engine_connection(self):
        self.ws.close()
