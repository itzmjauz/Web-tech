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

Method          | POST
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

/help => Show help page
-----------------------------------

/json[no] => get Item on Id
-------------------------------------

/json => Get whole Inventory as json
-------------------------------------

