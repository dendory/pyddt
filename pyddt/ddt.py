#
# Python DDT - (C) 2015 Patrick Lambert - Provided under the MIT License - https://github.com/dendory/pyddt
#
import uuid
import datetime

class DDT:
	def remove(self, name): # Remove an item
		if not name in self._data:
			raise ValueError("Name '" + str(name) + "' does not exist in dataset.")
		del self._data[name]

	def get(self, name): # Retrieve an item
		if not name in self._data:
			raise ValueError("Name '" + str(name) + "' does not exist in dataset.")
		return self._data[name]

	def add(self, data, name = None): # Add a new item
		if not name:
			name = uuid.uuid4()
		if name in self._data:
			raise ValueError("Name '" + str(name) + "' already exists in dataset.")
		if self._schema == {}:
			for k,v in data.items():
				self._schema[k.upper()] = type(v)
			self._data[name] = data
		else:
			data2 = {}
			for k,v in data.items():
				if k.upper() not in self._schema:
					raise ValueError("Key '" + str(k) + "' does not exist in schema.")
				elif self._schema[k.upper()] == type(self._available_types['DATE']):
					try:
						data2[k] = datetime.datetime.strptime(v, "%Y-%m-%d")
					except:
						raise ValueError("Type of '" + str(v) + "' does not match schema: " + str(self._schema[k.upper()]))					
				elif type(v) != self._schema[k.upper()]:
					raise ValueError("Type of '" + str(v) + "' does not match schema: " + str(self._schema[k.upper()]))
				else:
					data2[k] = v
			self._data[name] = data2		
		return name

	def set_schema(self, schema): # Manually set a schema
		for k,v in schema.items():
			if v.upper() not in self._available_types:
				raise ValueError("Invalid schema type: " + str(v))
			self._schema[k.upper()] = type(self._available_types[v.upper()])

	def get_schema(self): # Return the current schema
		return self._schema

	def __init__(self, schema = {}, constraints = {}, data = {}): # Initialize default values
		self._available_types = {"INT": 5, "STR": "aa", "FLOAT": 4.2, "BOOL": True, "DATE": datetime.date.today()}
		self._data = data
		self._constraints = constraints
		self._schema = schema
