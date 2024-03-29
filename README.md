Web tech homework
----------------------------------
Made By Peter Atkinson and Antoni Stevenet
==================================
includes Screen.css as standard css, and print.css for printing
edit the index.html for custom testing of the print.css

main.py API Documentation
===================================
In the Documentation we asume the address of the python server is ```localhost```
The prefered port is ```8080```, you can change this to your liking though.


Error Codes
----------------------------------
####401
Access denied. You shouldn't be trying whatever you are trying.
####403
There's something wrong with your URL.
####404
The page doesn't exist.
####405
You're using the wrong method to access this functionality of the API.
You might also be browsing to the wrong URL, so double check!


/reset => Creating the table ( same as resetting it )
-----------------------------------
The reset functionality resets the table and adds one item to the ~~empty~~ table.
It then returns the newly created table in JSON format.

|Value name    |   value|
|--------------|-------------|
|Name          | Banana|
|Category      | Fruit|
|Location      | Amsterdam|
|Date          | 2014-10-05|
|Amount        | 15|

####Resource URL:
```
localhost:8080/reset
```

####Resource information:

Method          | PUT
----------------|-----
Response format | JSON
Parameters      | None

####Parameters
None

/new => Adding a new item to the table
-----------------------------------
The new functionality adds a new item to the table.
It returns wether the addition was a succes and the added item's ID. 

| Variable    |    Value |
|-------------|----------|
|Addition     | Succes   |
|ID           | index in table |

Note that /new will always return Addition : succes, otherwise it returns nothing. 

####Resource URL:
```
localhost:8080/new
```

####Resource Information:

Method         | POST 
---------------|-----
Response format|JSON
Parameters     | Required

####Parameters

These Paramters are ALL required for the succesful addition of a new item.

Parameter Name  | Value format 
----------------|-----------------
name            | Alphanumerical characters
category        | ...
location        | ...
date            | Numbers and dashes
amount          | Numbers only

/edit[no]  => edit item on ID
-----------------------------------
Edit a specific item selected by ID
It returns wether the update was a succes. 

| Variable     |  Value |
|--------------|--------|
| Update       | Succes/Index unavailable |

####Resource URL:
```
localhost:8080/edit/[no]
```
where [no] is a valid number 

####Resource Information:

Method | PUT
-------|-----
Response Format | JSON
Parameters | Required

####Parameters
These Paramters are ALL required for succesfully changing an item's values.

Parameter Name  | Value format 
----------------|-----------------
name            | Alphanumerical characters
category        | ...
location        | ...
date            | Numbers and dashes
amount          | Numbers only

/help => Show help page
-----------------------------------
Links to the assignment3.html page

####Resource URL:
```
localhost:8080/help
```

####Resource Information:
Method | GET
-------|-----
Response format | Static file

/items/[no] => get Item by Id
-------------------------------------
Get an item from the database by navigating to items/[no] with [no] being its ID

Variable  |  Value
----------|----------
item      | Doesn't exist/its object data

####Resource URL:
```
localhost:8080/items/[no]
```
With [no] being its ID

####Resource Information

Method | GET
-------|-----
Response format | JSON
Parameters | None

####Parameters
None

/items => Get whole Inventory as json
-------------------------------------
Show the whole inventory

Variable | Value
---------|-----------
Inventory | Empty / Its object data

####Resource URL:
```
localhost:8080/items
```

####Resource Information:

Method | GET
-------|----------
Response format | JSON
Parameters  | None 

####Parameters
None

/deleterow[no] => Delete item instance by ID
---------------------------------------------
Delete an item by its ID.

Variable | Value
---------|-----------
Update   | Succes/Index unavailable

####Resource URL:
```
localhost:8080/deleterow[no]
```
where [no] is the item's ID.

####Resource Information

Method  |  DELETE
--------|-------
Response format | JSON
Parameters  | None

####Parameters 
None



##Examples
Some examples using the curl tool

###Getting all the inventory data
```
curl -X GET 'localhost:8080/items'
```
which returns something like:
```
{"Inventory": [{"amount": 15, "date": "2014-10-05", "category": "Fruit", "name": "Banana", "id": 1, "location": "Amsterdam"}]}
```
###Getting a single item 
```
curl -X GET 'localhost:8080/items/1'
```
returns:
```
{"item": [{"amount": 15, "date": "2014-10-05", "category": "Fruit", "name": "Banana", "id": 1, "location": "Amsterdam"}]}
```

###Adding an item
```
curl --data 'name=Melon&location=Peru&category=Fruit&date=2015-01-22&amount=15' 'localhost:8080/new'
```
returns:
```
{"Addition": "succes", "ID": 3}
```
Now we can see the table is updated:
```
curl -X GET 'localhost:8080/items'
{"Inventory": [{"amount": 15, "date": "2014-10-05", "category": "Fruit", "name": "Banana", "id": 1, "location": "Amsterdam"}, {"amount": 23, "date": "12-23-1023", "category": "123", "name": "123", "id": 2, "location": "123"}, {"amount": 15, "date": "2015-01-22", "category": "Fruit", "name": "Melon", "id": 3, "location": "Peru"}]}
```

###Deleting an item
```
curl -X DELETE 'localhost:8080/deleterow/3'
```
returns 
```
{"Update": "success"}
```
And once again we can see the table is updated:
```
curl -X GET 'localhost:8080/items'
{"Inventory": [{"amount": 15, "date": "2014-10-05", "category": "Fruit", "name": "Banana", "id": 1, "location": "Amsterdam"}, {"amount": 23, "date": "12-23-1023", "category": "123", "name": "123", "id": 2, "location": "123"}]}
```

###Resetting the table
```
curl -X PUT 'localhost:8080/reset'
```
returns
```
{"Inventory": [{"amount": 15, "date": "2014-10-05", "category": "Fruit", "name": "Banana", "id": 1, "location": "Amsterdam"}]
```
###Editing an item
```
curl -X PUT --data 'name=Melon&location=Peru&category=Fruit&date=2015-01-22&amount=25' 'localhost:8080/edit/2'
```
returns
```
{"Update": "success"}
```

###help?
Try that yourself, 
```
curl -X GET 'localhost:8080/help'
```
