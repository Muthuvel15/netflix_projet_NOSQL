
import requests
import pymongo
from pymongo import MongoClient

# URL API IMBD / Netflix54
url_IMBD = 'https://imdb-top-100-movies.p.rapidapi.com/'
url_Netflix_serie = " https://netflix-data.p.rapidapi.com/season/episodes/" 
#https://netflix54.p.rapidapi.com/search/  / https://netflix-data.p.rapidapi.com/season/episodes/

# Cle sceret IMBD API / Netflix54 API
headers = {
 'X-RapidAPI-Key': '50f68ad345mshe24ba433ec1f7a7p10abb7jsn59094bde033f', 
 'X-RapidAPI-Host': 'imdb-top-100-movies.p.rapidapi.com',
 "X-RapidAPI-Key": "50f68ad345mshe24ba433ec1f7a7p10abb7jsn59094bde033f",
 "X-RapidAPI-Host": "netflix-data.p.rapidapi.com"
}

params = {
     "lang": "en",
     "offset":"0",
     "limit":"60",
    #  "query":"Breaking Bad ,Stranger Things ,Narcos ,Better Call Saul ,Peaky Blinders ,The Crown ,Ozark ,Black Mirror ,Mindhunter ,The Haunting of Hill House ,Money Heist ,Dark ,The Witcher ,Daredevil ,The Punisher ,The Umbrella Academy ,Narcos: Mexico ,The Queen's Gambit ,Bridgerton ,The Sinner ,Bodyguard ,Fargo ,Cobra Kai ,Lucifer ,The Boys ,The Mandalorian ,Westworld ,The Handmaid's Tale ,Kingdom ,Altered Carbon ,Vikings ,The Last Kingdom ,The Expanse ,The Good Place ,La Casa de Papel (Money Heist) ,Sense8 ,The Killing ,Sex Education ,Hannibal ,Orange is the New Black ,Homeland ,Bates Motel ,Broadchurch ,The Fall ,Lost in Space ,Oz ,Shadow and Bone ,The Stranger ,The Blacklist ,The Alienist","offset":"50","limit_titles":"50",
}

# check if API connection is successful
try:
    response = requests.get(url_Netflix_serie, headers=headers, params=params)
    response.raise_for_status()
    print("Netflix54 API connection successful!")
except requests.exceptions.RequestException as e:
    print("Netflix54 API connection failed:", e)

def connect_to_mongoDB():
    try:
        # connect to MongoDB
        client = MongoClient('mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority')
        db = client['Netflix']
        # create collection / to change collection name
        collection_name = db['Netflix_project']
        return collection_name
    except pymongo.errors.PyMongoError as e:
        print("MongoDB connection failed:", e)

try:
    # Make API request
    response = requests.get(url_Netflix_serie, headers=headers, params=params)
    response.raise_for_status()
    print("Netflix54 API connection successful!")
    # Parse response as JSON
    data = response.json()
    print(data)
    # Insert data into MongoDB collection / example: test is a collection name
    connect_to_mongoDB().serie.insert_many(data)
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



