# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-26 21:14:29
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-04-10 19:23:49

# from qsConfig_connection import qsConfiguration
# from qsApi_connection import qsEngineCommunication
# from qsApi_global import qsEngineGlobalApi
# from qsApi_generic import qsEngineGenericObjectApi
# from qsApi_application import qsEngineAppApi

# measures = qsConfiguration(targetFile='Qlik Application Manager.xlsx', targetSheet='Master Measures')
# print(measures.fields)
# print(measures.valid_mi_stup())
# variables = qsConfiguration(targetFile='Qlik Application Manager.xlsx', targetSheet='Variables')
# print(variables.fields)
# print(variables.valid_var_stup())

"""
INITIALIZING CONNECTION TO DESKTOP APPLICATION
"""
app = 'Consumer Sales'
apppath = app.replace(" ","%20")#remove spaces from URL path
ISID = 'joshu'
url = 'ws://localhost:4848/app/C%3A%5CUsers%5C{}%5CDocuments%5CQlik%5CSense%5CApps%5C{}.qvf?reloadUri=http://localhost:4848/dev-hub/engine-api-explorer'.format(ISID,apppath)
        
ws = qsEngineCommunication(url)
qlik_app = qsEngineGlobalApi(ws)



"""
TESTING GLOBAL OBJECT METHODS
"""
#print(qlik_app.get_doc_list())
x=qlik_app.open_doc(app)
ACTIVE_DOC=qlik_app.get_active_doc()
print('Active Doc: {}'.format(ACTIVE_DOC))
HANDLE = qlik_app.get_handle(ACTIVE_DOC)
print('Current Handle: {}'.format(HANDLE))



"""
TESTING APPLICATION OBJECT METHODS
"""
APP_OBJECT = qsEngineAppApi(ws)
x=APP_OBJECT.get_measures(HANDLE)
HANDLE = qlik_app.get_handle(x)
print('Current Handle: {}'.format(HANDLE))



"""
TESTING GENERIC OBJECT METHODS
"""
s=qsEngineGenericObjectApi(ws)
LAYOUT = s.get_layout(HANDLE)
print(LAYOUT)



