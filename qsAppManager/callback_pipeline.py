# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-05-06 20:14:05


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

app = 'Consumer Sales'
apppath = app.replace(" ","%20")#remove spaces from URL path
ISID = 'joshu'
url = 'ws://localhost:4848/app/C%3A%5CUsers%5C{}%5CDocuments%5CQlik%5CSense%5CApps%5C{}.qvf?reloadUri=http://localhost:4848/dev-hub/engine-api-explorer'.format(ISID,apppath)

callback_pipeline(url)