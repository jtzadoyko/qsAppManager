# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzadoyko
# @Last Modified time: 2019-04-06 22:12:06
import json

class qsEngineGlobalApi:
    def __init__(self, socket):
        self.engine_socket = socket

    def get_doc_list(self):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": -
                          1, "method": "GetDocList", "params": []})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']['qDocList']
        except KeyError:
            return response['error']

    def open_doc(self, app_name, user_name='', password='', serial='', no_data=False):
        msg = json.dumps(
            {"jsonrpc": "2.0", "id": 0, "handle": -1, "method": "OpenDoc", "params": [app_name, user_name,
                                                                                      password, serial,
                                                                                      no_data]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response["error"]

    def get_active_doc(self):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": -1,
                          "method": "GetActiveDoc", "params": []})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response["error"]

    @staticmethod
    def get_handle(obj):
        try:
            return obj["qReturn"]["qHandle"]
        except ValueError:
            return "Bad handle value in " + obj
