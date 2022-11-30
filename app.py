
from flask_restful import Resource, Api
from flask import render_template
from os import system
from flask import *
import pymongo 

#Connecting to the  client local/cloud.
#client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient("mongodb+srv://kanojo:kanojo@cluster0.0pien5l.mongodb.net/?retryWrites=true&w=majority")
print(client)

#Creating a collection/datafield
db = client["main"]  #name of DB
collection = db['api'] # name of collection
print(client)

system("clear")

#staring web app
app = Flask(__name__)
api = Api(app)

#Login page
class Home(Resource):
  def get(self):
    return make_response(render_template('register.html')) 
  def post(self):
    return make_response(render_template('register.html')) 

#Login page
class Login(Resource):
  def get(self):
    return make_response(render_template('login.html'))  
  
  def post(self):
    name = request.form.get('name') # for post method
    num = request.form.get('no')
    date = request.form.get('date')
    pwd = request.form.get('pass')
    mail = request.form.get('email')
    choi = request.form.get('choice')
    dict = {"name":name,"email":mail,"pass":pwd}
    collection.insert_one(dict)
    print("-------------------------------")
    print("Data store to db")
    return make_response(render_template('login.html'))
    
# After login Welcome page
class Welcome(Resource):
  def get(self):
    return make_response(render_template('login.html')) 
  
  def post(self):
    pwd = request.form.get('pass')
    mail = request.form.get('email')
    data = collection.find_one({"email":mail,"pass":pwd},{"_id":0})
    print("-------------------------------")
    print(data)
    if data != None and mail == data['email'] and pwd == data['pass']:
      print("--------------------------")
      print(f"Welcome Page for {data['name']} loaded/Login Done")
      return make_response(render_template('welcome.html',name=data['name'],mail=data['email']))
    else:
      print("wrong pass")
      return make_response(render_template('login.html'))  

#Register account page  
class Reg(Resource):  
  def get(self):
    return make_response(render_template('register.html'))  
  def post(self):
    return make_response(render_template('register.html'))
        
api.add_resource(Home, '/',methods=['GET', 'POST'])  
api.add_resource(Login, '/login',methods=['GET', 'POST'])
api.add_resource(Welcome, '/welcome',methods=['GET', 'POST'])
api.add_resource(Reg, '/reg',methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)   
