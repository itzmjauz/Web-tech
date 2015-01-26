#!/usr/bin/env python

import sqlite3

db = sqlite3.connect('Inventory.db') # Warning: This file is created in the current directory

db.execute("""
CREATE TABLE inventory 
	(id INTEGER PRIMARY KEY, 
	name char(100) NOT NULL, 
	category char(100) NOT NULL, 
	location char(100), 
	date char(12), 
	amount INTEGER NOT NULL)
""")

db.commit()
