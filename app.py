# libaries and modules import
from api_connect import connect_to_mongoDB
from flask import Flask, request, jsonify



app = Flask(__name__)


@app.route('/data')
def get_data():
    # Query all data from collection
    data = connect_to_mongoDB().topFilms.find({})
    # Convert MongoDB cursor to list of dictionaries
    data_list = list(data)
    # Return JSON response
    return jsonify(data_list)


# read data from MongoDB
@app.route('/api/netflix_data')
def get_netflix_data():
    # retrieve data from MongoDB
    json_response = []
    for document in connect_to_mongoDB().findall():
        json_response.append(document)
    return jsonify(json_response)





# export albums to MongoDB
@app.route('/export-albums', methods=['POST'])
def export_albums():
    artist_name = request.form.get('artist_name')
    results = sp.search(q='artist:"{}"'.format(artist_name), type='album')
    for item in results['albums']['items']:
        mongo_collection.insert_one(item)
    return 'Albums exported to MongoDB!'



if __name__ == '__main__':
    app.run()