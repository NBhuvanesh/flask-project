from flask import Flask,request
import joblib
import pickle
api = Flask(__name__)

@api.route('/classify')
def my_profile():
    # return(request.args['message'])
    message = request.args['message']
    model = joblib.load('mod.pkl')
    result = model.predict_one(message)
    # response_body = {
    #     "name": "Nagato",
    #     "about" :"Hello! I'm a full stack developer that loves python and javascript"
    # }
    return result
