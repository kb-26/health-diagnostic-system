import flask
import os
from pymongo import MongoClient

client = MongoClient()

db = client.mydb
collection = db.health_management_system


app = flask.Flask(__name__)



@app.route('/home',methods = ['POST', 'GET'])
def home():
    result = {'count' : collection.count(), 'all_sym':collection.find()}
    if flask.request.method == 'POST':
        symptopms = flask.request.form['sym']
        symlist = [int(s) for s in symptopms.split(',')]
        symstring = ",".join(str(x) for x in symlist)
        mainlist = [0] * 132
        for i in range(132):
            if i in symlist:
                mainlist[i] = 1
            else:
                mainlist[i] = 0
        print(mainlist)
        mainstring = ",".join(str(x) for x in mainlist)
        fh = open("list.txt","w")
        fh.write(mainstring)
        fh.close()
        return symstring
    return flask.render_template("home.html",result = result)

#@app.route("/about")
#def about():
#    return flask.render_template("about.html")



if __name__ == "__main__":
    app.run(host = '172.17.4.214')
