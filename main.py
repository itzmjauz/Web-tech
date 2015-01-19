#!/usr/bin/python

import os.path
import sqlite3
import json

#change to liking
filename = "Inventory.db"

#create database if it doens't exist
if(not os.path.isfile(filename)):
    db = sqlite3.connect(filename)
    db.execute("""
        create table inventory 
	(id integer primary key, 
	name char(100) not null, 
	category char(100) not null, 
	location char(100), 
	date char(12), 
	amount integer not null)
    """)

    db.commit()
else:
    db = sqlite3.connect(filename)

#db.execute("INSERT INTO inventory VALUES (1,'Banana','Fruit','Amsterdam','2014-10-05',15)")
#db.execute("INSERT INTO inventory VALUES (2,'Apple','Fruit','Amsterdam','2014-02-05',58)")
#db.commit()

db.row_factory = sqlite3.Row
c = db.cursor()



def fetchAll():
    rows = db.execute("select * from inventory").fetchall()
    db.commit()
    print(json.dumps( [dict(ix) for ix in rows] ))



