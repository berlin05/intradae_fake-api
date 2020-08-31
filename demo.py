from nsetools import Nse
from flask import jsonify
from flask import request
import random

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
nse=Nse()
stocks=[]
stocks.append(["mrf","MRF"])
stocks.append(["lupin","Lupin"])
stocks.append(["3iinfotech","3i-Infotech"])
stocks.append(["rcom","Reliance Communications"])
stocks.append(["ultracemco","Ultratech Cement"])

@app.route('/stocks', methods=['GET'])
def home():
    
    return jsonify({'stocks':stocks})

@app.route('/price',methods=['GET'])
def price():
    data=[]
    for i in range(len(stocks)):
        ticker = stocks[i][0]
        
        ticket_price=random.randint(20,100)
        quote=nse.get_quote(ticker)
        lastPrice=quote['lastPrice']
        change=quote['change']
        name=quote['companyName']
        resp={'new_price':lastPrice,'change':change,'name':name,'ticket_price':ticket_price}
        data.append(resp)
    return jsonify({'data':data})
app.run()



