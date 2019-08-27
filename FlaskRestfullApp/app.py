from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from flask_jwt import JWT, jwt_required
from security import authenticate,identity

app = Flask(__name__)
app.secret_key = "ayaan"
api = Api(app)
items = []

jwt = JWT(app,authenticate,identity)

class Item(Resource):
    @jwt_required()
    def get(self,name):
        # item = list(filter(lambda x: x["name"]==name,items))[0]
        item = next(filter(lambda x: x["name"]==name,items),None)
        return {"item":item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x["name"]==name,items),None):
            return {'message':"An item with name {} is aleardy exists".format(name)}, 400
        
        request_data = request.get_json()
        new_item = {"name":name, "price":request_data["price"]}
        items.append(new_item)
        return new_item ,201

class ItemList(Resource):
    def get(self):
        return {"items":items}

    def post(self):
        # request_data = request.get_json()
        pass

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5004)