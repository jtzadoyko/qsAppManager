# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-04-09 21:27:16
import json


class qsEngineAppApi:
    """

    TODO:
        create applyPatches function inorder to update master items

    Args:

    Attributes:

    """

    def __init__(self, socket):
        self.engine_socket = socket

    def get_measures(self, doc_handle):

        msg = json.dumps(
            {"name": "MEASURELIST", "method": "CreateSessionObject", "handle": doc_handle, "params": [{
                "qInfo": {
                    "qType": "MeasureList"
                },
                "qMeasureListDef": {
                    "qType": "measure",
                    "qData": {
                        "title": "/title",
                        "tags": "/tags",
                        "qMeasure": "/qMeasure"}}}]})

        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def get_object(self, doc_handle, param_list=[]):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle,
                          "method": "GetObject", "params": param_list})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def create_master_dim(self, doc_handle, dim_id, dim_title, dim_grouping="N", dim_field='', dim_label='',
                          meta_def=""):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "CreateDimension", "params": [{
            "qInfo": {
                "qId": dim_id,
                "qType": "Dimension"
            },
            "qDim": {
                "title": dim_title,
                "qGrouping": dim_grouping,
                "qFieldDefs": [
                    dim_field
                ],
                "qFieldLabels": [
                    dim_label
                ]
            },
            "qMetaDef": {
                "title": meta_def
            }
        }]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def destroy_dim(self, doc_handle, dim_id):
        msg = json.dumps(
            {"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "DestroyDimension", "params": [{dim_id}]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def create_master_measure(self, doc_handle, measure_id, measure_title, measure_expr, meta_def=""):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "CreateMeasure", "params": [{
            "qInfo": {
                "qId": measure_id,
                "qType": "Measure"
            },
            "qMeasure": {
                "qLabel": measure_title,
                "qDef": measure_expr
            },
            "qMetaDef": {
                "title": measure_title
            }
        }]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def destroy_measure(self, doc_handle, measure_id):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "DestroyDimension",
                          "params": [{measure_id}]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def create_variable(self, doc_handle, var_id="", var_name="", var_comment="", var_def=""):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "CreateVariable", "params": [{
            "qInfo": {
                "qId": var_id,
                "qType": "Variable"
            },
            "qName": var_name,
            "qComment": var_comment,
            "qDefinition": var_def
        }]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']

    def destroy_variable_by_id(self, doc_handle, var_name):
        msg = json.dumps({"jsonrpc": "2.0", "id": 0, "handle": doc_handle, "method": "DestroyVariableById",
                          "params": [{var_name}]})
        response = json.loads(
            self.engine_socket.send_call(self.engine_socket, msg))
        try:
            return response['result']
        except KeyError:
            return response['error']
