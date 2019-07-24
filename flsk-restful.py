from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    
    def get(self, name):
        #for item in items:
         #   if item['name'] == name:
          #      return item
        item = next(filter(lambda x: x['name'] == name, items),None) #None sets default value so if next doesn't have value to print it doesn't throws an error
        return {"item" : item} 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items),None):
            return {"message" : "As item with name '{}' already exist.".format(name)}, 400


        #data = request.get_json(force=True) 
        data = request.get_json(silent=True) 
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class Itemlist(Resource):

    def get(self):
        return {"item" : items}


api.add_resource(Item, '/items/<string:name>')                      #http://127.0.0.1:5000/items/kushagra
api.add_resource(Itemlist, '/items')

app.run(port=5000,debug=True)
