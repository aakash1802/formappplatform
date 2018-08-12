#!/usr/bin/env python
# -*- coding: ascii -*-
__author__ = ""
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

import os

# Application Settings
HOST = "http://127.0.0.1"
PORT = 9991
DEBUG = True
COOKIE_SECRET = "!12@#34$"
XSRF_COOKIES = False
LOGIN_URL = "/login"
AUTOSCOPE = None
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, "frontend/templates")
STATIC_PATH = os.path.join(PROJECT_PATH, "../crimson-fe/static")
USERDATAPATH = os.path.join(PROJECT_PATH, "userdata")
CAMFILEUPLOADPATH = os.path.join(PROJECT_PATH, "vendor/fineuploader/php-traditional-server/files")
THUMBNAILPATH = os.path.join(PROJECT_PATH,"thumbnails")

# Database Settings
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DATABASE = "enqform"


# API Settings
PAGE_LIMIT = 10
COOKIE_MAX_AGE = 30  # day
USER_TOKEN_MAX_AGE = 43200 # minutes
NOTIFICATION_MAX_AGE = 10080 # minutes
TOKEN_MAX_AGE = 2  # minutes

#SMTP Settings
#MTP_HOST = "email-smtp.us-west-2.amazonaws.com"
#SMTP_PORT = 587
#SMTP_USER = 'AKIAJUS2G4DPCU7RMWNA'
#SMTP_PASSWORD = 'AvVdAU/M/ZYWx7/WvudGwyn2HA1TO6Rc3jXv/f1pxwwc'
#SMTP_SENDER = "contact@bluecrestsoft.com"
#SMTP_SUPPORT = "pratik.khandge@bluecrestsoft.com"
SMTP_SUPPORT = "simple@findmyjournal.com"
SMTP_SENDER = "abhinav.akash@crimsoni.com"

# Elastic Searhc Settings
# ELASTIC_HOST = "52.74.251.213"
# ELASTIC_PORT = 9200



#social media login settings
settings = dict(
			debug=DEBUG,
			cookie_secret=COOKIE_SECRET,
			xsrf_cookies=XSRF_COOKIES,
			login_url=LOGIN_URL,
			template_path=TEMPLATE_PATH,
			static_path=STATIC_PATH,
			autoescape=AUTOSCOPE
			 #client_id="APP-M4J9POOOOHZ8385O",
			# client_id="APP-M4J9POOOOHZ8385O",
            # client_secret="c569d9d7-dbf4-4df4-acbd-47d953574a23",
            # redirect_uri="https://app.findmyjournal.com/?app=1",
	    	# twitter_consumer_key="U3AMLLWbwqWF5DV2gUmoMniol",
	    	# twitter_consumer_secret="8DtQDkB543FlVNDbNLcOdFEq8U6yUB9K6kyQvnZkgDf8RlOvgZ",
	    	# facebook_api_key="1666504396930667",
	    	# facebook_secret="49cd39fa6c28f217418231bb13c54282",
            # fb_redirect_uri="https://app.findmyjournal.com/?app=2",
	    	# linkedin_client_id="75lnnlkhw4pdqq",
            # linkedin_client_secret="TAnRJV08ddVmxk2f",
            # linkedin_redirect_url="https://app.findmyjournal.com/?app=5",
            # #google_redirect_uri="http://devloper.revaldomain.com/?app=3",
	    	# google_redirect_uri="https://devtest.findmyjournal.com/?app=3",
            # google_oauth={"key": "1028001557304-9mdp5aoauv5mqfe36sq5lvcn6orb3j3t.apps.googleusercontent.com",
            #                           "secret": "YSzeOFFaGd_m6ZPJ4_LmsLOM"}
)