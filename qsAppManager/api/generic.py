# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-04-09 21:27:14
import json


class qsEngineGenericObjectApi:
    """

    TODO:

    Args:

    Attributes:

    """

    def __init__(self, socket):
        self.engine_socket = socket

    def get_layout(self, handle):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0,
                          "handle": handle, "method": "GetLayout", "params": []})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response["result"]
        except KeyError:
            return response["error"]
