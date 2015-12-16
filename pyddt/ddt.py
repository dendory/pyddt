#
# Python DDT - (C) 2015 Patrick Lambert - Provided under the MIT License - https://github.com/dendory/pyddt
#
import uuid
import datetime
import hashlib
import pickle

version = "1.0"

class DDT:
	def remove(self, name): # Remove an item
		if not name in self._data:
			raise ValueError("Name '" + str(name) + "' does not exist in dataset.")
		del self._data[name]

	def get(self, name): # Retrieve an item
		if not name in self._data:
			raise ValueError("Name '" + str(name) + "' does not exist in dataset.")
		data2 = self._data[name]
		for k,v in data2.items():
			if self._schema[k.upper()] == type(self._available_types['DATE']): 
				data2[k] = str(v).split()[0]
			elif self._schema[k.upper()] == type(self._available_types['DATETIME']): 
				data2[k] = str(v)
			elif self._schema[k.upper()] == type(self._available_types['HASH']): 
				data2[k] = v.hexdigest()
			else:
				data2[k] = v
		return data2

	def save(self, filename): # Save dataset
		data2 = {'version': version, 'constraints': self._constraints, 'schema': self._schema, 'data': self._data}
		with open(filename, 'wb') as f:
			pickle.dump(data2, f, protocol=4)

	def load(self, filename): # Load dataset
		with open(filename, 'rb') as f:
			data2 = pickle.loads(f.read())
		self._data = data2['data']
		self._constraints = data2['constraints']
		self._schema = data2['schema']

	def add(self, data, name = None): # Add a new item
		if not name:
			name = str(uuid.uuid4())
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
				elif self._schema[k.upper()] == type(self._available_types['BOOLEAN']):
					if str(v).upper() == "FALSE" or str(v).upper() == "F" or str(v) == "0":
						data2[k] = False
					elif str(v).upper() == "TRUE" or str(v).upper() == "T" or str(v) == "1":
						data2[k] = True
					else:
						raise ValueError("Type of '" + str(v) + "' does not match schema: " + str(self._schema[k.upper()]))
				elif self._schema[k.upper()] == type(self._available_types['HASH']):
					m = hashlib.sha256()
					m.update(str(v).encode('utf-8'))
					data2[k] = m
				elif self._schema[k.upper()] == type(self._available_types['DATETIME']):
					try:
						data2[k] = datetime.datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
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
		self._available_types = {'INT': 5, 'STR': "aa", 'FLOAT': 4.2, 'BOOLEAN': True, 'DATETIME': datetime.datetime.now(), 'DATE': datetime.date.today(), 'ARRAY': [1,2], 'HASH': hashlib.sha256()}
		self._data = data
		self._constraints = constraints
		self._schema = schema
