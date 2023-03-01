# libaries and modules import
from api_connect import connect_to_mongoDB
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

# connect to MongoDB
    # try:
        # connect to MongoDB
client = MongoClient('mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority')
db = client['Netflix']
# create collection / to change collection name
Netflix_project = db['Netflix_project']
# except pymongo.errors.PyMongoError as e:
# print("MongoDB connection failed:", e)
        
# index page       
@app.route('/')
def home():
    return render_template('index.html')



# get all data from MongoDB
@app.route('/alldata', methods=['GET'])
def get_data():
    # retrieve all documents from collection
    data = []
    for doc in Netflix_project.find({}, {'_id': 0}):
        data.append(doc)
    # return documents as JSON
    return jsonify(data)

# display all data in table
@app.route('/table')
def display_table():
    # Retrieve data from your MongoDB collection
    data = list(Netflix_project.find())    
    # Render the HTML template and pass in the data as a variable
    return render_template('table.html', data=data)


@app.route('/aggregate')
def aggregate():
    # Run the aggregation query
    result = Netflix_project.aggregate([
        { "$match": { "type": {"$ne": None } } },
    {
        "$group":{"_id":"$type","nb":{"$sum":1}}
    }
    ])
    # Convert the result to a list so it can be passed to the template
    data = list(result)
    # Render the template with the data
    return render_template('aggregate.html', data=data)










# @app.route('/data', methods=['GET'])
# def get_data():
#     data = []
#     query = Netflix_project.aggregate([ {"$group":{"_id":"$type","nb":{"$sum":1}}}, {"$sort":{"nb":-1}}, {"$limit":1}])
#     print(query)
#     data.append(query)
#     return jsonify(data)   



        




# read data from MongoDB
# @app.route('/api/netflix_data')
# def get_netflix_data():
#     # retrieve data from MongoDB
#     json_response = []
#     for document in connect_to_mongoDB().findall():
#         json_response.append(document)
#     return jsonify(json_response)





# export albums to MongoDB
# @app.route('/export-albums', methods=['POST'])
# def export_albums():
#     artist_name = request.form.get('artist_name')
#     results = sp.search(q='artist:"{}"'.format(artist_name), type='album')
#     for item in results['albums']['items']:
#         mongo_collection.insert_one(item)
#     return 'Albums exported to MongoDB!'



if __name__ == '__main__':
    app.run()