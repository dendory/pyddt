# PyDDT
Python 3.4+ implementation of Dictionary Data Type

This library allows the storage and manipulation of records in datasets using a custom schema and dictionary structure. It provides many data types and utility functions to make it easy to deal with data in a fast and efficient manner.

## Data types

Valid data types for the schema include: STR, INT, FLOAT, ARRAY, BOOLEAN, DATETIME, HASH

Examples:
STR: "Hello world"
ARRAY: ["hello", "world", 34]
INT: 4
FLOAT: 1.00324
BOOLEAN: True
DATETIME: "2015-01-28 16:17:03"
HASH: sha256("Hello world")

## Usage

Import the module:

    import pyddt

Create a dataset. Here, you can optionally define the schema and initial data:

    mydata = pyddt.DDT()

Set the schema as a dictionary of labels and data types. Note that you don't have to manually set the schema, PyDDT can initialize it from the first record you add:

    myschema = {'name': 'STR', 'age': 'INT', 'creation': 'DATE'}
    mydata.set_schema(myschema)

Add records as dictionaries of data followed by the name of the record. The name is optional, and will be set to a unique ID if none is passed. The values must match the labels and data types from your schema:

    mydata.add({'name': "John Smith", 'age': 24, 'creation': "2007-01-27"}, "REC-001")
    mydata.add({'name': "Jane Smith", 'age': 21, 'creation': "2009-11-16"}, "REC-002")
    mydata.add({'name': "Tom McCarthy", 'age': 35, 'creation': "2005-06-08"})

Retrieve a record:

    print(mydata.get("REC-002"))

Remove a record:

    mydata.remove("REC-002")
    