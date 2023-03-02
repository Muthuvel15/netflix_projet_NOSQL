# libaries and modules import
from api_connect import connect_to_mongoDB
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_bootstrap import Bootstrap
import plotly.express as px
import plotly.graph_objs as go


app = Flask(__name__)
bootstrap = Bootstrap(app)

# connect to MongoDB
# try:
# connect to MongoDB
client = MongoClient(
    'mongodb+srv://muthuvel:muthuvel123@cluster.cemcbh8.mongodb.net/?retryWrites=true&w=majority')
db = client['Netflix']
# create collection / to change collection name
Netflix_project = db['Netflix_project']
topFilms= db['topFilms']
# except pymongo.errors.PyMongoError as e:
# print("MongoDB connection failed:", e)

# index page


@app.route('/')
def home():
    return render_template('landing.html')


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


@app.route('/table', methods=['GET'])
def display_table():
    # Retrieve data from your MongoDB collection
    data = list(Netflix_project.find())
    # Render the HTML template and pass in the data as a variable
    return render_template('table.html', data=data)


@app.route('/data1', methods=['GET'])
def data1():
    # Run the aggregation query
    result = Netflix_project.aggregate([
        {"$match": {"type": {"$ne": None}}},
        {
            "$group": {"_id": "$type", "nb": {"$sum": 1}}
        }
    ])
    # Convert the result to a list so it can be passed to the template
    data = list(result)
    # Render the template with the data
     # Extract the labels and values from the data list
    labels = [d['_id'] for d in data]
    values = [d['nb'] for d in data]

    # Create a Plotly Bar chart
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])

    # Convert the graph to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the template with the graph
    return render_template('data1.html', plot_html=plot_html)
    # return render_template('data1.html', data=data)


@app.route('/data2', methods=['GET'])
def data2():
    result = Netflix_project.aggregate([
        {"$match": {"director": {"$ne": "null"}}},
        {"$unwind": "$director"},
        {
            "$group": {
                "_id": "$director",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    data = list(result)
    # Extract the labels and values from the data list
    labels = [d['_id'] for d in data]
    values = [d['count'] for d in data]

    # Create a Plotly Bar chart
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    
    # Update the chart layout with title, x and y axis labels
    fig.update_layout(title='Top 10 Directors with Most Films', 
                      xaxis_title='Director', 
                      yaxis_title='Number of Films')

    # Convert the graph to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the template with the graph
    return render_template('data2.html', plot_html=plot_html)
    # return render_template('data2.html', data=data)

@app.route('/data3', methods=['GET'])
def data3():
    result = Netflix_project.aggregate([
        {
            "$match": {"country": {"$ne": None}}
        },
        {
            "$group": {"_id": "$country", "nb": {"$sum": 1}}

        },
        {
            "$sort": {"nb": -1}
        },
        {"$limit": 10}
    ])
    data = list(result)
    # Extract the labels and values from the data list
    labels = [d['_id'] for d in data]
    values = [d['nb'] for d in data]

    # Create a Plotly Bar chart
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    
    # Update the chart layout with title, x and y axis labels
    fig.update_layout(title='Quels pays produisent le plus de films/séries ?', 
                      xaxis_title='Nom des Pays', 
                      yaxis_title='nombre de films')

    # Convert the graph to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the template with the graph
    return render_template('data3.html', plot_html=plot_html)




@app.route('/data4', methods=['GET'])
def data4():
    result = Netflix_project.aggregate([
        {
            "$group": {"_id": "$release_year", "nb": {"$sum": 1}}

        },
        {"$sort": {"nb": -1}},
    ])
    data = list(result)
    
    # Extract the labels and values from the data list
    labels = [d['_id'] for d in data]
    values = [d['nb'] for d in data]

    # Create a Plotly Bar chart
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    
    # Update the chart layout with title, x and y axis labels
    fig.update_layout(title='Nombre de films/séries par année de production', 
                      xaxis_title='Année de production', 
                      yaxis_title='Nombre de films/séries')

    # Convert the graph to HTML
    plot_html = fig.to_html(full_html=False)

    return render_template('data4.html', plot_html=plot_html)




@app.route('/data5', methods=['GET'])
def data5():
    result = topFilms.aggregate([
        {"$match": {"genre": {"$ne": "null"}}},
        {"$unwind": "$genre"},
        {
            "$group": {
                "_id": "$genre",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        { "$limit": 10 }
    ])
    data = list(result)
    labels = [d['_id'] for d in data]
    values = [d['count'] for d in data]

    # Create a Plotly Pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    # Update the chart layout with title
    fig.update_layout(title='Les genres les plus populaires sur Netflix')

    # Convert the graph to HTML
    plot_html = fig.to_html(full_html=False)

    return render_template('data5.html', plot_html=plot_html)



@app.route('/data6', methods=['GET'])
def data6():
   return render_template('data6.html')

@app.route('/crud', methods=['GET'])
def CRUD():
    return render_template('crud.html')


@app.route('/netflix/<title>',  methods=['GET'])
def get_netflix(title):
    result = list(Netflix_project.find({'title': title}, {'_id': 0}))
    return render_template('netflix.html', result=result, title=title)


if __name__ == '__main__':
    app.run()
