
import requests
import pymongo
from pymongo import MongoClient

# URL API IMBD / Netflix54
url_IMBD = 'https://imdb-top-100-movies.p.rapidapi.com/'
url_Netflix_serie = "https://netflix-data.p.rapidapi.com/season/episodes/"

# Cle sceret IMBD API / Netflix54 API
headers = {
 'X-RapidAPI-Key': '50f68ad345mshe24ba433ec1f7a7p10abb7jsn59094bde033f', 
 'X-RapidAPI-Host': 'imdb-top-100-movies.p.rapidapi.com',
 "X-RapidAPI-Key": "50f68ad345mshe24ba433ec1f7a7p10abb7jsn59094bde033f",
 "X-RapidAPI-Host": "netflix-data.p.rapidapi.com"
}

params = {
     "lang": "en",
     "ids":"80077209,80117715",
     "offset":"0",
     "limit":"25"
}

# check if API connection is successful
try:
    response = requests.get(url_Netflix_serie, headers=headers, params=params)
    response.raise_for_status()
    print("Netflix54 API connection successful!")
except requests.exceptions.RequestException as e:
    print("Netflix54 API connection failed:", e)

def connect_to_mongoDB():
    # connect to MongoDB
    client = MongoClient('mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority')
    db = client['Netflix']
    # create collection / to change collection name
    collection_name = db['Netflix_project']
    return collection_name

try:
    # Make API request
    response = requests.get(url_Netflix_serie, headers=headers, params=params)
    response.raise_for_status()
    print("Netflix54 API connection successful!")
    # Parse response as JSON
    data = response.json()
    # Insert data into MongoDB collection / example: test is a collection name
    connect_to_mongoDB().test.insert_many(data)
    print("Data inserted into MongoDB")
except (requests.exceptions.RequestException, pymongo.errors.PyMongoError) as e:
    print("Netflix54 API connection or MongoDB insertion failed:", e)


















# import requests

# url = "https://netflix54.p.rapidapi.com/title/details/"
# headers = {
#     "X-RapidAPI-Key": "50f68ad345mshe24ba433ec1f7a7p10abb7jsn59094bde033f",
#     "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
# }
# params = {
#     "ids": "80057281",
#     "lang": "en"
# }

# response = requests.get(url, headers=headers, params=params)

# data = response.json()

# print(data)



