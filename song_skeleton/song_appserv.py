# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:29:39 2020

@author: Chema
"""

import logging
import sys
import uuid
import json
from flask.json import JSONEncoder  


class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__   
        
class Song:
      def __init__(self):
        self.id = str(uuid.uuid4())
        self.author = ""
        self.title = ""
        self.song = ""
      def __str__(self):
        return str(self.__dict__)    
      

class AppServ:
    def __init__(self):
        self.logger = logging.getLogger('AppServ')
        self.songs = self.create_songs()
            
    def create_songs(self):
        songs = {}
        for i in range(10):
            song = Song()
            song.author = "Author " + str(i)
            song.title = "Title " + str(i)
            song.song = "Song " + str(i)
            songs[song.id] = song
        return songs
        
    def list_songs(self):
        try:
            return self.songs
        except:
            self.logger.error("Exception when getting songs: ",sys.exc_info()[0],"occured.")
        return {}
    
    def get_song(self, song_id):
        try:
            if song_id in self.songs:
                return self.songs[song_id]
            else:
                return None
        except:
            self.logger.error("Exception when getting songs: ",sys.exc_info()[0],"occured.")
        return {}
    
def save_list_as_json(filename, mylist, encoder):
    with open(filename, 'w', encoding="utf-8") as fp:
        dump_data = json.dumps(encoder.encode(mylist), indent=2)
        fp.write(dump_data)
    fp.close()  
    
if __name__=="__main__":
    app_serv = AppServ()
    songs = app_serv.list_songs()
    save_list_as_json("songs.json",list(songs.values()),MyEncoder())