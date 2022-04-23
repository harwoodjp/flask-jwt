import sqlite3
import json

def select_users():
  query = "SELECT id, first_name, last_name, email FROM user;"
  con = sqlite3.connect('database.db')
  cur = con.cursor()
  results = []
  for row in cur.execute(query):
    result = dict()
    result["id"] = row[0]
    result["first_name"] = row[1]
    result["last_name"] = row[2]
    result["email"] = row[3]
    results.append(result)
  con.close()
  return results

def select_user_email_password(email, password):
  query = "SELECT id, first_name, last_name FROM user WHERE email='{}' AND password = '{}';".format(email, password)
  con = sqlite3.connect('database.db')
  cur = con.cursor()
  results = []
  for row in cur.execute(query):
    result = dict()
    result["id"] = row[0]
    result["first_name"] = row[1]
    result["last_name"] = row[2]
    results.append(result)
  con.close()
  return results

def select_books_user(user):
  query = "SELECT title FROM book WHERE user = {}".format(user)
  con = sqlite3.connect('database.db')
  cur = con.cursor()
  results = []
  for row in cur.execute(query):
    result = dict()
    result["title"] = row[0]
    results.append(result)
  con.close()
  return results


