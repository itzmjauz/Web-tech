#!/usr/bin/python

import os.path
import sqlite3

#change to liking
filename = "Inventory.db"

db = sqlite3.connect(filename)

if(not os.path.isfile(filename)):
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


        
