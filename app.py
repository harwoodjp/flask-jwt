from flask import Flask, request, jsonify, make_response, render_template
from .database import select_users, select_user_email_password, select_books_user
import json
import jwt


app = Flask(__name__, template_folder='./')

@app.route("/")
def index():
  return render_template('index.html')


@app.get("/users")
def list_users():
  return json.dumps(select_users())

@app.post("/books")
def list_books_user():
  req = request.get_json()
  token = req["token"]
  user = get_token_user(token)
  if user:
    result = select_books_user(user["id"])
    return json.dumps(result)
  error = dict()
  error["message"] = "invalid token!"    
  return json.dumps(error)


@app.post("/login")
def login_user():
  req = request.get_json()
  email = req["email"]
  password = req["password"]
  result = select_user_email_password(email, password)
  if len(result) > 0:
    user = result[0]
    user["token"] = get_token(user)
    return json.dumps(user)
  error = dict()
  error["message"] = "invalid credentials!"
  return json.dumps(error)


def get_token(user):
  secret = "123"
  token = jwt.encode({"data": user}, secret, algorithm="HS256")
  return token

def get_token_user(token):
  secret = "123"
  try:
    result = jwt.decode(token, secret, algorithms=["HS256"])
    print("get_token_user result: ")
    if result["data"]["id"]:
      print(result["data"])
      return result["data"]
  except:
    return None
  return None