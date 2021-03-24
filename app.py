from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with

import datetime
import json
from bson import json_util
from bson.objectid import ObjectId

import os

from stockserver.admin.user import User, UserList
from stockserver.admin.user import User
from stockserver.job.job import Job

from stockserver.code.stockcode import Code, CodeList, Price, OrderList


print(os.getcwd())
print(os.path.abspath('.'))

app = Flask(__name__)
CORS(app)
api = Api(app)



#https://flask-restful.readthedocs.io/en/0.3.3/intermediate-usage.html#full-parameter-parsing-example



api.add_resource(CodeList, "/codes", endpoint="codes")
api.add_resource(Code, "/codes/<string:code>", endpoint="code")
api.add_resource(Price, "/codes/<string:code>/price", endpoint="price")
api.add_resource(OrderList, "/orders", endpoint="orders")
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(User,  "/user/<string:id>", endpoint="user")
api.add_resource(Job,  "/job/<int:id>", endpoint="job")

if __name__ == "__main__":
    app.run(debug=True)