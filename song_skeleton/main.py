# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:24:54 2020

@author: Chema
"""

import os
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask import send_from_directory   
from flask.json import JSONEncoder  

from song_appserv import *




class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__   
        
        
app_serv = AppServ()

app = Flask(__name__,
            static_url_path='', 
            static_folder='web',
            template_folder='web')


api = Api(app)
parser = reqparse.RequestParser()
app.json_encoder = MyEncoder

          
            
          

class SongEntityList(Resource):
    def get(self):
        return jsonify(app_serv.list_songs())
    
    
class SongEntityResource(Resource):
    def get(self, song_id):     
        return jsonify(app_serv.get_song(song_id))
       
   
api.add_resource(SongEntityList, '/api/songs')
api.add_resource(SongEntityResource, '/api/songs/<song_id>')


"""
Index.html
"""
@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/favicon.ico') 
def favicon(): 
    return app.send_static_file('./img/favicon.ico')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)