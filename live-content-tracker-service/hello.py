from flask import Flask, jsonify
from datetime import datetime 
from flask_cors import CORS
import apidata
app = Flask(__name__)
CORS(app)

@app.route("/tweets/<date>",methods=['GET'])
def hello_world(date):
    date=datetime.fromisoformat(date)
    data_list_master = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('mlb'),date),'mlb')
    lasmayores = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('lasmayores'),date),'lasmayores')
    mlbjapan = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('mlbjapan'),date),'mlbjapan')
    mlbdominicana = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('mlbdominicana'),date),'mlbdominicana')
    mlbcuba = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('mlbcuba'),date),'mlbcuba')
    mlbvenezuela = apidata.sort_data_2(apidata.get_twitter_post_data(apidata.get_userID('mlbvenezuela'),date),'mlbvenezuela')
    data_list_master.extend(lasmayores)
    data_list_master.extend(mlbjapan)
    data_list_master.extend(mlbdominicana)
    data_list_master.extend(mlbcuba)
    data_list_master.extend(mlbvenezuela)
    data_list=jsonify(data_list_master)
    data_list.headers.add('Access-Control-Allow-Origin', '*')
    return data_list

    
