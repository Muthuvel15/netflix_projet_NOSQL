
# not use this code
# install pymongo
# import pymongo
# from pymongo import MongoClient
# import json
# import pandas as pd

# #connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = MongoClient('mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority')
# db = client['Netflix']
# restaurants = db['Netflix_project']

# print('Connected to MongoDB!')
# print("db name:",db.name)



#print(db['Netflix_project'].find_one())


 
 
 
 #old code 
 
 # from flask import Flask
# from flask_mongoengine import MongoEngine
# import os
# from dotenv import load_dotenv
# env_path = Path('Web API Netflix\.env') / '.env'

# load_dotenv(dotenv_path=env_path)
 
 
# app = Flask(__name__)
# db = MongoEngine()
# db. init_app(app)


# USER=muthuvel
# PASSWORD=muthuvel123

# database_name = "Netflix"
# # = "mongodb+srv://:"+os.environ.get('PASSWORD')+"@cluster.cemcbh8.mongodb.net/test"
# DB_URL = "mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority"
# app.config["MONGODB_SETTINGS"] = DB_URL
# print(DB_URL) 

# db = MongoEngine()
# db. init_app(app)
 
# if __name__ == '__main__':
#     app.run()













# from pymongo import MongoClient

# user= "muthuvel"
# mdp= "muthuvel123"


# mongo_uri = 'mongodb+srv://'+user+':'+mdp+'@cluster.cemcbh8.mongodb.net/test'
# mongo_client = pymongo.MongoClient(mongo_uri)
# db = mongo_client ["my_database"]
# collection = db["artists"]

