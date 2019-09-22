# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-26 21:14:29
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-22 18:15:57

from __init__ import * 

"""
INITIALIZING CONNECTION TO DESKTOP APPLICATION
"""

app = 'Master Items Manager Testing'
apppath = app.replace(" ","%20")#remove spaces from URL path
ISID = 'joshu'
url = 'ws://localhost:4848/app/C%3A%5CUsers%5C{}%5CDocuments%5CQlik%5CSense%5CApps%5C{}.qvf?reloadUri=http://localhost:4848/dev-hub/engine-api-explorer'.format(ISID,apppath)
        
ws = qsEngineCommunication(url)
QSE = qsEngineGlobalApi(ws)

"""
TESTING GLOBAL OBJECT METHODS
"""
def retrieve_application_list(QSE):
	return [QSE.get_doc_list()[app_index]['qDocName'] for app_index,app_name in enumerate(QSE.get_doc_list())]

retrieve_application_list(QSE)

def retrieve_current_handle(QSE, Doc):
	ACTIVE_DOC = Doc
	return QSE.get_handle(ACTIVE_DOC)

active_application = QSE.open_doc(app)
retrieve_current_handle(QSE, QSE.get_active_doc())

"""
TESTING APPLICATION OBJECT METHODS
"""
APP_OBJECT = qsEngineAppApi(ws)
MEASURES_DOC = APP_OBJECT.get_measures(retrieve_current_handle(QSE, QSE.get_active_doc()))

"""
TESTING GENERIC OBJECT METHODS
"""
GENERIC_OBJECT = qsEngineGenericObjectApi(ws)
LAYOUT = GENERIC_OBJECT.get_layout(retrieve_current_handle(QSE, MEASURES_DOC))

def retrieve_application_measures():
	for index,measure_dict in enumerate(LAYOUT['qLayout']['qMeasureList']['qItems']):
		print(LAYOUT['qLayout']['qMeasureList']['qItems'][index]['qInfo']['qId'])
		print(LAYOUT['qLayout']['qMeasureList']['qItems'][index]['qData']['qMeasure']['qLabelExpression'])
		print(LAYOUT['qLayout']['qMeasureList']['qItems'][index]['qData']['qMeasure']['qLabel'])
		print(LAYOUT['qLayout']['qMeasureList']['qItems'][index]['qData']['qMeasure']['qDef'])
		print(LAYOUT['qLayout']['qMeasureList']['qItems'][index]['qData']['qMeasure']['coloring'])

retrieve_application_measures()


