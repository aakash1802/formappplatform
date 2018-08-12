#!/usr/bin/env python
# -*- coding: ascii -*-

__author__ = ""
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

# python imports
import datetime
import sys
# from tornado.options import define, options
from importlib import reload
# reload(sys)
# sys.set
# sys.setdefaultencoding('utf-8')

# tornado imports
import tornado

class BaseHandler(tornado.web.RequestHandler):
    """
    User defined base class for all requests.
    """

    def __init__(self, application, request, **kwargs):

        """
        Constructor function used to call super constructor.
        dt_handler is used to convert datetime or date object into isoformat.
        """

        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.dt_handler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date) else None
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'accept, cache-control, origin, x-requested-with, x-file-name, content-type')
	    # self.set_header("Access-Control-Allow-Origin", "*")