import os
import sqlite3
import json as real_json
from bottle import route, run, debug, template, request, static_file, error, hook, response

# only needed when you run Bottle on mod_wsgi
from bottle import default_app


# This hook the headers below to all responses.
# You may extend this hook to add additional headers
# (hint: check if your server returns the appropriate MIME related information)
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

# Cross domain POST, PUT and DELETE requests will invoke a preflight OPTIONS request.
# If this request if not properly handled, the actual request will be cancelled.
# This route catches all OPTIONS requests.

@route('/:#.*#',method='OPTIONS')
def options():
    return


@route('/new', method='POST')
def new_item():
  response.status=201

  
  name = request.POST.get('name').strip()
  category = request.POST.get('category').strip()
  location = request.POST.get('location').strip()
  date = request.POST.get('date').strip()
  amount = request.POST.get('amount').strip()
  conn = sqlite3.connect('Inventory.db')
  c = conn.cursor()

  c.execute(
      "INSERT INTO inventory (name, category, location, date, amount) VALUES (?,?,?,?,?)", (name, category, location, date, amount))
  new_id = c.lastrowid

  conn.commit()
  c.close()

  return {'Addition' : 'succes',            'ID' : new_id}

@route('/edit/:no', method='POST')
def edit_item(no):

  name = request.POST.get('name').strip()
  category = request.POST.get('category').strip()
  location = request.POST.get('location').strip()
  date = request.POST.get('date').strip()
  amount = request.POST.get('amount').strip()

  conn = sqlite3.connect('Inventory.db')
  c = conn.cursor()
  c.execute("SELECT * FROM inventory WHERE id LIKE?", (str(no)))
  rows = c.fetchall()
  if rows:
      return {'Update' : 'Index unavailable'}
  else:
    c.execute(
          "UPDATE inventory SET name = ?, category = ?, location = ?, date =?, amount = ? WHERE id LIKE ?", (name, category, location, date, amount, no))
    conn.commit()

  return {'Update' : 'success'}

@route('/deleterow/:no', method='POST')
def delete_item(no):

  conn = sqlite3.connect('Inventory.db')
  c = conn.cursor()
  c.execute(
      "DELETE FROM inventory WHERE id LIKE ?", (no))
  conn.commit()

  return {'Update' : 'success'}

  #else:
  #  conn = sqlite3.connect('Inventory.db')
  #  c = conn.cursor()
  #  c.execute(
  #      "SELECT name, category, location, date, amount FROM inventory WHERE id LIKE ?", (str(no)))
  #  cur_data = c.fetchone()

  #  return template('edit_task', old=cur_data, no=no)

@route('/help')
def help():

  return static_file('assignment3.html', root='.')

@route('/items/:json#[0-9]+#')
def show_json(json):

  conn = sqlite3.connect('Inventory.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute(
      "SELECT * FROM inventory WHERE id LIKE ?", (json))
  rows = c.fetchall()
  c.close()

  if not rows:
    response.status = 204
    return {'item': 'This item number does not exist!'}
  else:
    return {'item' :[dict(ix) for ix in rows]}

@route('/items')
def show_json2():

  conn = sqlite3.connect('Inventory.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute("SELECT * FROM inventory")
  rows = c.fetchall()
  c.close()

  if not rows:
    response.status = 204
    return {'Inventory': 'This Inventory is empty!'}
  else:
    return {'Inventory' : [dict(ix) for ix in rows] }



@route('/reset', method='POST')
def reset():

  db = sqlite3.connect('Inventory.db') # Warning: This file is created in the current directory

  db.execute("""
  DROP TABLE inventory
  """)

  # create table
  db.execute("""
  CREATE TABLE inventory
    (id INTEGER PRIMARY KEY,
	name char(100) NOT NULL,
	category char(100) NOT NULL,
	location char(100),
	date char(12),
	amount INTEGER NOT NULL)
  """)

  # create example row
  db.execute("""
  INSERT INTO inventory
	(name, category, location, date, amount)
	VALUES (?, ?, ?, ?, ?)
    """, ("Banana", "Fruit", "Amsterdam", "2014-10-05", "15"));

  # commit changes to database:
  db.commit()

  conn = sqlite3.connect('Inventory.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute("SELECT * FROM inventory")
  rows = c.fetchall()
  c.close()

  if not rows:
    return {'Inventory': 'This Inventory is empty!'}
  else:
    return {'Inventory' : [dict(ix) for ix in rows] }

@error(403)
def mistake403(code):
  return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
  return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True, port=8080)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment
