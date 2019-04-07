# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzadoyko
# @Last Modified time: 2019-03-26 19:20:04


from websocket import create_connection


class qsEngineCommunication:

    def __init__(self, url):
        self.url = url
        self.ws = create_connection(self.url)
        self.session = self.ws.recv()

    @staticmethod
    def send_call(self, call_msg):
        self.ws.send(call_msg)
        return self.ws.recv()

    @staticmethod
    def close_qvengine_connection(self):
        self.ws.close()
