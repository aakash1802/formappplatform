import lib.base
from lib.base import BaseHandler
# from lib.config import CAMFILEUPLOADPATH, THUMBNAILPATH, PROJECT_PATH
from os import walk
import os, json, uuid
import xml.etree.ElementTree as ET
from tornado.web import asynchronous


# from lib.db

class LoginBaseHandler(BaseHandler):

    # def get(self):
    #     self.write("thumbnail, world")

    def prepare(self):
        pass


class LoginHandler(LoginBaseHandler):
    def extract(self, fileuid, filedir, fname):
        comand = "ffmpeg  -ss 00:00:00 -i " + filedir + '/' + fname[
            0] + " -frames:v 1 " + filedir + '/' + "THUMBFRAME01.jpeg"

        os.system(comand)
        print
        comand


    def post(self):
        response = {"status": "OK", "userID": "UID","token":"token"}
        self.write(json.dumps(response))
        return

    # def get(self):
    #     fileuid = self.get_query_argument("fileuid")
    #     print
    #     fileuid
    #     filedir = CAMFILEUPLOADPATH + '/' + fileuid
    #     fname = []
    #     print
    #     fname
    #     for (dirpath, dirnames, filenames) in walk(filedir):
    #         fname.extend(filenames)
    #         break
    #     print
    #     fname
