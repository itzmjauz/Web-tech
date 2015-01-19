#!/usr/bin/python

import os.path
import sqlite3

#change to liking
filename = "Inventory.db"

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


        
