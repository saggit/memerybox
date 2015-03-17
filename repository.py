import os
import time
from os import path


class Repository(object):

    def __init__(self, path):
        self.path = path

    def list_album(self):
        return  [(f, time.ctime(os.path.getctime(os.path.join(self.path, f)))) for f in os.listdir(self.path)]
        
    def list_photos(self, path):
        full_path = os.path.join(self.path, path)
        return [os.path.join(full_path, f) for f in os.listdir(full_path)]