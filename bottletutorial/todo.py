import sqlite3
import json as real_json
from bottle import route, run, debug, template, request, static_file, error

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

@route('/new', method='GET')
def new_item():

  if request.GET.get('save', '').strip():
    name = request.GET.get('name').strip()
    category = request.GET.get('category').strip()
    location = request.GET.get('location').strip()
    date = request.GET.get('date').strip()
    amount = request.GET.get('amount').strip()
    conn = sqlite3.connect('Inventory.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO inventory (name, category, location, date, amount) VALUES (?,?,?,?,?)", (name, category, location, date, amount))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return {'Addition' : 'succes',            'ID' : new_id}

@route('/edit/:no', method='GET')
def edit_item(no):

  if request.GET.get('save', '').strip():
    name = request.GET.get('name').strip()
    category = request.GET.get('category').strip()
    location = request.GET.get('location').strip()
    date = request.GET.get('date').strip()
    amount = request.GET.get('amount').strip()

    conn = sqlite3.connect('Inventory.db')
    c = conn.cursor()
    c.execute(
        "UPDATE inventory SET name = ?, category = ?, location = ?, date =?, amount = ? WHERE id LIKE ?", (name, category, location, date, amount, no))
    conn.commit()

    return {'Update' : 'succes'} 

  #else:
  #  conn = sqlite3.connect('Inventory.db')
  #  c = conn.cursor()
  #  c.execute(
  #      "SELECT name, category, location, date, amount FROM inventory WHERE id LIKE ?", (str(no)))
  #  cur_data = c.fetchone()

  #  return template('edit_task', old=cur_data, no=no)

@route('/help')
def help():

  static_file('help.html', root='.')

@route('/json:json#[0-9]+#')
def show_json(json):

  conn = sqlite3.connect('Inventory.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute(
      "SELECT * FROM inventory WHERE id LIKE ?", (json))
  rows = c.fetchall()
  c.close()

  if not rows:
    return {'item': 'This item number does not exist!'}
  else:
    return {'item' :[dict(ix) for ix in rows]}

@route('/json')
def show_json2():

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
run(reloader=True)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment
