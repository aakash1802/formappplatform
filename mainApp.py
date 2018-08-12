#!/usr/bin/env python
# -*- coding: ascii -*-

__author__ = ""
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

# tornado imports
import tornado.web
import tornado.auth
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options, parse_command_line

# application imports
from conf.config import PORT, DEBUG, XSRF_COOKIES, COOKIE_SECRET, AUTOSCOPE, settings

define("port", default=PORT, type=int, help="run app on the given port")

# imports for url routing
# from controllers.thumbnail import ThumbnailHandler, SampleThumbnailHandler, GearThumbnailHandler, SonySampleThumbnailHandler
# from controllers.UserProject import ProjectCreateHandler
# from controllers.vidstich import VidHandler, GearVidHandler, SonyVidHandler, SonyTestVidHandler
from controllers.login import LoginHandler
# from lib.config import PROJECT_PATH


class Application(tornado.web.Application):
    """
        Class contain all urls w.r.t. handler
    """

    def __init__(self):
        """
            Constructor of Application class
        """
        handlers = [
            ("/api/v1/project/create", LoginHandler),
            # ("/api/v1/stitchsample/samsunggear", GearThumbnailHandler),
            # ("/api/v1/stitchsample/sony", SonySampleThumbnailHandler),
            # ("/api/v1/createthumbs", ThumbnailHandler),
            # ("/api/v1/stitchsample", SampleThumbnailHandler),
            # ("/api/v1/stitchfinal/sony", SonyVidHandler),
	        # ("/api/v1/stitchfinal/test/sony", SonyTestVidHandler),
            # ("/api/v1/stitchfinal/samsunggear", GearVidHandler),
            # ("/api/v1/stitchfinal", VidHandler),
            # ("/api/v1/projectstatus", VidHandler),
            # (r"/vendor/(.*)", tornado.web.StaticFileHandler, {"path": PROJECT_PATH}),

            # ("/api/v1/voxtab/sendotp", SendOtpHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)



def main():
    parse_command_line()
    application = tornado.httpserver.HTTPServer(Application())
    # application = tornado.httpserver.HTTPServer(Application(), max_buffer_size=167772160)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()