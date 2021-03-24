from datetime import datetime
import time
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
# from stocklab.agent.ebest import EBest
# from stocklab.db_handler.mongodb_handler import MongoDBHandler

# mongodb = MongoDBHandler()
# ebest = EBest("DEMO")
# ebest.login()

# import os
# print("job.py")
# print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

# print(os.getcwd())
# print(os.path.abspath('.'))

class Job(Resource):
    def get(self, id=None):
        if id:
            print("specific user")
            return "specific user"
        else:
            print("list of users")
            return "list of users"